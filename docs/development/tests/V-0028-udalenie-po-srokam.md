---
id: V-0028
type: verification
title: Удаление по срокам
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0018, T-0027, T-0028, T-0044]
---

# Удаление по срокам

Unit, pytest: `будет: cd learningBack && uv run pytest tests/test_retention.py -q`. Доказывает: данные с истёкшим сроком удаляются периодической задачей, свежие остаются. Пройдена, когда тест написан вместе с T-0028. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-data-policy.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
