---
id: T-0164
type: task
title: Проверка ссылок на оригинал
status: in_review
change: feature
created: 2026-10-12
updated: 2026-10-12
links:
  implements: [R-0076]
  depends_on: [T-0149]
  verified_by: [V-0135]
  affects: [M-0051]
---

# Проверка ссылок на оригинал

Периодическая проверка адресов источников; мёртвая ссылка помечается, сохранённый фрагмент остаётся.

## Журнал

- 2026-10-12 · заведена из docs/inbox/protukhanie-znaniy-v-grafe.md · приложение
- 2026-10-12 · learningBack#81 (влит), CI зелёный: задача check_links и POST /graph/sources/check-links проверяют адреса источников (HEAD, при отказе GET) раз в 30 дней; мёртвая ссылка помечается в meta и в ответе утверждений (linkDead), фрагмент и атрибуция остаются · claude
