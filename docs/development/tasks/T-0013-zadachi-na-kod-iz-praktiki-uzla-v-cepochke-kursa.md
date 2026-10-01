---
id: T-0013
type: task
title: Задачи на код из практики узла в цепочке курса
status: in_review
change: feature
created: 2026-09-30
updated: 2026-10-01
links:
  implements: [R-0010, R-0007]
  decided_by: [A-0003]
  depends_on: [T-0011, T-0012]
  affects: [M-0003]
---

# Задачи на код из практики узла в цепочке курса

Для технических предметов практика apply в цепочке курса (SPEC-11) должна порождать задачу на код, а не только concept_apply.

## Журнал

- 2026-09-30 · заведена из docs/inbox/learning-expansion.md, docs/inbox/course-and-study.md · приложение
- 2026-10-01 · добавлены связи вне приложения: decided_by A-0003 · claude
- 2026-10-01 · готова к работе · claude
- 2026-10-01 · взята в работу · хук модуля для практики, не ломающий независимость ядра (A-0001) · claude
- 2026-10-01 · на проверку · тесты test_course и test_study: хук apply_activity, ядро без имён модулей; на устройстве не проверялось · claude
