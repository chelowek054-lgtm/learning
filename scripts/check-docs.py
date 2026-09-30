"""Проверка относительных ссылок в markdown документации (P3-CI-03).

Запуск из корня суперпроекта: python scripts/check-docs.py
Проверяет README.md, ROADMAP.md и docs/** (кроме archive/). Внешние ссылки и
якоря пропускаются; ссылки внутрь сабмодулей не проверяются, если сабмодуль пуст.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")


def files() -> list[Path]:
    out = [ROOT / "README.md", ROOT / "ROADMAP.md"]
    out += [p for p in (ROOT / "docs").rglob("*.md") if "archive" not in p.parts]
    return out


def main() -> int:
    bad: list[str] = []
    for f in files():
        for target in LINK.findall(f.read_text(encoding="utf-8")):
            if target.startswith(("http:", "https:", "mailto:")):
                continue
            path = Path(os.path.normpath(f.parent / target))
            if not path.exists():
                bad.append(f"{f.relative_to(ROOT)}: {target}")
    for line in bad:
        print("битая ссылка:", line)
    print(f"проверено файлов: {len(files())}, битых ссылок: {len(bad)}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
