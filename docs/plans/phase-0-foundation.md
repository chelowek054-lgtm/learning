# Фаза 0 — Каркас (Foundation)

**Цель фазы:** собрать пустой, но связный и запускаемый скелет всей системы — монорепо, мобильный клиент, backend, схему БД, доменно-независимое ядро и механизм регистрации модулей. По итогам Фазы 0 нет ни одной обучающей фичи, но есть работающий сквозной «пустой» контур: клиент стартует, backend отвечает, БД мигрируется, модуль регистрируется в ядре.

**Не входит в фазу:** любые реальные Activity (эссе, карточки, скоринг), вызовы LLM, sync-логика с данными. Это Фаза 1. Здесь — только каркас и контракты.

**Предпосылки (контекст):**
- Уже есть Expo-scaffold в `learningFront/` (SDK 57, expo-router, RN 0.86, React 19.2, TS 6). ⚠️ Перед любым кодом под Expo читать версионные доки SDK 57 (`AGENTS.md` в проекте: https://docs.expo.dev/versions/v57.0.0/).
- Рабочая директория — `D:\work\learning`, Windows, PowerShell.
- Целевая структура репозитория — [01 — Архитектура, §5](../architecture/01-architecture.md#5-структура-репозитория-монорепо).

---

## Definition of Done фазы

Фаза 0 завершена, когда всё истинно:

1. ✅ `npm install` в корне поднимает workspace; `apps/mobile` стартует (`expo start`) и открывается на устройстве/эмуляторе.
2. ✅ `core-engine`, `module-languages`, `module-ml`, `ui-kit` — собираются как пакеты и импортируются из `apps/mobile`.
3. ✅ Ядро при старте собирает реестр модулей из манифестов; в логах видно зарегистрированные (пустые) типы Activity обоих модулей.
4. ✅ FastAPI поднимается локально, отвечает на `GET /health`, отдаёт OpenAPI-схему.
5. ✅ Миграции применяются к локальному Postgres; все таблицы из [02 — Логический план, §2](../architecture/02-logical.md#2-модель-данных) существуют.
6. ✅ Клиентский SQLite инициализируется и применяет свои миграции при первом запуске.
7. ✅ Инварианты не нарушены: ядро без доменного кода, ключей LLM нигде нет, `.env` в `.gitignore`.

---

## Рабочие потоки (workstreams)

Потоки WS1–WS3 частично параллельны; WS4–WS6 зависят от WS1. Рекомендованный порядок: **WS1 → (WS2 ∥ WS3 ∥ WS4) → WS5 → WS6**.

```
WS1 Монорепо ──┬── WS4 core-engine ── WS5 Модули (манифесты + реестр) ── WS6 Миграция Expo
               ├── WS2 Backend (FastAPI)
               └── WS3 Схема БД (Postgres + Alembic)
```

---

## WS1 — Монорепо и инструментарий

**Итог:** npm-workspace с целевой структурой каталогов и общими конфигами TS/линта.

- [x] `P0-WS1-01` Инициализировать корневой `package.json` (private) с полем `workspaces: ["apps/*", "packages/*"]` (npm workspaces).
- [x] `P0-WS1-02` Создать целевые каталоги: `apps/`, `services/`, `packages/{core-engine,module-languages,module-ml,ui-kit}`.
- [x] `P0-WS1-03` Базовый `tsconfig.base.json` в корне; пакеты наследуют через `extends`. Пути-алиасы (`@praxis/core-engine` и т.д.). Source-first (noEmit).
- [x] `P0-WS1-04` Единый линт/формат (ESLint flat + Prettier) на корне; конфиг общий для всех TS-пакетов.
- [x] `P0-WS1-05` Корневой `.gitignore` (node_modules, `.env`, сборки, `.expo`) и `.env.example`.
- [x] `P0-WS1-06` `README.md` корня: как поднять клиент и backend (ссылки на этот план).

**DoD WS1:** ✅ `npm install` проходит; пакеты видят друг друга по алиасам (typecheck OK); линт/тест/формат — зелёные.

---

## WS2 — Backend-скелет (FastAPI)

**Итог:** запускаемый FastAPI с health-эндпоинтом, структурой `core/` + `modules/`, конфигом окружения. Без бизнес-логики и без вызовов LLM.

- [ ] `P0-WS2-01` `services/api/` — Python-проект на **uv**, Python 3.12+, зависимости: `fastapi`, `uvicorn`, `pydantic-settings`, `sqlalchemy`, `alembic`, `psycopg`.
- [ ] `P0-WS2-02` Структура: `core/` (`app.py`, `config.py`, `db.py`, роутеры-заглушки `sync`, `jobs`, `content`, `auth`) и `modules/{languages,ml}/` (пустые пакеты с `__init__`).
- [ ] `P0-WS2-03` `GET /health` → `{status: ok, version}`; подключить OpenAPI на `/docs`.
- [ ] `P0-WS2-04` Конфиг через `pydantic-settings` из `.env` (DB URL, later: CLAUDE_API_KEY). Ключи **только** из окружения.
- [ ] `P0-WS2-05` Заготовка `ai_gateway/` (интерфейс, без реализации вызова) — чтобы контракт был зафиксирован (см. [02 §6](../architecture/02-logical.md#6-ai-gateway-backend)).
- [ ] `P0-WS2-06` `Dockerfile` + `docker-compose.yml` (api + postgres) для локального запуска.

**DoD WS2:** `docker compose up` (или локальный uvicorn) поднимает API; `GET /health` возвращает ok; `/docs` открывается.

---

## WS3 — Схема БД (Postgres + Alembic)

**Итог:** все таблицы из логического плана созданы миграцией. Данных и логики нет — только структура и связи.

- [ ] `P0-WS3-01` Настроить Alembic в `services/api`; подключение к Postgres из конфига.
- [ ] `P0-WS3-02` SQLAlchemy-модели по [02 §2.1](../architecture/02-logical.md#21-основные-таблицы): `user`, `activity`, `response`, `srs_card`, `job`, `material`, `rubric`.
- [ ] `P0-WS3-03` Ключевые индексы: `srs_card(user_id, due_at)`, `response(user_id, synced)`, `job(user_id, status)`, `activity(user_id, module, type)`.
- [ ] `P0-WS3-04` Первая миграция `0001_init`; применить к локальной БД.
- [ ] `P0-WS3-05` Seed-скрипт (заглушка): один тестовый `user`, по одной пустой `rubric`-строке на модуль (для проверки FK). Без реальных промптов.

**DoD WS3:** `alembic upgrade head` создаёт все таблицы; структура совпадает с [02 §2.1](../architecture/02-logical.md#21-основные-таблицы).

---

## WS4 — core-engine (доменно-независимое ядро)

**Итог:** TS-пакет с типами и интерфейсами ядра, без предметной логики. Реализация методов — заглушки/минимум, важны контракты.

- [ ] `P0-WS4-01` Типы из [02 §1](../architecture/02-logical.md#1-центральная-абстракция-activity): `Activity`, `Connectivity`, `Grade`, `Response`.
- [ ] `P0-WS4-02` Контракты модульной системы из [02 §3.1](../architecture/02-logical.md#31-контракт-манифеста-клиент): `ModuleManifest`, `ActivityTypeDef`, `LocalGrader`, `ImporterDef`, `SchedulerConfig`.
- [ ] `P0-WS4-03` **Реестр модулей**: `registerModule(manifest)`, `getRenderer(type)`, `getActivityTypes()`, `getLocalGrader(type)` — табличный lookup по `type`, **без** `if module === ...`.
- [ ] `P0-WS4-04` Интерфейс локального хранилища (порт) `LocalStore` для SQLite-адаптера — методы для `activity`/`response`/`srs_card`/`job` (сигнатуры, реализация в WS6).
- [ ] `P0-WS4-05` Обёртка FSRS (`ts-fsrs`): интерфейс `Scheduler` (`schedule(card, rating)`, `dueToday()`) — сигнатуры + тонкая реализация поверх ts-fsrs.
- [ ] `P0-WS4-06` Интерфейс `SyncClient` и `JobQueue` (порты) — сигнатуры по [02 §5](../architecture/02-logical.md#5-job-queue-и-синхронизация), без сетевой реализации.
- [ ] `P0-WS4-07` Юнит-тест реестра: регистрируем фиктивный модуль → `getActivityTypes()` его возвращает.

**DoD WS4:** пакет собирается; тест реестра зелёный; **grep по `core-engine` не находит строк `languages`/`ml`/`ielts`** (проверка инварианта доменной независимости).

---

## WS5 — Модули: манифесты и регистрация

**Итог:** `module-languages` и `module-ml` объявляют свои (пока пустые) типы Activity и регистрируются в ядре. Рендереры — заглушки «not implemented».

- [ ] `P0-WS5-01` `module-languages`: манифест с задекларированными типами из [03 §1.1](../architecture/03-functional.md#11-типы-activity) (`ielts_writing_task2`, `vocab_srs`, `reading_drill`, …) — только метаданные (`type`, `connectivity`, `payloadSchema`-заглушка).
- [ ] `P0-WS5-02` `module-ml`: манифест с типами из [03 §2.1](../architecture/03-functional.md#21-типы-activity) (`material_read`, `concept_recall`, `concept_srs`, `code_task`).
- [ ] `P0-WS5-03` Рендереры-заглушки для каждого типа (компонент «Activity type X — not implemented»).
- [ ] `P0-WS5-04` Бэкенд-модули (`services/api/modules/{languages,ml}`): объявить `id` и пустые `rubrics()/generators()` — контракт из [02 §3.2](../architecture/02-logical.md#32-контракт-модуля-backend).
- [ ] `P0-WS5-05` Точка сборки: клиент при старте регистрирует оба модуля в реестре ядра; лог перечисляет зарегистрированные типы.

**DoD WS5:** старт клиента логирует все типы обоих модулей; ядро остаётся без доменных `if`.

---

## WS6 — Миграция Expo в apps/mobile

**Итог:** существующий `learningFront/` переезжает в `apps/mobile/`, подключается к workspace и к `core-engine`/модулям, инициализирует локальный SQLite.

> ⚠️ Читать доки SDK 57 перед изменениями Expo-конфигурации (`AGENTS.md`).

- [ ] `P0-WS6-01` Перенести содержимое `learningFront/` → `apps/mobile/` (сохранить git-историю, если возможно; иначе зафиксировать перенос отдельным коммитом).
- [ ] `P0-WS6-02` Подключить `apps/mobile` к npm-workspace; добавить зависимости на `@praxis/core-engine`, `@praxis/module-*`, `@praxis/ui-kit`.
- [ ] `P0-WS6-03` Добавить `expo-sqlite` + `drizzle-orm`; настроить Drizzle-схему по [02 §2.2](../architecture/02-logical.md#22-локальная-sqlite-vs-серверная-postgres) (локальные таблицы).
- [ ] `P0-WS6-04` Реализовать `LocalStore` (порт из WS4) поверх expo-sqlite; миграции применяются при первом запуске.
- [ ] `P0-WS6-05` Стартовый экран-заглушка: показывает список зарегистрированных типов Activity (визуальное подтверждение, что ядро+модули+БД связаны).
- [ ] `P0-WS6-06` Проверить запуск на iOS и Android (или доступной платформе); зафиксировать результат/скрин.

**DoD WS6:** `expo start` в `apps/mobile` запускает приложение; стартовый экран показывает типы Activity из обоих модулей; SQLite-миграции применены.

---

## Порядок выполнения (предлагаемый)

1. **WS1** — монорепо (разблокирует всё).
2. Параллельно: **WS2** (backend), **WS3** (БД), **WS4** (ядро).
3. **WS5** — модули (нужен WS4).
4. **WS6** — миграция Expo (нужны WS1, WS4, WS5).
5. Прогон **DoD фазы** целиком.

---

## Проверки инвариантов в конце фазы

- [ ] `core-engine` не содержит доменных строк (grep `languages|ml|ielts|toefl` → пусто).
- [ ] Ключей LLM нет в клиенте и в git (`.env` игнорируется; в коде только `process.env`/settings).
- [ ] Нет форка «offline/online приложения» — есть флаг `connectivity` в типах.
- [ ] Единый `response` как event log присутствует в обеих БД (Postgres + SQLite-порт).

---

## Открытые вопросы Фазы 0 (решить по ходу, затем перенести в архитектурные доки)

1. **Auth:** собственный JWT в FastAPI или Supabase Auth. Для Фазы 0 можно оставить `auth`-роутер заглушкой, но выбрать до Фазы 1.
2. ~~**Менеджер Python-окружения:** `uv` vs `poetry`.~~ ✅ Решено: **uv** (доступен в окружении).
3. **Managed Postgres для dev:** локальный Docker-Postgres на Фазе 0; выбор облачного (Supabase/Neon) — к Фазе 1.
4. **Сохранение git-истории** при переносе `learningFront` → `apps/mobile` (WS6-01): проверить, что `learningFront/.git` — отдельный репозиторий, и решить стратегию (subtree/переинициализация монорепо).
