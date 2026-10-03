---
id: T-0047
type: task
title: Push прогресса FSRS с LWW по updated_at
status: done
change: feature
created: 2026-09-30
updated: 2026-10-01
links:
  implements: [R-0025]
  affects: [M-0003, M-0011]
---

# Push прогресса FSRS с LWW по updated_at

Добавить srs_card.updated_at на клиенте и сервере (миграция); push изменённых карточек; pull применяет только более новые по updated_at, не затирая локальный прогресс.

## Журнал

- 2026-09-30 · заведена из docs/inbox/sync-and-jobs.md · приложение
- 2026-10-01 · готова к работе · claude
- 2026-10-01 · взята в работу · claude
- 2026-10-01 · на проверку · claude
- 2026-10-01 · выполнена · реализовано в миграции 0011, тесты test_sync и sync-service.test · claude
- 2026-10-03 · связь с картой M-0011: она объявляет возможность, которую меняет задача (сверка map_capability_missing) · claude
