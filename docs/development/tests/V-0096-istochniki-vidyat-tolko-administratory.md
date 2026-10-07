---
id: V-0096
type: verification
title: Источники видят только администраторы
status: approved
created: 2026-10-06
updated: 2026-10-07
kind: manual
links:
  verifies: [R-0045]
---

# Источники видят только администраторы

Чем проверяется: обход всех GET-маршрутов от имени учащегося не находит ни одного пути к источникам, документам и ссылкам на файлы; маршруты источников отвечают 403.
Команда: `cd learningBack && uv run pytest tests/test_sources_admin_only.py tests/test_source_search.py tests/test_source_upload.py -q`

## Журнал

- 2026-10-06 · заведена · приложение
- 2026-10-07 · на подтверждение · architect
- 2026-10-07 · подтверждён · architect
