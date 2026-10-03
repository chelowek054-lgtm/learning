---
id: T-0016
type: task
title: Вопросы concept_recall из материала
status: done
change: feature
created: 2026-09-30
updated: 2026-10-01
links:
  implements: [R-0011, R-0014]
  depends_on: [T-0015]
  affects: [M-0003, M-0011]
---

# Вопросы concept_recall из материала

Оживить modules/ml/generators.py: concept_recall_from_material сейчас нигде не вызывается — генерация вопросов из материала отложена до импорта.

## Журнал

- 2026-09-30 · заведена из docs/inbox/learning-expansion.md, docs/inbox/ml-track.md · приложение
- 2026-10-01 · готова к работе · claude
- 2026-10-01 · взята в работу · claude
- 2026-10-01 · на проверку · тесты test_material_nodes: вопросы с опорой на фрагменты, без дублей; живой вызов модели не запускался; клиентская кнопка в работе · claude
- 2026-10-01 · выполнена · тесты test_material_nodes: вопросы с опорой на фрагменты, без дублей; живой вызов модели не запускался; клиентская кнопка в работе · claude
- 2026-10-03 · связь с картой M-0011: она объявляет возможность, которую меняет задача (сверка map_capability_missing) · claude
