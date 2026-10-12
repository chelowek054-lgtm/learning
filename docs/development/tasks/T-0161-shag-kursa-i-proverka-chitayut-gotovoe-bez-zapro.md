---
id: T-0161
type: task
title: Шаг курса и проверка читают готовое, без запросов к модели
status: in_progress
change: feature
created: 2026-10-12
updated: 2026-10-13
links:
  implements: [R-0075]
  depends_on: [T-0160]
  verified_by: [V-0134]
  affects: [M-0051]
---

# Шаг курса и проверка читают готовое, без запросов к модели

modules/knowledge/study.py, assessment.py и клиент берут теорию и задания из собранного узла; модель — только для открытых ответов и личных материалов.

## Журнал

- 2026-10-12 · заведена из docs/inbox/sborka-uzla-i-bank-zadaniy-bez-llm-pri-obuchenii.md · приложение
- 2026-10-13 · learningBack#80 (влит), CI main зелёный: GET /graph/nodes/{id}/items отдаёт готовые задания с ключами. НЕ СДЕЛАНО: шаг курса и проверка в клиенте и в study.py/assessment.py по-прежнему ходят через старый путь · claude
