---
id: T-0072
type: task
title: Переход на PostgreSQL 17 с AGE и pgvector
status: in_review
change: feature
created: 2026-10-06
updated: 2026-10-06
links:
  implements: [R-0043]
  decided_by: [A-0026, A-0024]
  affects: [M-0026]
---

# Переход на PostgreSQL 17 с AGE и pgvector

Образ Postgres 17 с расширениями в docker-compose, миграция Alembic с расширениями и схемой графа, перенос данных с проверкой восстановления, откат.

## Журнал

- 2026-10-06 · заведена из docs/inbox/decision-postgres-17-migration.md, docs/inbox/decision-graph-database.md · приложение
- 2026-10-06 · взята в работу, сделана: образ `deploy/postgres` (PostgreSQL 17.11, Apache AGE 1.7.0, pgvector 0.8.7), миграция 0025 создаёт расширения и граф `knowledge`, данные перенесены через pg_dump после проверенной копии (26 таблиц, версия миграции совпала), старый каталог данных PG16 сохранён рядом в `.data/postgres16-…` (learningBack PR 39) · claude
- 2026-10-06 · найдено при проверке: дамп с `--clean` падает при накате в пустую базу, потому что AGE на DROP EXTENSION без расширения в базе даёт ошибку; `scripts/restore-check.sh` теперь заранее создаёт расширения, правило записано в `docs/60-operations/environments.md` · claude
- 2026-10-06 · на проверку: тесты бэкенда проходят на PG 17 (Cypher-обход предпосылок, векторный поиск); отдельной записи проверки нет; не проверено на staging · claude
- 2026-10-06 · связь implements R-0043: переход базы — основание для хранения и слияния знаний из источников · claude
