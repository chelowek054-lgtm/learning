---
id: V-0034
type: verification
title: Версия API и совместимость клиента
status: approved
created: 2026-09-30
updated: 2026-10-02
kind: manual
command: 'cd learningBack && uv run pytest tests/test_versioning.py -q'
links:
  verifies: [R-0020, T-0030, T-0031, T-0032, T-0033, T-0034]
---

# Версия API и совместимость клиента

Unit, pytest: `будет: cd learningBack && uv run pytest tests/test_api_version.py -q`. Доказывает: пути под /v1, несовместимый клиент получает понятное сообщение об обновлении. Пройдена, когда тест написан вместе с T-0033. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-deploy-and-release.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-02 · подключена команда прогона: test_versioning (T-0033) · claude
