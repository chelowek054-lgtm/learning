---
id: V-0069
type: verification
title: Sync, повторы задач, защита чужих записей
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
links:
  verifies: [R-0025, T-0046, T-0047, T-0048, T-0049, T-0050]
---

# Sync, повторы задач, защита чужих записей

Integration, pytest: `cd learningBack && uv run pytest tests/test_sync.py tests/test_job_retry.py -q`. Доказывает: push идемпотентен и не принимает чужие id; задача оценивается и даёт карточки; временный сбой повторяется с отсрочкой, постоянный — failed с причиной; LWW карточек не принимает более старую версию. Пройдена, когда все тесты проходят (проверяет и T-0047). Состояние: есть и проходит на 2026-09-30.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-sync-and-jobs.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
