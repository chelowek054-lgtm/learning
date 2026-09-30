# Фаза 1 — MVP

| | |
|---|---|
| **Статус** | 🟡 закрыта по коду 2026-07-04 · 31/33 · две задачи переоткрыты при сверке 2026-09-30 → Ф3 |
| **Цель** | Вертикальный срез главной гипотезы ([scope](../00-product/scope.md#главная-гипотеза)): AI-оценка письма + error-log + SRS, и универсальность движка (тот же движок тянет ML). Всё offline-first |
| **Выход** | регистрация → онбординг → эссе офлайн → черновой сигнал → sync → оценка → ошибки в SRS → повторение; ML: материал → вспомнить → проверка → SRS |
| **Спеки** | [SPEC-02](../20-specs/SPEC-02-auth-and-roles.md), [SPEC-03](../20-specs/SPEC-03-sync-and-jobs.md), [SPEC-04](../20-specs/SPEC-04-ai-gateway-and-rubrics.md), [SPEC-05](../20-specs/SPEC-05-srs-and-error-log.md), [SPEC-06](../20-specs/SPEC-06-writing.md), [SPEC-07](../20-specs/SPEC-07-ml-track.md), [SPEC-12](../20-specs/SPEC-12-learner-experience.md) |
| **Решения** | ADR-0004, 0007, 0009, 0014 |
| **Подробные доказательства** | [archive/phase-1-mvp.md](./archive/phase-1-mvp.md) |

## Потоки

```
Фундамент:  WS1 Auth ──► WS2 Sync + Jobs ──► WS3 AI-gateway ──► WS4 Рубрики и генераторы
Фичи:       WS5 Writing · WS6 Vocab SRS · WS7 ML-трек · WS8 Онбординг + Home
```

### WS1 — Аутентификация (собственный JWT)

| ID | Задача | Трассировка | Статус | Проверка |
|---|---|---|---|---|
| P1-WS1-01 | Миграция `0002`: `password_hash` (argon2) | FR-AUTH-01, NFR-12 | 🟢 | live |
| P1-WS1-02 | `/auth/register`, `/auth/login`, `get_current_user` | FR-AUTH-01..02, AC-02.1..2 | 🟢 | live |
| P1-WS1-03 | Защита `sync`/`jobs`/`content` | AC-02.3 | 🟢 | live |
| P1-WS1-04 | Клиент: SecureStore, http-клиент с Bearer, `entities/session` | FR-AUTH-02 | 🟢 | live web |
| P1-WS1-05 | Экраны `pages/auth`, route-guard | FR-AUTH-01..02 | 🟢 | live web |

### WS2 — Sync + очередь задач

| ID | Задача | Трассировка | Статус | Проверка |
|---|---|---|---|---|
| P1-WS2-01 | `POST /sync/push` + `GET /sync/pull`: per-user, LWW, идемпотентность по `id` | FR-SYNC-02, AC-03.2 | 🟡 | live. **Переоткрыта:** сервер принимает `srsCards`, но клиент их не шлёт — прогресс FSRS не уходит наверх → [P3-SYNC-02](./phase-3-hardening.md) |
| P1-WS2-02 | Персист jobs, переходы `pending → running → done/failed` | FR-SYNC-03 | 🟢 | live |
| P1-WS2-03 | Клиент: `SyncClient` (HTTP) и `JobQueue` (SQLite) | FR-SYNC-02..03 | 🟢 | build + live web |
| P1-WS2-04 | Детекция сети, триггеры sync, применение pull | FR-SYNC-04 | 🟢 | live web. Авто-триггер на появление сети не сделан → P3-SYNC-01 |

### WS3 — AI-gateway

| ID | Задача | Трассировка | Статус | Проверка |
|---|---|---|---|---|
| P1-WS3-01 | `AIGateway.grade` со structured output (tool-use по схеме), модель per-rubric | FR-AI-01, FR-AI-03 | 🟢 | live (с 2026-08-25 — `OpenAICompatibleGateway`, ADR-0009) |
| P1-WS3-02 | Реестр рубрик из БД; рендер промпта | FR-AI-04 | 🟢 | live |
| P1-WS3-03 | Валидация результата в `Grade`; **учёт токенов per-user/type; кэш генерации по хэшу входа** | FR-AI-03, FR-AI-05, FR-AI-06 | 🟡 | **Переоткрыта при сверке:** валидация есть, учёта токенов и кэша в коде нет → [P3-AI-02](./phase-3-hardening.md), [P3-AI-03](./phase-3-hardening.md) |
| P1-WS3-04 | `MockAIGateway` за тем же интерфейсом; выбор реализации по ключу | FR-AI-02, AC-04.1 | 🟢 | test |

### WS4 — Рубрики и генераторы

| ID | Задача | Трассировка | Статус | Проверка |
|---|---|---|---|---|
| P1-WS4-01 | Рубрика `ielts_writing_task2` v1 | FR-WRT-03 | 🟢 | live |
| P1-WS4-02 | Рубрика `concept_check` v1 | FR-ML-02 | 🟢 | live |
| P1-WS4-03 | Генераторы: AWL, `grade.errors → srs_card`, `concept_recall` из материала | FR-SRS-03 | 🟢 | live (генератор из материала не вызывается → P5-IMP-04) |
| P1-WS4-04 | Seed демо-контента | FR-AI-04 | 🟢 | live (рубрики только через ручной seed → P3-AI-01) |

### WS5 — Writing `ielts_writing_task2`

| ID | Задача | Трассировка | Статус | Проверка |
|---|---|---|---|---|
| P1-WS5-01 | Редактор эссе со счётчиком слов | FR-WRT-01 | 🟢 | live web |
| P1-WS5-02 | Офлайн-грейдер: объём, абзацы, AWL | FR-WRT-02, FR-ENG-05 | 🟢 | live web |
| P1-WS5-03 | Submit → `appendResponse` + `enqueueJob(grade_writing)` офлайн | FR-SYNC-01, AC-06.1 | 🟢 | live web |
| P1-WS5-04 | Экран разбора: 4 критерия, ошибки, образец | FR-WRT-03, AC-06.2 | 🟢 | live |
| P1-WS5-05 | Error-log → карточки | FR-SRS-03, AC-06.3 | 🟢 | live |

### WS6 — Vocab SRS

| ID | Задача | Трассировка | Статус | Проверка |
|---|---|---|---|---|
| P1-WS6-01 | Карточка front/back + again/hard/good/easy | FR-SRS-01 | 🟢 | live web |
| P1-WS6-02 | `Scheduler.review` → `fsrs_state` + `due_at` в LocalStore | FR-SRS-01, AC-05.1 | 🟢 | live web |
| P1-WS6-03 | Очередь «на сегодня» из `listDueSrsCards` | FR-SRS-02 | 🟢 | live web |
| P1-WS6-04 | Колода из error-log и AWL | FR-SRS-03 | 🟢 | live (AWL выдаётся всем → P3-INV-02) |

### WS7 — ML-трек

| ID | Задача | Трассировка | Статус | Проверка |
|---|---|---|---|---|
| P1-WS7-01 | `material-read` | FR-ML-01 | 🟢 | live web |
| P1-WS7-02 | `concept-recall` → `enqueueJob(grade_concept)` | FR-ML-02 | 🟢 | live web |
| P1-WS7-03 | Разбор проверки; ошибки → SRS | FR-ML-02 | 🟢 | live |

### WS8 — Онбординг, Home, навигация

| ID | Задача | Трассировка | Статус | Проверка |
|---|---|---|---|---|
| P1-WS8-01 | Онбординг: выбор целей → профиль | FR-UX-01, FR-AUTH-03 | 🟢 | live web. Анкета IELTS+ML заменена выбором предмета (P2-X-06) |
| P1-WS8-02 | Home = «на сегодня»: due-SRS + активности | FR-UX-02 | 🟢 | live web. Заменено одним действием (P2-X-06) |
| P1-WS8-03 | Навигация (табы), route-guard | FR-UX-02 | 🟢 | live web |
| P1-WS8-04 | Простой адаптивный план: слабейший критерий → фокус | FR-UX-02 | 🟢 | build. Поглощён курсом Ф2 |

## Проверки конца фазы

| Проверка | Итог |
|---|---|
| Сквозной сценарий Writing (офлайн → sync → оценка → SRS) | 🟢 live web + backend; ⚪ device → P3-DEV-02 |
| ML-трек | 🟢 live web; ⚪ device → P3-DEV-02 |
| Повторный sync идемпотентен | 🟢 live |
| Инварианты: ключ не в клиенте; ядро клиента без доменных строк; единый лог | 🟢. Ядро backend не проверялось → нарушение найдено 2026-09-30 → P3-INV-01 |
