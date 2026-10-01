---
id: T-0049
type: task
title: Фоновый воркер для длинных AI-задач
status: backlog
change: feature
created: 2026-09-30
updated: 2026-10-01
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
