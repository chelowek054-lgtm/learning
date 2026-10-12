---
id: T-0153
type: task
title: Ссылки на источник у утверждений в API для учащегося
status: in_review
change: feature
created: 2026-10-12
updated: 2026-10-13
links:
  implements: [R-0072]
  depends_on: [T-0149, T-0152]
  verified_by: [V-0131]
  affects: [M-0051]
---

# Ссылки на источник у утверждений в API для учащегося

Ответ теории узла для учащегося включает у утверждений название, автора, лицензию, место и адрес с якорем; фрагмент — только при разрешающей лицензии. Переиспользует modules/knowledge/provenance_api.py.

## Журнал

- 2026-10-12 · заведена из docs/inbox/istochniki-tolko-s-licenziey-i-vidimost-uchaschemusya.md · приложение
- 2026-10-13 · learningBack#80 (влит), CI main зелёный: GET /graph/nodes/{id}/claims отдаёт учащемуся утверждения с названием источника, лицензией, страницей, ссылкой и цитатой (цитата — только при разрешающей лицензии) · claude
