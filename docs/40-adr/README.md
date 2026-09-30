# 40 — Архитектурные решения (ADR)

Здесь записано, **почему** система устроена так, а не иначе. ADR не переписывается задним числом: изменённое решение оформляется новым ADR, а старый получает статус `superseded by`. Шаблон — [`_template.md`](./_template.md).

ADR 0001–0017 восстановлены 2026-09-30 из журнала ROADMAP, HANDOFF и планов фаз. Решения принимались раньше, дата в каждом ADR — дата принятия.

| ADR | Решение | Статус | Затрагивает |
|---|---|---|---|
| [0001](./0001-docdd.md) | Документация — источник правды; изменения идут по DocDD | accepted | всё |
| [0002](./0002-superproject-submodules.md) | Суперпроект с сабмодулями; оркестрация в корне, Dockerfile у сервиса | accepted | SPEC-17 |
| [0003](./0003-client-expo-fsd.md) | Клиент на Expo/React Native по Feature-Sliced Design; ядро в `shared/engine` | accepted | SPEC-01 |
| [0004](./0004-offline-first-local-source-of-truth.md) | Offline-first: локальная БД — источник правды для действий; LWW; один активный девайс | accepted | SPEC-03 |
| [0005](./0005-raw-expo-sqlite.md) | Raw `expo-sqlite` за портом `LocalStore` вместо Drizzle; web — in-memory | accepted | SPEC-03 |
| [0006](./0006-expo-sdk-54.md) | Expo SDK 54 ради совместимости с публичным Expo Go | accepted | NFR-20 |
| [0007](./0007-own-jwt-auth.md) | Собственный JWT в FastAPI вместо Supabase Auth | accepted | SPEC-02 |
| [0008](./0008-uv-python.md) | uv для Python-окружения backend | accepted | — |
| [0009](./0009-llm-provider-as-config.md) | Провайдер LLM задаётся конфигурацией; один OpenAI-совместимый gateway | accepted | SPEC-04 |
| [0010](./0010-single-root-env.md) | Один `.env` в корне суперпроекта для всех сервисов | accepted | NFR-16 |
| [0011](./0011-knowledge-as-module-cow.md) | Модель знаний — модуль backend, не ядро; канон + персональный слой copy-on-write | accepted | SPEC-08 |
| [0012](./0012-mastery-beta-not-irt.md) | Освоенность — бета-модель с приором из предпосылок, не IRT | accepted | SPEC-10 |
| [0013](./0013-course-as-developmental-simulation.md) | Курс — симуляция развития (4 стадии), а не топосорт | accepted | SPEC-11 |
| [0014](./0014-jobs-processed-on-push.md) | AI-задачи исполняются синхронно на `/sync/push` (до появления воркера) | accepted | SPEC-03 |
| [0015](./0015-srs-is-a-card-queue.md) | Повторение — очередь карточек, а не тип Activity | **proposed** | SPEC-05, SPEC-11 |
| [0016](./0016-empty-domain-built-by-learner.md) | Пустую область строит выбравший предмет; узлы — draft до вычитки | accepted | SPEC-08 |
| [0017](./0017-ui-vocabularies-single-source.md) | Словари интерфейса — единые источники в реестре и `entities`, не в экранах | accepted | SPEC-12 |
| [0018](./0018-phase-renumbering.md) | Перенумерация фаз: укрепление фундамента перед речью | accepted | 50-plans |

## Решения, которые предстоит принять

| Вопрос | Когда | Задача |
|---|---|---|
| Контракт модулей backend и их регистрация | Ф3 | P3-INV-01 |
| Где STT (API / контейнер / on-device), формат аудио | до Ф4 WS2 | P4-WS2-00 |
| Фоновой воркер вместо обработки на push | до Ф4 WS2 | P4-WS2-03 |
| Где TTS | до Ф4 WS6 | P4-WS6-00 |
| Граф для языкового домена | Ф5 | P5-LANG-01 |
| Хостинг и managed Postgres | Ф6 | P6-OPS-01 |
| Стратегия sync для нескольких устройств | Ф6 | P6-SYNC-01 |
