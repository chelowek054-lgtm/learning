---
id: V-0066
type: verification
title: Error-log, колода по предмету, карточки узла
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0024, T-0004, T-0026, T-0045]
---

# Error-log, колода по предмету, карточки узла

Unit, pytest: `cd learningBack && uv run pytest tests/test_sync.py tests/test_modules.py tests/test_study.py -q`. Доказывает: ошибки оценки становятся карточками, AWL получает только языковой предмет, слабый ответ создаёт карточку узла один раз. Пройдена, когда все тесты проходят. Состояние: есть и проходит на 2026-09-30.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-srs-and-error-log.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
