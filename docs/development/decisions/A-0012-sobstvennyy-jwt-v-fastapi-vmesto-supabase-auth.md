---
id: A-0012
type: decision
title: Собственный JWT в FastAPI вместо Supabase Auth
status: approved
created: 2026-09-30
updated: 2026-10-01
---

# Собственный JWT в FastAPI вместо Supabase Auth

Принято 2026-07-04. Backend уже был, Postgres локальный, внешних зависимостей хотелось меньше. Аутентификация сделана в FastAPI: пароли — argon2 (pwdlib), токен — HS256 JWT на 30 дней, is_superuser выдаётся только из CLI, восстановление — одноразовый 8-значный код из своей таблицы. Supabase Auth отвергнут — готовые письма и OAuth не перевесили внешнюю зависимость и вторую БД пользователей. Доставка писем, отзыв токенов и rate-limit остаются задачами Ф6 (P6-AUTH-01..02).

## Журнал

- 2026-09-30 · заведена из docs/inbox/decision-own-jwt-auth.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
