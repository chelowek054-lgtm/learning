---
id: V-0138
type: verification
title: Многоязычный граф
status: approved
created: 2026-10-12
updated: 2026-10-12
kind: manual
command: 'cd learningBack && uv run pytest tests/test_v0138_v0139_languages.py -q'
links:
  verifies: [R-0079]
---

# Многоязычный граф

Тест: русский и английский фрагменты об одном понятии сливаются в один узел с двумя ссылками; сборка даёт теорию и задания на обоих языках; смена языка изучения отдаёт готовое без запроса к модели.

## Журнал

- 2026-10-12 · заведена из docs/inbox/mnogoyazychnyy-graf-znaniy.md · приложение
- 2026-10-12 · на подтверждение · architect
- 2026-10-12 · подтверждён · architect
- 2026-10-12 · добавлена команда автоматической проверки (tests/test_v0138_v0139_languages.py): ru и en в одном узле, готовые тексты на языке изучения · claude
