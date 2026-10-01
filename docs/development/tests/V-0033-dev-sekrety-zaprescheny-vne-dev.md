---
id: V-0033
type: verification
title: Dev-секреты запрещены вне dev
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0020, T-0030, T-0031, T-0032, T-0033, T-0034]
---

# Dev-секреты запрещены вне dev

Unit, pytest: `будет: cd learningBack && uv run pytest tests/test_secrets_guard.py -q`. Доказывает: сервер не стартует в staging/prod с dev-значениями секретов. Пройдена, когда тест написан вместе с T-0032. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-deploy-and-release.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
