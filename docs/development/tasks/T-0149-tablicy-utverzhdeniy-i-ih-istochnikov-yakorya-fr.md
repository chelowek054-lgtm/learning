---
id: T-0149
type: task
title: Таблицы утверждений и их источников, якоря фрагментов
status: in_review
change: feature
created: 2026-10-12
updated: 2026-10-13
links:
  decided_by: [A-0033]
  implements: [R-0071]
  verified_by: [V-0130]
  affects: [M-0051]
---

# Таблицы утверждений и их источников, якоря фрагментов

Утверждение и ссылка утверждения на фрагмент (цитата, смещения, отметка проверки); у фрагмента смещения и адрес с якорем; миграция. Переиспользует modules/knowledge/models.py (SourceFragment, ConceptSource) и provenance.py.

## Журнал

- 2026-10-12 · заведена из docs/inbox/utverzhdenie-edinica-znaniya-grafa.md · приложение
- 2026-10-12 · добавлена связь decided_by A-0033 (единица знания — утверждение), перенесена с требования · claude
- 2026-10-13 · learningBack#80 (влит), CI main зелёный: таблицы claim, claim_source, claim_conflict, concept_term, concept_area, learning_item и поля источника (язык, уровень доверия, карантин), миграция 0035. Проверки не писались (по просьбе) · claude
