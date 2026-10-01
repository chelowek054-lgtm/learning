---
id: V-0029
type: verification
title: Удаление аккаунта
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0018, T-0027, T-0028, T-0044]
---

# Удаление аккаунта

Unit, pytest: `будет: cd learningBack && uv run pytest tests/test_account_delete.py -q`. Доказывает: после удаления в БД нет строк пользователя, кроме анонимизированной статистики. Пройдена, когда тест написан вместе с T-0028. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-data-policy.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
