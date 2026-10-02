---
id: V-0071
type: verification
title: Инкрементальный pull
status: approved
created: 2026-09-30
updated: 2026-10-02
kind: manual
command: 'cd learningBack && uv run pytest tests/test_sync.py -k "since" -q && cd ../learningFront && npx vitest run src/shared/api/sync-service.test.ts'
links:
  verifies: [R-0025, T-0046, T-0047, T-0048, T-0049, T-0050]
---

# Инкрементальный pull

Unit, pytest: `будет: cd learningBack && uv run pytest tests/test_sync_since.py -q`. Доказывает: GET /sync/pull?since= отдаёт только изменения новее since; push не шлёт неизменённое. Пройдена, когда тест написан вместе с T-0048. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-sync-and-jobs.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-02 · подключена команда прогона: test_sync и sync-service.test: инкрементальный pull (T-0048) · claude
