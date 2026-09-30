"""Прогон автоматических проверок DocDD и запись отчёта (docs/02-workspace-contract.md, «Отчёты»).

Запуск из корня проекта: python scripts/docdd-report.py [--dry-run]

Берёт записи типа verification из docs/development/tests, у каждой читает поле
`command`, выполняет его и пишет `docs/development/tests/reports/<дата>-local.json`:
`V-xxxx → passed | failed`. Результат — факт, его нельзя поставить руками: по нему
консоль отличает «подтверждено прогоном» от «только объявлено».

Пропускаются проверки без `command`, ручные (kind: manual, review) и те, чья
команда начинается со слова «будет» — теста ещё нет, и выдавать его за упавший
нечестно: такая проверка остаётся без результата (`verification_never_run`).
"""

from __future__ import annotations

import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TESTS = ROOT / "docs" / "development" / "tests"
REPORTS = TESTS / "reports"
TIMEOUT_SECONDS = 900


def front_matter(text: str) -> dict[str, str]:
    m = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.S)
    if not m:
        return {}
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if kv:
            value = kv.group(2).strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
                value = value[1:-1].replace("''", "'")
            out[kv.group(1)] = value
    return out


def runnable() -> tuple[list[tuple[str, str]], list[str]]:
    """(id, команда) для автоматических проверок и id пропущенных."""
    todo: list[tuple[str, str]] = []
    skipped: list[str] = []
    for f in sorted(TESTS.glob("V-*.md")):
        fm = front_matter(f.read_text(encoding="utf-8"))
        vid, command = fm.get("id", ""), fm.get("command", "")
        if not vid:
            continue
        if fm.get("kind") in ("manual", "review") or not command or command.startswith("будет"):
            skipped.append(vid)
        else:
            todo.append((vid, command))
    return todo, skipped


def main() -> int:
    dry = "--dry-run" in sys.argv
    todo, skipped = runnable()
    print(f"автоматических проверок: {len(todo)}, без запуска (ручные/ещё нет теста): {len(skipped)}")
    if dry:
        for vid, cmd in todo:
            print(f"  {vid}: {cmd}")
        return 0

    started = dt.datetime.now(dt.timezone.utc)
    results: dict[str, str] = {}
    for vid, command in todo:
        try:
            proc = subprocess.run(
                command, shell=True, cwd=ROOT, capture_output=True, timeout=TIMEOUT_SECONDS
            )
            results[vid] = "passed" if proc.returncode == 0 else "failed"
        except subprocess.TimeoutExpired:
            results[vid] = "failed"
        print(f"  {results[vid]:6} {vid}  {command[:80]}")

    failed = sum(1 for v in results.values() if v == "failed")
    REPORTS.mkdir(parents=True, exist_ok=True)
    out = REPORTS / f"{started.date().isoformat()}-local.json"
    out.write_text(
        json.dumps(
            {
                "contract": "docdd.workspace/1",
                "runner": "local",
                "started_at": started.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "total": len(results),
                "failed": failed,
                "verifications": results,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"отчёт: {out.relative_to(ROOT)}; упало: {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
