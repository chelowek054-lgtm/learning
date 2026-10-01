---
id: A-0014
type: decision
title: Raw expo-sqlite за портом LocalStore вместо Drizzle; web — in-memory
status: approved
created: 2026-09-30
updated: 2026-10-01
---

# Raw expo-sqlite за портом LocalStore вместо Drizzle; web — in-memory

Принято 2026-07-04. Исходный план предполагал Drizzle ORM, но её миграции требуют codegen и настройки Metro под .sql, непроверяемой без устройства; на web expo-sqlite тянет wa-sqlite.wasm с требованиями COEP/OPFS. Решено использовать SQLite напрямую (CREATE TABLE IF NOT EXISTS, синхронный API) за портом LocalStore; на web — платформенная in-memory замена sqlite-local-store.web.ts. WatermelonDB отвергнут — навязывает свою модель синхронизации. Замена хранилища затрагивает только адаптер; на web данные теряются при перезагрузке — приемлемо, web не целевая платформа.

## Журнал

- 2026-09-30 · заведена из docs/inbox/decision-raw-expo-sqlite.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
