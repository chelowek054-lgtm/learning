---
id: V-0098
type: verification
title: Загрузка проверенного учебника в канон графа
status: approved
created: 2026-10-06
updated: 2026-10-07
kind: manual
links:
  verifies: [R-0047]
---

# Загрузка проверенного учебника в канон графа

Чем проверяется: администратор загружает PDF, Markdown или текст, дубли по содержимому не плодятся, скан без текстового слоя отклоняется, ход разбора виден, удаление источника убирает выведенное только из него.
Команда: `cd learningBack && uv run pytest tests/test_source_upload.py tests/test_ingest.py tests/test_provenance.py -q && cd ../learningFront && npx vitest run src/features/sources`

## Журнал

- 2026-10-06 · заведена · приложение
- 2026-10-07 · на подтверждение · architect
- 2026-10-07 · подтверждён · architect
