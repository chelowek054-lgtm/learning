---
id: V-0010
type: verification
title: Рубрики на свежей базе
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0004]
---

# Рубрики на свежей базе

Unit, pytest: `cd learningBack && uv run pytest tests/test_modules.py -k rubrics -q`. Доказывает: недостающие рубрики модулей добавляются при старте, существующая версия не перезаписывается. Пройдена, когда тесты проходят и на чистой базе после миграций рубрики появляются без seed.py. Состояние: есть и проходит на 2026-09-30.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-ai-gateway.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
