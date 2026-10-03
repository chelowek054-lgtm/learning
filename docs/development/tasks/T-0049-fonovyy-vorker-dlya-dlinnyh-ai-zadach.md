---
id: T-0049
type: task
title: Фоновый воркер для длинных AI-задач
status: in_review
change: feature
created: 2026-09-30
updated: 2026-10-03
links:
  implements: [R-0025, R-0023]
  decided_by: [A-0007]
  affects: [M-0003]
---

# Фоновый воркер для длинных AI-задач

Синхронная обработка jobs на /sync/push (d-jobs-on-push) не укладывается в таймаут для STT и генерации аудио. Нужен ADR о воркере и реализация до начала Ф4 (речь).

## Журнал

- 2026-09-30 · заведена из docs/inbox/sync-and-jobs.md, docs/inbox/speaking.md · приложение
- 2026-10-01 · добавлены связи вне приложения: decided_by A-0007 · claude
- 2026-10-03 · взята в работу: отдельный процесс-воркер берёт pending-jobs с блокировкой SKIP LOCKED, режим jobs_mode=worker отключает обработку на /sync/push · claude
- 2026-10-03 · на проверку, learningBack#26 слита: core/worker, scripts/worker, jobs_mode=worker (по умолчанию inline), сервис worker в docker-compose по профилю; не проверено: параллельная работа нескольких воркеров на реальной базе (SKIP LOCKED опирается на Postgres, тест — один воркер), запуск на staging; V-0064 не подтверждена человеком · claude
