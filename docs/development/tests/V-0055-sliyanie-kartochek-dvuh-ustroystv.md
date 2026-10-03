---
id: V-0055
type: verification
title: Слияние карточек двух устройств
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
command: 'cd learningBack && uv run pytest tests/test_srs_merge.py -q && cd ../learningFront && npx vitest run src/shared/engine/scheduler/card-merge.test.ts src/shared/api/sync-service.test.ts'
links:
  verifies: [R-0019, T-0029]
---

# Слияние карточек двух устройств

Unit, pytest: `будет: cd learningBack && uv run pytest tests/test_srs_merge.py -q`. Доказывает: повторения на двух устройствах сходятся без отката интервалов — побеждает последнее ревью, а не время записи; response конфликтов не даёт. Пройдена, когда тест написан вместе с T-0029. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-multi-device.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-03 · подключена команда прогона: test_srs_merge (последнее ревью, повторы и провалы, идемпотентность, порядок записи не откатывает интервалы, победившая версия приходит на pull, ответы без конфликтов) и клиентские card-merge/sync-service; два реальных устройства не проверялись · claude
