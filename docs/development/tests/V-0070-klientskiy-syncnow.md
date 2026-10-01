---
id: V-0070
type: verification
title: Клиентский syncNow
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0025, T-0046, T-0047, T-0048, T-0049, T-0050]
---

# Клиентский syncNow

Unit, npm: `cd learningFront && npx vitest run src/shared/api/sync-service.test.ts`. Доказывает: изменённые карточки уходят и помечаются, пришедшие не возвращаются, pull не затирает локальный прогресс, статус failed переносится с причиной. Пройдена, когда все тесты проходят. Состояние: есть и проходит на 2026-09-30.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-sync-and-jobs.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
