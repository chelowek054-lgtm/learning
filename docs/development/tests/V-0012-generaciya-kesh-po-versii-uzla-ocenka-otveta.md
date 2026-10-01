---
id: V-0012
type: verification
title: Генерация, кэш по версии узла, оценка ответа
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0005]
---

# Генерация, кэш по версии узла, оценка ответа

Unit, pytest: `cd learningBack && uv run pytest tests/test_assessment.py tests/test_assessment_cache.py -q`. Доказывает: промпт содержит теорию узла, узел-ярлык даёт 409, кэш ключуется по версии узла и инвалидируется правкой, закрытый ответ оценивается без LLM. Пройдена, когда все тесты проходят. Состояние: есть и проходит на 2026-09-30.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-assessment.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
