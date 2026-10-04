---
id: T-0038
type: task
title: 'Job explain_distractors: разбор дистракторов при сети'
status: in_review
change: feature
created: 2026-09-30
updated: 2026-10-04
links:
  implements: [R-0022]
  verified_by: [V-0060]
  affects: [M-0003, M-0011]
---

# Job explain_distractors: разбор дистракторов при сети

Разбор «почему этот вариант неверен» приходит job-ом при сети и не блокирует прохождение дрилла.

## Журнал

- 2026-09-30 · заведена из docs/inbox/reception-drills.md · приложение
- 2026-10-04 · взята в работу, сделана: хук job_handlers в контракте модуля, job explain_distractors (learningBack PR 31), клиент ставит job на ошибки с выбором (learningFront PR 20) · claude
- 2026-10-04 · на проверку: тесты проходят; показ разбора на экране дрилла не сделан — клиенту нужен метод чтения job-результата из локального хранилища · claude
