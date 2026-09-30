# SPEC-03 — Offline-first, синхронизация, очередь задач

| | |
|---|---|
| **Статус** | `partial` — push/pull и очередь работают; прогресс FSRS не уходит наверх, нет авто-триггера, `since` и повторов |
| **Требования** | FR-SYNC-01..06, FR-SYNC-08, NFR-01, NFR-05 |
| **Фаза** | [Ф1](../50-plans/phase-1-mvp.md) · [Ф3](../50-plans/phase-3-hardening.md) |
| **Решения** | [ADR-0004](../40-adr/0004-offline-first-local-source-of-truth.md), [ADR-0005](../40-adr/0005-raw-expo-sqlite.md), [ADR-0014](../40-adr/0014-jobs-processed-on-push.md) |
| **Обновлено** | 2026-09-30 |

## Назначение

Сделать так, чтобы всё, что человек *делает*, работало без сети, а всё, что требует LLM, выполнялось при её появлении без потерь и дублей ([vision](../00-product/vision.md#две-ортогональные-оси)).

## Поведение

1. **Локальная запись.** Ответы на offline-типы, повторения и постановка AI-задач пишутся в SQLite (`LocalStore`). Сеть для этого не нужна.
2. **Очередь.** Feature, которой нужна AI-оценка, пишет `response` и ставит `job {id (UUID клиента), type, inputRef: {responseId, rubricId}}` со статусом `pending`.
3. **Sync** — две фазы:
   - **Push.** Клиент отправляет `activities`, несинхронизированные `responses`, `pending`-jobs и изменённые `srsCards`. Сервер принудительно проставляет `user_id` из токена, делает upsert по `id` (LWW) и возвращает `ackIds`. Клиент помечает подтверждённые ответы `synced`.
   - **Обработка.** Сервер исполняет `pending`-jobs пользователя синхронно в том же запросе ([ADR-0014](../40-adr/0014-jobs-processed-on-push.md)): оценка → `response.grade` → карточки error-log → `job.status='done'`.
   - **Pull.** Клиент забирает активности, ответы, `done`-jobs и карточки. Карточки применяются **только вставкой**: pull не затирает локальный прогресс FSRS.
4. **Триггеры sync:** открытие «Сегодня», отправка ответа на оценку, ручная кнопка в профиле; **цель** — ещё и переход offline → online и возврат приложения из фона.
5. **Сбой задачи.** Сейчас любая ошибка сразу даёт `failed` с причиной в `result.error`. **Цель:** повтор с отсрочкой до лимита попыток, затем `failed`.
6. **Конфликты.** Один активный девайс, LWW на уровне записи. `response` иммутабелен, кроме дописывания `grade`.

## Контракт

| Метод | Путь | Вход | Выход |
|---|---|---|---|
| POST | `/sync/push` | `{activities[], responses[], jobs[], srsCards[]}` (camelCase) | `{ackIds[]}` |
| GET | `/sync/pull` | *(цель: `?since=ISO-8601`)* | `{activities[], responses[], jobs[] (только done), srsCards[]}` |
| GET | `/jobs` | — | все jobs пользователя |
| POST | `/jobs/process` | — | обработать `pending` вручную (отладка) |

Типы jobs: `grade_writing` (рубрика `ielts_writing_task2`), `grade_concept` (рубрика `concept_check`). Ф4 добавит `transcribe`, `grade_speaking`, `explain_distractors`.

Локальные таблицы SQLite: `activity`, `response`, `srs_card`, `job` (схема повторяет серверную, JSON-поля — TEXT).

## Критерии приёмки

| AC | Критерий | Проверка | Статус |
|---|---|---|---|
| AC-03.1 | Эссе, написанное офлайн, лежит в локальном `response` и `job pending` | live web (офлайн-режим браузера) | 🟢 |
| AC-03.2 | Повторный push тех же записей не создаёт дублей | live | 🟢 |
| AC-03.3 | После push с сетью эссе оценено, ошибки стали карточками, pull приносит их на клиент | live | 🟢 |
| AC-03.4 | Pull не затирает локальный прогресс карточки | test/ревью `sync-service.ts` (insert-only) | 🟢 |
| AC-03.5 | Прогресс повторений уходит на сервер; после переустановки интервалы восстанавливаются | live | ⚪ |
| AC-03.6 | Переход offline → online запускает sync сам | device | ⚪ |
| AC-03.7 | `pull?since=` отдаёт только изменения новее `since` | test | ⚪ |
| AC-03.8 | Временный сбой LLM не даёт `failed` с первой попытки; после лимита — `failed` с причиной | test | ⚪ |
| AC-03.9 | Весь сценарий AC-03.1..3 проходит на устройстве в самолётном режиме | device | ⚪ |

## Код

- Backend: `core/routers/sync.py`, `core/routers/jobs.py`, `core/jobs.py` (`process_job`), `core/schemas.py` (`*IO`, camelCase-алиасы).
- Клиент: порты `src/shared/engine/ports/{local-store,sync,jobs}.ts`; реализация `src/shared/api/db/sqlite-local-store.ts` (+ `.web.ts` in-memory), `sync-client.ts`, `sync-service.ts` (`syncNow`), `job-queue.ts`, `grading.ts` (`submitForGrading`), `src/shared/lib/connectivity.ts`.

## Расхождения

| Расхождение | Задача |
|---|---|
| `syncNow` отправляет `srsCards: []` — прогресс FSRS не синхронизируется | [P3-SYNC-02](../50-plans/phase-3-hardening.md) |
| Нет триггера на появление сети и возврат из фона | P3-SYNC-01 |
| Push каждый раз отправляет **все** локальные активности | P3-SYNC-03 |
| `pull` отдаёт всё, параметр `since` в порту есть, на сервере нет | P3-SYNC-03 |
| Ошибка обработки сразу даёт `failed`, повторов нет | P3-SYNC-04 |
| Имена модулей в `core/jobs.py` | P3-INV-01 |
| Web-реализация `LocalStore` — in-memory: после перезагрузки вкладки данные теряются | принято ([ADR-0005](../40-adr/0005-raw-expo-sqlite.md)); web — инструмент разработки |

## Открытые вопросы

- Когда синхронная обработка jobs на push перестанет укладываться в таймаут запроса (Speaking, генерация), нужен фоновой воркер. Решение — ADR перед [Ф4](../50-plans/phase-4-speech-reception.md) (P4-WS2-03).

## Журнал

| Дата | Изменение |
|---|---|
| 2026-09-30 | Создана из 02-logical §5 и кода; найдено: прогресс FSRS не уходит наверх |
