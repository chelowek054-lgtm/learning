"""Матрица «требование → спека → задачи» (docs/50-plans/traceability.md).

Запуск из корня суперпроекта: python scripts/gen-traceability.py
Читает docs/10-requirements/functional.md и таблицы задач docs/50-plans/phase-*.md,
обновляет сводку в functional.md и пишет traceability.md. Завершается с кодом 1,
если есть требование в статусе accepted/partial без единой задачи плана.
"""

from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FR_FILE = ROOT / "docs/10-requirements/functional.md"
PLANS = sorted((ROOT / "docs/50-plans").glob("phase-*.md"))
OUT = ROOT / "docs/50-plans/traceability.md"

REQ = re.compile(r"^\| (FR-[A-Z]+-\d+) \| .+? \| .+? \| (SPEC-\d+) \| (\w+) \|$", re.M)
TASK = re.compile(r"^\| (P\d-[A-Z0-9]+-\d+) \| .*? \| (.*?) \| (\S+) \|", re.M)


def main() -> int:
    fr_text = FR_FILE.read_text(encoding="utf-8").replace("\r\n", "\n")
    reqs = REQ.findall(fr_text)
    status_count = collections.Counter(r[2] for r in reqs)

    tasks: dict[str, list[str]] = collections.defaultdict(list)
    for plan in PLANS:
        text = plan.read_text(encoding="utf-8").replace("\r\n", "\n")
        for tid, trace, state in TASK.findall(text):
            for fid in re.findall(r"FR-[A-Z]+-\d+", trace):
                tasks[fid].append(f"{tid} {state}")

    lines = [
        "# Матрица трассировки",
        "",
        "Требование → спека → задачи плана. Сгенерировано `scripts/gen-traceability.py` из "
        "`10-requirements/functional.md` и таблиц задач `phase-*.md`; не править руками.",
        "",
        "| Требование | Спека | Статус | Задачи |",
        "|---|---|---|---|",
    ]
    for fid, spec, status in [(r[0], r[1], r[2]) for r in reqs]:
        lines.append(f"| {fid} | {spec} | {status} | {', '.join(tasks.get(fid, [])) or '—'} |")

    orphans = [
        r[0] for r in reqs if r[2] in ("accepted", "partial") and not tasks.get(r[0])
    ]
    lines += [
        "",
        "Требования в статусе accepted/partial без задач плана: " + (", ".join(orphans) or "нет") + ".",
    ]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    summary = f"Сводка: **{len(reqs)} требований**: " + ", ".join(
        f"`{k}` {v}" for k, v in status_count.most_common()
    ) + "."
    new_text = re.sub(r"Сводка: \*\*\d+ требований\*\*.*", summary, fr_text)
    FR_FILE.write_text(new_text, encoding="utf-8", newline="\n")

    print(summary)
    for o in orphans:
        print("требование без задачи:", o)
    return 1 if orphans else 0


if __name__ == "__main__":
    sys.exit(main())
