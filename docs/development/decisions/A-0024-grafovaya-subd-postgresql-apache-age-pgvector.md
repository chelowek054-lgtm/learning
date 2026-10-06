---
id: A-0024
type: decision
title: 'Графовая СУБД: PostgreSQL + Apache AGE + pgvector'
status: approved
created: 2026-10-06
updated: 2026-10-06
---

# Графовая СУБД: PostgreSQL + Apache AGE + pgvector

Решение: граф хранится и обходится в той же базе, что и остальные данные: PostgreSQL 17 с расширениями Apache AGE (Cypher) и pgvector (поиск кандидатов на слияние). Таблицы concept, concept_edge, domain_edge остаются источником правды на переходе. Отдельная графовая СУБД (Neo4j Community) — только если замер обходов покажет узкое место.
Почему: одна транзакция и без синхронизации двух хранилищ; открытые лицензии; наш масштаб — сотни тысяч узлов. Отвергнуты: ArangoDB, Memgraph, FalkorDB (не открытые лицензии), Kùzu (заархивирован в октябре 2025), NebulaGraph и JanusGraph (избыточны).

## Журнал

- 2026-10-06 · заведена из docs/inbox/decision-graph-database.md, docs/inbox/decision-knowledge-pipeline-and-graph-db.md · приложение
- 2026-10-06 · подтверждён · пользователь (в чате: «Подтвердил»); для A-0028 принято предложение — белый список каталогов, затем API поиска
