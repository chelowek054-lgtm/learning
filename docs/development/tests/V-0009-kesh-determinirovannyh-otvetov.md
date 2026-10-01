---
id: V-0009
type: verification
title: Кэш детерминированных ответов
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0004]
---

# Кэш детерминированных ответов

Unit, pytest: `cd learningBack && uv run pytest tests/test_llm_cache.py -q`. Доказывает: кэш включается только явным cache=True; ключ зависит от модели, инструмента, схемы и промпта; сбой кэша — промах, а не ошибка. Пройдена, когда все тесты проходят. Состояние: есть и проходит на 2026-09-30.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-ai-gateway.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
