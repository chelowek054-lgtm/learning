---
id: V-0007
type: verification
title: 'Транспорт к провайдеру: повторы, max_tokens, бюджет'
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0004]
---

# Транспорт к провайдеру: повторы, max_tokens, бюджет

Unit, pytest: `cd learningBack && uv run pytest tests/test_openai_gateway.py -q`. Доказывает: обрыв канала, 402 с подстройкой бюджета и ответ текстом вместо вызова инструмента повторяются; max_tokens есть в каждом запросе. Пройдена, когда все тесты проходят. Состояние: есть и проходит на 2026-09-30.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-ai-gateway.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
