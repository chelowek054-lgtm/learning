---
id: V-0015
type: verification
title: Хеш кода, rate-limit и отзыв сессий
status: approved
created: 2026-09-30
updated: 2026-10-02
kind: manual
command: 'cd learningBack && uv run pytest tests/test_auth.py -k "reset or revokes or rate_limited or token_without_version" -q'
links:
  verifies: [R-0006, T-0002, T-0003]
---

# Хеш кода, rate-limit и отзыв сессий

Unit, pytest: `будет: cd learningBack && uv run pytest tests/test_auth_hardening.py -q`. Доказывает: код восстановления хранится хешем, частый запрос кода даёт 429, после смены пароля прежний токен недействителен. Пройдена, когда тесты написаны вместе с T-0003 и проходят. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-auth.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-02 · подключена команда прогона: test_auth: хеш кода, 429, отзыв сессий (T-0003); доставка кода (T-0002) не покрыта · claude
