---
id: T-0031
type: task
title: 'Staging: деплой из main с миграциями и бэкапами'
status: in_progress
change: feature
created: 2026-09-30
updated: 2026-10-03
links:
  implements: [R-0020]
  decided_by: [A-0015, A-0017, A-0019]
  depends_on: [T-0030]
  affects: [M-0003]
---

# Staging: деплой из main с миграциями и бэкапами

Деплой staging из main, миграции применяются до старта нового API, настроены бэкапы БД.

## Журнал

- 2026-09-30 · заведена из docs/inbox/platform-and-release.md · приложение
- 2026-10-01 · добавлены связи вне приложения: decided_by A-0015, decided_by A-0017, decided_by A-0019 · claude
- 2026-10-03 · сделано без привязки к площадке: deploy/docker-compose.staging.yml (секреты обязательны, база закрыта, воркер всегда), scripts/deploy-staging.sh (код → образы → копия и проверка её восстановления → API с миграциями → /health), scripts/backup-db.sh, scripts/restore-check.sh, docs/60-operations/environments.md; копия и восстановление проверены на локальной базе (26 таблиц, миграция совпала); НЕ сделано: деплой на реальный сервер (ждёт выбора хостинга T-0030), запуск из CI, вынос копий за пределы сервера; V-0032 пройти можно только на сервере · claude
