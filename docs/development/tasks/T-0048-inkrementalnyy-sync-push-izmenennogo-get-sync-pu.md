---
id: T-0048
type: task
title: 'Инкрементальный sync: push изменённого, GET /sync/pull?since='
status: backlog
change: feature
created: 2026-09-30
updated: 2026-09-30
links:
  implements: [R-0025]
  decided_by: [A-0014]
---

# Инкрементальный sync: push изменённого, GET /sync/pull?since=

Push сейчас каждый раз отправляет все локальные активности; pull отдаёт всё. Нужно: push только изменённого после прошлого sync; сервер принимает параметр since для pull (в порту клиента он уже есть).

## Журнал

- 2026-09-30 · заведена из docs/inbox/sync-and-jobs.md · приложение
- 2026-10-01 · добавлены связи вне приложения: decided_by A-0014 · claude
