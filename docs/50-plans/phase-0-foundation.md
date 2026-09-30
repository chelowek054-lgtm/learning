# Фаза 0 — Каркас

| | |
|---|---|
| **Статус** | ✅ закрыта 2026-07-04 · 34/34 |
| **Цель** | Пустой, но связный и запускаемый скелет: суперпроект, FSD-клиент, доменно-независимое ядро, FastAPI + Postgres, оркестрация |
| **Выход** | Клиент стартует и показывает зарегистрированные типы Activity; backend отвечает; БД мигрируется |
| **Спеки** | [SPEC-01](../20-specs/SPEC-01-activity-engine.md), [SPEC-03](../20-specs/SPEC-03-sync-and-jobs.md) (порты), [SPEC-17](../20-specs/SPEC-17-platform-and-release.md) (стенд) |
| **Решения** | ADR-0002…0008 |
| **Подробные доказательства** | [archive/phase-0-foundation.md](./archive/phase-0-foundation.md) |

## Потоки

```
WS1 Репозиторий и тулинг ──► WS4 Ядро ──► WS5 Модули ──► WS6 LocalStore + экран
WS2 Backend-скелет ──► WS3 Схема БД
```

### WS1 — Репозиторий и фронт-тулинг

| ID | Задача | Трассировка | Статус | Проверка |
|---|---|---|---|---|
| P0-WS1-01 | Суперпроект + сабмодули `learningFront`/`learningBack`; `docs/` в суперпроекте | ADR-0002 | 🟢 | live |
| P0-WS1-02 | FSD-скелет `src/{app,pages,widgets,features,entities,shared}` | NFR-14, ADR-0003 | 🟢 | build |
| P0-WS1-03 | Алиас `@/*` → `src/*`; публичный API слоёв через `index.ts` | NFR-14 | 🟢 | build |
| P0-WS1-04 | Тулинг: `ts-fsrs`, `vitest`, `prettier`; скрипты `typecheck`/`test`/`format` | NFR-13 | 🟢 | build |
| P0-WS1-05 | `.gitignore`; окружение без секретов | NFR-02 | 🟢 | ревью (позже сведено к корневому `.env`, ADR-0010) |
| P0-WS1-06 | README суперпроекта и `learningFront/src/README.md` | NFR-19 | 🟢 | ревью |

### WS4 — Ядро `shared/engine`

| ID | Задача | Трассировка | Статус | Проверка |
|---|---|---|---|---|
| P0-WS4-01 | Типы `Activity`, `Connectivity`, `Grade`, `Response` | FR-ENG-01, NFR-05 | 🟢 | build |
| P0-WS4-02 | Контракты `ModuleManifest`, `ActivityTypeDef`, `ActivityRenderer`, `LocalGrader`, `ImporterDef`, `SchedulerConfig` | FR-ENG-02, FR-ENG-05 | 🟢 | build |
| P0-WS4-03 | `ModuleRegistry`: табличный lookup по `type`, защита от коллизий | FR-ENG-02, SPEC-01 AC-01.1..3 | 🟢 | test |
| P0-WS4-04 | Порт `LocalStore` (+ `SrsCardRecord`, `JobRecord`) | FR-SYNC-01 | 🟢 | build |
| P0-WS4-05 | Обёртка FSRS `Scheduler` | FR-SRS-01 | 🟢 | test |
| P0-WS4-06 | Порты `SyncClient` и `JobQueue` | FR-SYNC-02, FR-SYNC-03 | 🟢 | build |
| P0-WS4-07 | Юнит-тесты реестра и планировщика | NFR-13 | 🟢 | test |

### WS5 — Модули как FSD-слайсы

| ID | Задача | Трассировка | Статус | Проверка |
|---|---|---|---|---|
| P0-WS5-01 | Метаданные модуля `languages` (6 типов) | FR-ENG-02 | 🟢 | test (сейчас в `entities/module/languages.ts`) |
| P0-WS5-02 | Метаданные модуля `ml` (4 типа) | FR-ENG-02 | 🟢 | test |
| P0-WS5-03 | Плейсхолдер-рендерер `NotImplementedActivity` | FR-ENG-04, AC-01.4 | 🟢 | build |
| P0-WS5-04 | Backend-заглушки `modules/{languages,ml}` | FR-ENG-06 | 🟢 | live |
| P0-WS5-05 | Composition root: `initModuleRegistry()` собирает и регистрирует манифесты | FR-ENG-02 | 🟢 | build (сейчас в `widgets/module-registry`) |

### WS6 — SQLite LocalStore и стартовый экран

| ID | Задача | Трассировка | Статус | Проверка |
|---|---|---|---|---|
| P0-WS6-01 | Схема SQLite в `shared/api/db` (`CREATE TABLE IF NOT EXISTS`) | FR-SYNC-01, ADR-0005 | 🟢 | build |
| P0-WS6-02 | `SqliteLocalStore` + web-замена in-memory | FR-SYNC-01, ADR-0005 | 🟢 | build |
| P0-WS6-03 | Виджет `activity-dispatcher` | FR-ENG-01 | 🟢 | build |
| P0-WS6-04 | Экран `pages/home`; тонкий роут; провайдер реестра | FR-ENG-02 | 🟢 | build |
| P0-WS6-05 | `expo export --platform android` → EXIT 0 | NFR-18 (частично) | 🟢 | build. ⚠️ Рантайм на устройстве не проверялся → P3-DEV-01 |

### WS2 — Backend-скелет

| ID | Задача | Трассировка | Статус | Проверка |
|---|---|---|---|---|
| P0-WS2-01 | Проект на uv (Python 3.12), зависимости, `uv.lock` | ADR-0008 | 🟢 | live |
| P0-WS2-02 | Структура `core/` + `modules/` | FR-ENG-06 | 🟢 | live |
| P0-WS2-03 | `GET /health`, OpenAPI | SPEC-17 | 🟢 | live |
| P0-WS2-04 | Конфиг `pydantic-settings`; ключи только из окружения | NFR-02 | 🟢 | live |
| P0-WS2-05 | Протокол `AIGateway` | FR-AI-01 | 🟢 | build |
| P0-WS2-06 | Dockerfile в сабмодуле; корневой `docker-compose.yml` | ADR-0002 | 🟢 | live `docker compose up` |

### WS3 — Схема БД

| ID | Задача | Трассировка | Статус | Проверка |
|---|---|---|---|---|
| P0-WS3-01 | Alembic, URL из настроек | — | 🟢 | live |
| P0-WS3-02 | Модели `user`, `activity`, `response`, `srs_card`, `job`, `material`, `rubric` | FR-ENG-01, NFR-04 | 🟢 | live |
| P0-WS3-03 | Индексы `srs_card(user_id, due_at)`, `response(user_id, synced)`, `job(user_id, status)`, `activity(user_id, module, type)` | FR-SRS-02 | 🟢 | live |
| P0-WS3-04 | Миграция `0001_init` | — | 🟢 | live `alembic upgrade head` |
| P0-WS3-05 | Seed-заглушка `scripts/seed.py` | FR-AI-04 | 🟢 | live |

## Проверки инвариантов фазы

| Проверка | Итог |
|---|---|
| `shared/engine` без доменных строк | 🟢 grep пуст |
| Ключей LLM нет в клиенте и git | 🟢 |
| Connectivity — флаг в типах, нет форка | 🟢 |
| Единый `response` в обеих БД | 🟢 |

## Итоги и долги

- Решения фазы: uv, raw `expo-sqlite`, оркестрация в корне, Expo SDK 54 (ADR-0005, 0006, 0008, 0002).
- **Долг:** рантайм клиента на устройстве не проверен. Он тянулся через Ф1 и Ф2 и закрывается в Ф3 (P3-DEV-01..04).
