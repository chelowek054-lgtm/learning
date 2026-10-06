---
id: V-0094
type: verification
title: Источники, разбор в граф со ссылками на фрагмент, слияние и поиск
status: draft
created: 2026-10-06
updated: 2026-10-06
kind: manual
links:
  verifies: [R-0043]
---

# Источники, разбор в граф со ссылками на фрагмент, слияние и поиск

Чем проверяется: расширения Postgres и объектное хранилище, разбор документа в понятия с проверкой цитаты по тексту, слияние дублей по близости и решению модели, поиск по белому списку, поиск по пробелам графа для администратора, резервные копии объектов.
Команда: `cd learningBack && uv run pytest tests/test_graph_extensions.py tests/test_objects.py tests/test_backup_objects.py tests/test_provenance.py tests/test_ingest.py tests/test_merge.py tests/test_source_search.py tests/test_gap_search.py tests/test_migrations_match_models.py -q && cd ../learningFront && npx vitest run src/features/sources`

## Журнал

- 2026-10-06 · заведена · приложение
