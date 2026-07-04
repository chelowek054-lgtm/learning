# Фаза 0 — Каркас (Foundation)

**Цель фазы:** собрать пустой, но связный и запускаемый скелет всей системы — суперпроект с сабмодулями, клиент по FSD с доменно-независимым ядром и реестром модулей, backend-скелет, схему БД. По итогам нет ни одной обучающей фичи, но есть сквозной «пустой» контур: клиент стартует и показывает зарегистрированные типы Activity, backend отвечает, БД мигрируется.

**Не входит:** реальные Activity (эссе, карточки, скоринг), вызовы LLM, sync с данными. Это Фаза 1.

**Контекст репозитория:**
- Корень `D:\work\learning` — **git-суперпроект** с сабмодулями `learningFront` (клиент) и `learningBack` (backend), каждый — отдельный репозиторий. `docs/` — в суперпроекте.
- Клиент организован по **Feature-Sliced Design** — см. [04 — Фронтенд (FSD)](../architecture/04-frontend-fsd.md). Ядро — в `src/shared/engine`.
- Стек: Expo SDK 57 / RN 0.86 / React 19.2 / TS 6 (клиент); FastAPI + uv (backend). ⚠️ Перед кодом под Expo читать доки SDK 57 (`AGENTS.md`: https://docs.expo.dev/versions/v57.0.0/).
- Инструменты фронта — обычный **npm** (без workspaces).

---

## Definition of Done фазы

1. ✅ `npm install` в `learningFront` проходит; `npx expo start` поднимает приложение.
2. ✅ Ядро (`shared/engine`) типобезопасно, тесты зелёные, доменно-независимо (grep чист).
3. ✅ Клиент при старте регистрирует оба модуля; стартовый экран показывает их типы Activity.
4. ✅ FastAPI (`learningBack`) поднимается, отвечает на `GET /health`, отдаёт OpenAPI.
5. ✅ Миграции применяются к Postgres; все таблицы из [02 §2](../architecture/02-logical.md#2-модель-данных) существуют.
6. ✅ Клиентский SQLite инициализируется и применяет миграции при первом запуске.
7. ✅ Инварианты: ядро без доменного кода, ключей LLM нет в клиенте, `.env` в `.gitignore`.

---

## Рабочие потоки

Порядок: **WS1 → WS4 → (WS5 ∥ WS6)** для фронта; **WS2 ∥ WS3** для бэка (независимы).

```
learningFront:  WS1 Каркас+FSD ── WS4 Ядро(shared/engine) ──┬── WS5 Модули (features + манифесты)
                                                            └── WS6 SQLite LocalStore + стартовый экран
learningBack:   WS2 FastAPI-скелет ── WS3 Схема БД (Alembic)
```

---

## WS1 — Каркас репозитория и фронт-тулинг · ✅ done

**Итог:** суперпроект с сабмодулями; в `learningFront` — FSD-скелет, зависимости и скрипты тулинга.

- [x] `P0-WS1-01` Суперпроект + сабмодули `learningFront`/`learningBack` (`.gitmodules`), `docs/` в суперпроекте.
- [x] `P0-WS1-02` FSD-скелет в `learningFront/src`: `app/`, `pages/`, `widgets/`, `features/`, `entities/`, `shared/{engine,ui,api,config,lib}`.
- [x] `P0-WS1-03` Алиас `@/*` → `src/*` (в `tsconfig.json`); публичный API слоёв через `index.ts`.
- [x] `P0-WS1-04` Тулинг: `ts-fsrs`, `vitest`, `prettier`; скрипты `typecheck`/`test`/`format`; `.prettierrc.json`.
- [x] `P0-WS1-05` `.gitignore` суперпроекта и сабмодулей; `.env.example` в `learningFront` (EXPO_PUBLIC_* без секретов).
- [x] `P0-WS1-06` README суперпроекта и `learningFront/src/README.md` (FSD).

**DoD WS1:** ✅ `npm install` проходит; `typecheck`/`test`/`format` — зелёные.

---

## WS4 — Ядро `shared/engine` (доменно-независимое) · ✅ done

**Итог:** типы, контракты модульной системы, реестр, порты, обёртка FSRS, тесты. Реализация — минимальная, важны контракты.

- [x] `P0-WS4-01` Типы: `Activity`, `Connectivity`, `Grade`, `Response` ([02 §1](../architecture/02-logical.md#1-центральная-абстракция-activity), [§7](../architecture/02-logical.md#7-модель-grade-результат-скоринга)).
- [x] `P0-WS4-02` Контракты: `ModuleManifest`, `ActivityTypeDef`, `ActivityRenderer`, `LocalGrader`, `ImporterDef`, `SchedulerConfig` ([02 §3.1](../architecture/02-logical.md#31-контракт-манифеста-клиент)). Рендерер opaque (`unknown`) — без зависимости ядра от React.
- [x] `P0-WS4-03` `ModuleRegistry` (табличный lookup по `type`, без `if module === ...`): `registerModule`, `getRenderer`, `getActivityTypes`, `getLocalGrader`, `getModuleIdForType`; защита от коллизий.
- [x] `P0-WS4-04` Порт `LocalStore` (+ `SrsCardRecord`, `JobRecord`) для SQLite-адаптера.
- [x] `P0-WS4-05` Обёртка FSRS (`ts-fsrs`): `Scheduler` (`createCard`/`review`/`dueCards`).
- [x] `P0-WS4-06` Порты `SyncClient` и `JobQueue` ([02 §5](../architecture/02-logical.md#5-job-queue-и-синхронизация)).
- [x] `P0-WS4-07` Юнит-тесты реестра и планировщика (vitest).

**DoD WS4:** ✅ типы чисты (0 ошибок tsc); 7/7 тестов зелёные; grep `languages|ml|ielts` по `shared/engine` — пусто.

---

## WS5 — Модули как FSD-слайсы + манифесты · ✅ done

**Итог:** домены `languages`/`ml` объявляют типы Activity. Метаданные держатся ЧИСТЫМИ (только `import type` из ядра — стираются при сборке, тестируются в node), рендереры подключаются в composition root. Backend-модули — самодостаточные заглушки.

- [x] `P0-WS5-01` `src/app/modules/languages.ts`: чистые метаданные `languagesActivityTypes: ActivityTypeDef[]` (6 типов, [03 §1.1](../architecture/03-functional.md#11-типы-activity)).
- [x] `P0-WS5-02` `src/app/modules/ml.ts`: `mlActivityTypes` (4 типа, [03 §2.1](../architecture/03-functional.md#21-типы-activity)).
- [x] `P0-WS5-03` Единый плейсхолдер-рендерер `shared/ui/NotImplementedActivity` (показывает `activity.type`); feature-слайсы на тип — Фаза 1.
- [x] `P0-WS5-04` Backend-заглушки `learningBack/modules/{languages,ml}` (`MODULE_ID`, `ACTIVITY_TYPES`, пустые `rubrics()/generators()`); контракт ModuleBackend — WS2.
- [x] `P0-WS5-05` Composition root `src/app/modules/index.ts`: `initModuleRegistry()` собирает манифесты (метаданные + рендерер), регистрирует, логирует типы. Вызов при старте — в WS6 (стартовый экран).

**DoD WS5:** ✅ метаданные конформны `ModuleManifest` (0 ошибок tsc); тесты метаданных зелёные (12/12 всего); коллизий типов нет; ядро без доменных `if`. Runtime-лог включается в WS6.

---

## WS6 — SQLite LocalStore + стартовый экран · ✅ done

**Итог:** порт `LocalStore` на `expo-sqlite`; схема при старте; стартовый экран показывает зарегистрированные модули/типы, статус SQLite и демо-диспетчеризацию (подтверждение связки ядро+модули+БД).

> ⚠️ Доки SDK 57 прочитаны (expo-sqlite API) перед кодом.

- [x] `P0-WS6-01` `expo-sqlite ~57.0.0`. Схема ([02 §2.2](../architecture/02-logical.md#22-локальная-sqlite-vs-серверная-postgres)) в `shared/api/db` через `CREATE TABLE IF NOT EXISTS`. **Решение:** raw expo-sqlite вместо drizzle-orm в Ф0 (drizzle-миграции требуют codegen + Metro-конфиг под `.sql`, не проверить без устройства; порт `LocalStore` абстрагирует БД).
- [x] `P0-WS6-02` `SqliteLocalStore` реализует порт `LocalStore` поверх sync-API (`runSync`/`getAllSync`); `migrate()` + фабрика `createSqliteLocalStore`. **Web:** платформенная замена `sqlite-local-store.web.ts` (in-memory) — expo-sqlite на web тянет `wa-sqlite.wasm` (COEP/OPFS), избыточно для mobile-first; Metro подхватывает `.web.ts`.
- [x] `P0-WS6-03` Виджет `widgets/activity-dispatcher` (рендер по `activity.type` через реестр; opaque-рендерер приводится к компоненту).
- [x] `P0-WS6-04` Экран `pages/home` (типы + статус БД + демо-диспетчеризация); роут `src/app/index.tsx` — тонкий re-export; провайдер реестра в `_layout` через `app/providers`. Реестр читается из контекста `shared/lib` (pages не импортируют app — правило FSD).
- [x] `P0-WS6-05` Проверка сборки: `expo export --platform android` → **EXIT 0**, Hermes-бандл собран (весь FSD-граф + `@/`-алиасы + expo-sqlite резолвятся/компилируются). ⚠️ Рантайм на устройстве/эмуляторе не прогонялся (недоступен в среде) — остаётся к ручной проверке.

**DoD WS6:** ✅ приложение бандлится (`expo export` EXIT 0); экран показывает типы обоих модулей; SQLite-схема применяется в `migrate()`. Визуальный/рантайм-прогон на устройстве — открытый пункт.

**DoD WS6:** `expo start` запускает приложение; стартовый экран показывает типы обоих модулей; SQLite-миграции применены.

---

## WS2 — Backend-скелет (FastAPI) · learningBack

**Итог:** запускаемый FastAPI с health, структурой `core/` + `modules/`, конфигом окружения. Без бизнес-логики и вызовов LLM.

- [ ] `P0-WS2-01` `learningBack` — Python-проект на **uv**, Python 3.12+: `fastapi`, `uvicorn`, `pydantic-settings`, `sqlalchemy`, `alembic`, `psycopg`.
- [ ] `P0-WS2-02` Структура: `core/` (`app.py`, `config.py`, `db.py`, роутеры-заглушки `sync`/`jobs`/`content`/`auth`) и `modules/{languages,ml}/`.
- [ ] `P0-WS2-03` `GET /health` → `{status: ok, version}`; OpenAPI на `/docs`.
- [ ] `P0-WS2-04` Конфиг через `pydantic-settings` из `.env` (DATABASE_URL, later CLAUDE_API_KEY). Ключи — только из окружения. `.env.example` в `learningBack`.
- [ ] `P0-WS2-05` Заготовка `ai_gateway/` (интерфейс, без вызова) — контракт [02 §6](../architecture/02-logical.md#6-ai-gateway-backend).
- [ ] `P0-WS2-06` `Dockerfile` + `docker-compose.yml` (api + postgres) для локального запуска.

**DoD WS2:** `docker compose up` (или uvicorn) поднимает API; `GET /health` = ok; `/docs` открывается.

---

## WS3 — Схема БД (Postgres + Alembic) · learningBack

**Итог:** все таблицы из логического плана созданы миграцией.

- [ ] `P0-WS3-01` Alembic в `learningBack`; подключение к Postgres из конфига.
- [ ] `P0-WS3-02` SQLAlchemy-модели по [02 §2.1](../architecture/02-logical.md#21-основные-таблицы): `user`, `activity`, `response`, `srs_card`, `job`, `material`, `rubric`.
- [ ] `P0-WS3-03` Индексы: `srs_card(user_id, due_at)`, `response(user_id, synced)`, `job(user_id, status)`, `activity(user_id, module, type)`.
- [ ] `P0-WS3-04` Миграция `0001_init`; применить к локальной БД.
- [ ] `P0-WS3-05` Seed-заглушка: один `user`, по одной пустой `rubric`-строке на модуль (FK).

**DoD WS3:** `alembic upgrade head` создаёт все таблицы по [02 §2.1](../architecture/02-logical.md#21-основные-таблицы).

---

## Проверки инвариантов в конце фазы

- [ ] `shared/engine` без доменных строк (grep `languages|ml|ielts|toefl` → пусто).
- [ ] Ключей LLM нет в клиенте и в git (`.env` игнорируется).
- [ ] Нет форка «offline/online» — есть флаг `connectivity` в типах.
- [ ] Единый `response` как event log в обеих БД (Postgres + SQLite-порт).

---

## Открытые вопросы Фазы 0

1. **Auth:** собственный JWT в FastAPI или Supabase Auth — выбрать до Фазы 1 (в Ф0 `auth`-роутер заглушкой).
2. ~~**Менеджер Python:** uv vs poetry.~~ ✅ **uv**.
3. **Managed Postgres для dev:** локальный Docker-Postgres в Ф0; облачный (Supabase/Neon) — к Ф1.
4. **Границы FSD-импортов:** подключить линтер (`steiger` / `eslint-plugin-boundaries`) — отдельной задачей; на старте grep + ревью.
