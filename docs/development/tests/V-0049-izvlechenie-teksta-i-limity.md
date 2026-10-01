---
id: V-0049
type: verification
title: Извлечение текста и лимиты
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0011, T-0014, T-0015, T-0016]
---

# Извлечение текста и лимиты

Unit, pytest: `будет: cd learningBack && uv run pytest tests/test_material_import.py -q`. Доказывает: PDF и Markdown до 20 МБ разбиваются на фрагменты, больший файл отклоняется с причиной. Пройдена, когда тест написан вместе с T-0014. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-material-import.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
