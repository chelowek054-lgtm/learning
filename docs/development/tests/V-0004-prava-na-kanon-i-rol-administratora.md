---
id: V-0004
type: verification
title: Права на канон и роль администратора
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0003, T-0001]
---

# Права на канон и роль администратора

Integration, pytest: `cd learningBack && uv run pytest tests/test_graph_access.py tests/test_auth.py -q`. Доказывает: запись в канон доступна только is_superuser, обычный пользователь получает 403, роль не выдаётся через регистрацию. Пройдена, когда все тесты проходят. Состояние: есть и проходит на 2026-09-30.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-admin-and-curation.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
