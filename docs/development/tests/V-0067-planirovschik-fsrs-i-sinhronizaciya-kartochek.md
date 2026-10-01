---
id: V-0067
type: verification
title: Планировщик FSRS и синхронизация карточек
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0024, T-0004, T-0026, T-0045]
---

# Планировщик FSRS и синхронизация карточек

Unit, npm: `cd learningFront && npx vitest run src/shared/engine/scheduler src/shared/api`. Доказывает: ответ меняет состояние и срок без сети; изменённые карточки уходят на сервер, пришедшие — не возвращаются. Пройдена, когда все тесты проходят. Состояние: есть и проходит на 2026-09-30.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-srs-and-error-log.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
