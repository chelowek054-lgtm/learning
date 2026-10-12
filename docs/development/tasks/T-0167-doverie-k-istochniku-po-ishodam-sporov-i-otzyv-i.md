---
id: T-0167
type: task
title: Доверие к источнику по исходам споров и отзыв источника
status: in_review
change: feature
created: 2026-10-12
updated: 2026-10-12
links:
  implements: [R-0077]
  depends_on: [T-0165, T-0169]
  verified_by: [V-0136]
  affects: [M-0051]
---

# Доверие к источнику по исходам споров и отзыв источника

Пересчёт уровня доверия по проигранным спорам; отзыв источника с каскадом через provenance.remove_document.

## Журнал

- 2026-10-12 · заведена из docs/inbox/oshibochnyy-konsensus-i-ispravlenie-znaniy.md, docs/inbox/otsev-nelikvidnyh-istochnikov.md · приложение
- 2026-10-12 · learningBack#81 (влит), CI зелёный: проигранный спор (решения a/b) отмечается у источников проигравшего утверждения; 3 → A понижается до B, 5 → до C, 8 при C → карантин; отзыв источника POST /graph/sources/{id}/revoke через provenance.remove_document (изучаемое отклоняется с записью). НЕ СДЕЛАНО: кнопки отзыва в клиенте, метрики противоречий и доли нового · claude
