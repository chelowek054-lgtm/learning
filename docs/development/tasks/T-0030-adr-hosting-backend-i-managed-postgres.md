---
id: T-0030
type: task
title: 'ADR: хостинг backend и managed Postgres'
status: in_review
change: feature
reuse: none
created: 2026-09-30
updated: 2026-10-11
links:
  implements: [R-0020]
  affects: [M-0003]
---

# ADR: хостинг backend и managed Postgres

Выбор хостинга (Fly.io/Railway/VPS) и БД (Supabase/Neon); документ 60-operations/environments.md.

## Журнал

- 2026-09-30 · заведена из docs/inbox/platform-and-release.md · приложение
- 2026-10-03 · предложение по хостингу положено заметкой в docs/inbox/decision-hosting.md (варианты, рекомендация для staging, что не выяснено); выбор за человеком, статус не меняю · claude
- 2026-10-11 · черновик сравнения и рекомендации лежит в docs/60-operations/environments.md (свой VPS с docker compose на старте; ограничение — pgvector и Apache AGE); выбор хостинга и страны за человеком; запись ADR заводит консоль после вычитки · claude
- 2026-10-11 · повторная проверка 2026-10-11: ЖДЁТ ВНЕШНЕГО: выбор хостинга и страны за человеком (ADR после вычитки hosting-options.md) · claude
