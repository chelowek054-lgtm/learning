---
id: T-0155
type: task
title: Принадлежность понятия к областям
status: in_progress
change: feature
created: 2026-10-12
updated: 2026-10-13
links:
  implements: [R-0073]
  verified_by: [V-0132]
  affects: [M-0051]
---

# Принадлежность понятия к областям

Связь «понятие — область» с этапом, уровнем и необязательностью; миграция; курс, схема, плейсмент и освоенность читают через неё. Переиспользует modules/knowledge/models.py, course.py, placement.py.

## Журнал

- 2026-10-12 · заведена из docs/inbox/odno-ponyatie-v-neskolkih-oblastyah.md · приложение
- 2026-10-13 · learningBack#80 (влит), CI main зелёный: concept_area заполняется при извлечении и при слиянии, поиск похожих идёт по всему графу. НЕ СДЕЛАНО: курс, схема, плейсмент и освоенность по-прежнему читают concept.domain, а не принадлежность через concept_area · claude
