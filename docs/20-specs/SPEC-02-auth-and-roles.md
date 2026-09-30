# SPEC-02 — Аккаунт, вход, восстановление, роли

| | |
|---|---|
| **Статус** | `partial` — механика готова; доставка кода и ужесточение под публичный доступ — Ф6 |
| **Требования** | FR-AUTH-01..07, FR-UX-06, NFR-12 |
| **Фаза** | [Ф1](../50-plans/phase-1-mvp.md) · [Ф6](../50-plans/phase-6-product-release.md) |
| **Решения** | [ADR-0007](../40-adr/0007-own-jwt-auth.md) |
| **Обновлено** | 2026-09-30 |

## Назначение

Отделить данные одного учащегося от другого и дать администратору права на курирование канона, без внешнего провайдера авторизации.

## Поведение

1. **Регистрация.** Email и пароль от 6 символов. Сервер создаёт пользователя, выполняет провижининг стартового контента ([SPEC-05](./SPEC-05-srs-and-error-log.md)) и сразу выдаёт токен.
2. **Вход.** Верная пара → токен. На неверную пару один ответ, без уточнения, что именно неверно.
3. **Сессия** — Bearer JWT (HS256, срок из конфига, по умолчанию 30 дней). Клиент хранит его в SecureStore (web — в `localStorage`). На `login`/`register` заголовок `Authorization` не отправляется.
4. **Профиль** — произвольный JSON. Клиент кладёт туда `subject` ([SPEC-12](./SPEC-12-learner-experience.md)).
5. **Восстановление пароля.** Запрос кода гасит прежние невыданные коды и создаёт новый (8 цифр, TTL из конфига). Ответ одинаков для существующего и несуществующего email. Подтверждение проверяет код за постоянное время, считает неверные попытки и после лимита отвечает 429. Пока доставки нет, код читается из БД.
6. **Роль администратора** (`is_superuser`) выдаётся только CLI. Эндпоинты курирования требуют её (`CurrentSuperuser`).
7. **Ошибки сети** клиент отличает от ошибок API: «нет связи» не выдаётся за «неверный пароль».

## Контракт

| Метод | Путь | Вход | Выход | Ошибки |
|---|---|---|---|---|
| POST | `/auth/register` | `{email, password}` | 201 `{access_token, token_type}` | 409 email занят, 422 |
| POST | `/auth/login` | `{email, password}` | `{access_token, token_type}` | 401 |
| GET | `/auth/me` | — | `{id, email, is_superuser, profile}` | 401 |
| PUT | `/auth/me/profile` | `{profile}` | `UserOut` | 401 |
| POST | `/auth/password-reset/request` | `{email}` | 202 `{status, ttl_minutes}` | — |
| POST | `/auth/password-reset/confirm` | `{email, code: /^\d{8}$/, new_password}` | 204 | 400 код неверен/просрочен, 429 лимит попыток |

Данные: `user(id, email unique, password_hash argon2, is_superuser, profile jsonb, created_at)`, `password_reset_code(user_id, code varchar(8), expires_at, used_at, attempts, created_at)`.

Конфиг: `JWT_SECRET`, `ACCESS_TOKEN_EXPIRE_MINUTES`, `PASSWORD_RESET_CODE_TTL_MINUTES` (15), `PASSWORD_RESET_MAX_ATTEMPTS` (5).

## Критерии приёмки

| AC | Критерий | Проверка | Статус |
|---|---|---|---|
| AC-02.1 | Регистрация → 201 и токен; повтор email → 409 | live + test `test_auth.py` | 🟢 |
| AC-02.2 | Неверный пароль → 401 без раскрытия причины | live + test `test_auth.py` | 🟢 |
| AC-02.3 | `sync`, `jobs`, `content`, `graph` без токена → 401/403 | live + test `test_auth.py` | 🟢 |
| AC-02.4 | Запрос кода для несуществующего email → тот же 202 | live + test `test_auth.py` | 🟢 |
| AC-02.5 | Неверный код увеличивает `attempts`; после лимита → 429; верный → 204, старый пароль → 401 | live + test `test_auth.py` | 🟢 |
| AC-02.6 | Восстановление проходит из клиента: запрос → ввод кода → новый пароль | live web | 🟢 |
| AC-02.7 | Код приходит письмом; в БД хранится хеш | live | ⚪ Ф6 |
| AC-02.8 | После смены пароля прежний токен → 401; частые запросы кода → 429 | test | ⚪ Ф6 |

## Код

- Backend: `core/routers/auth.py`, `core/security.py` (argon2 через `pwdlib`, JWT, генерация кода), `core/deps.py` (`CurrentUser`, `CurrentSuperuser`), `core/models.py` (`User`, `PasswordResetCode`), миграции `0002`, `0004`, `0005`; CLI `scripts/createsuperuser.py`.
- Клиент: `src/shared/api/{auth-api,http,token,token.web}.ts` (`ApiError` vs `NetworkError`), `src/entities/session`, `src/pages/auth/ui/{auth-screen,password-reset-screen}.tsx`.

## Расхождения

| Расхождение | Задача |
|---|---|
| Код восстановления хранится открыто (осознанно, до доставки) | [P6-AUTH-02](../50-plans/phase-6-product-release.md) |
| Токен не отзывается после смены пароля | P6-AUTH-02 |

## Открытые вопросы

- Провайдер почты и нужен ли SMS — решается в P6-AUTH-01.
- Refresh-токены: пока одна долгая сессия («для себя»); к публичному релизу — решить в ADR.

## Журнал

| Дата | Изменение |
|---|---|
| 2026-09-30 | Создана из кода и ROADMAP §3.5 |
