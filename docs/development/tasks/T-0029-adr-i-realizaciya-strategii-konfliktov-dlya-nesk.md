---
id: T-0029
type: task
title: ADR и реализация стратегии конфликтов для нескольких устройств
status: in_review
change: feature
created: 2026-09-30
updated: 2026-10-03
links:
  implements: [R-0019]
  affects: [M-0003]
---

# ADR и реализация стратегии конфликтов для нескольких устройств

Принять ADR: слияние srs_card по fsrs_state.last_review вместо времени записи; реализовать на sync push/pull.

## Журнал

- 2026-09-30 · заведена из docs/inbox/platform-and-release.md · приложение
- 2026-10-03 · взята в работу: слияние карточки по последнему ревью (fsrs_state.last_review), а не по времени записи; сервер и клиент; решение для записи ADR — заметка в docs/inbox · claude
- 2026-10-03 · на проверку, learningBack#27 и learningFront#19 слиты: слияние карточки по последнему ревью на сервере и клиенте; решение для ADR положено в docs/inbox/decision-card-merge-by-last-review.md (записи заводит консоль); V-0055 не подтверждена человеком, на двух устройствах не проверялось · claude
