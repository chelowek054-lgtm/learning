---
id: T-0047
type: task
title: Push прогресса FSRS с LWW по updated_at
status: backlog
change: feature
created: 2026-09-30
updated: 2026-09-30
links:
  implements: [R-0025]
---

# Push прогресса FSRS с LWW по updated_at

Добавить srs_card.updated_at на клиенте и сервере (миграция); push изменённых карточек; pull применяет только более новые по updated_at, не затирая локальный прогресс.

## Журнал

- 2026-09-30 · заведена из docs/inbox/sync-and-jobs.md · приложение
