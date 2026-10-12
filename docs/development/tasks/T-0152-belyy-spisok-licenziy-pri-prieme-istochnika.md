---
id: T-0152
type: task
title: Белый список лицензий при приёме источника
status: in_review
change: feature
created: 2026-10-12
updated: 2026-10-13
links:
  implements: [R-0072]
  verified_by: [V-0131]
  affects: [M-0051]
---

# Белый список лицензий при приёме источника

Проверка лицензии в modules/knowledge/source_search.py и при ручной загрузке; список в настройках; причина отказа видна администратору.

## Журнал

- 2026-10-12 · заведена из docs/inbox/istochniki-tolko-s-licenziey-i-vidimost-uchaschemusya.md · приложение
- 2026-10-13 · learningBack#80 (влит), CI main зелёный: белый список лицензий (настройки source_licenses_allowed), источник без разрешённой лицензии отклоняется на воронке до извлечения с причиной в trust_reasons · claude
