---
id: V-0076
type: verification
title: Эссе → оценка → карточки
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0026, T-0025]
---

# Эссе → оценка → карточки

Integration, pytest: `cd learningBack && uv run pytest tests/test_sync.py -k "grades_job or repeated_push" -q`. Доказывает: эссе оценивается по рубрике, оценка несёт версию рубрики, ошибки становятся карточками, повторный push не оценивает дважды. Пройдена, когда тесты проходят. Состояние: есть и проходит на 2026-09-30.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-writing-task2.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
