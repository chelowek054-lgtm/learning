# SPEC-05 — Интервальное повторение и error-log

| | |
|---|---|
| **Статус** | `partial` — FSRS и error-log работают; колода не зависит от предмета, типы SRS разошлись |
| **Требования** | FR-SRS-01..06, NFR-01, NFR-04, NFR-08 |
| **Фаза** | [Ф1](../50-plans/phase-1-mvp.md) · [Ф3](../50-plans/phase-3-hardening.md) |
| **Решения** | [ADR-0015](../40-adr/0015-srs-is-a-card-queue.md) (proposed) |
| **Обновлено** | 2026-09-30 |

## Назначение

Удерживать факты и понятия интервальным повторением и связать его с продукцией: ошибки становятся карточками ([vision](../00-product/vision.md#решение)).

## Поведение

1. **Повторение.** Экран повторения берёт карточки с `due_at ≤ now` из локального хранилища. Учащийся видит лицевую сторону, открывает оборот и отвечает again/hard/good/easy. `Scheduler.review` (ts-fsrs) пересчитывает `fsrs_state` и `due_at`. Сеть не нужна.
2. **Источники карточек** (`source`):
   - `awl` — стартовая колода Academic Word List при регистрации;
   - `error_log` — ошибки из `grade.errors` после оценки продукции; слабый ответ на шаге курса;
   - `generated` — карточка удержания узла при старте шага курса;
   - `imported` — зарезервировано для импорта ([SPEC-16](./SPEC-16-learning-expansion.md)).
3. **Error-log.** Каждая ошибка `{kind, excerpt, correction, explanation}` становится карточкой: лицевая сторона «Исправь: «excerpt»», оборот — исправление и объяснение.
4. **Привязка к графу.** Карточка по узлу несёт `concept_id`; одна карточка удержания на узел.
5. **Стартовая колода** (цель): зависит от предмета. AWL получает только тот, у кого предмет языковой. Остальные начинают с пустой колоды, которую наполняют курс и error-log.

## Контракт

`srs_card(id, user_id, module, front jsonb, back jsonb, source, concept_id null, fsrs_state jsonb, due_at, created_at)`. Индексы `(user_id, due_at)`, `(user_id, concept_id)`.

`fsrs_state` — формат ts-fsrs: `{due, stability, difficulty, elapsed_days, scheduled_days, reps, lapses, state}`. Backend создаёт пустое состояние (`state=0`, New), клиент оживляет `due` в `Date` при первом ревью.

## Критерии приёмки

| AC | Критерий | Проверка | Статус |
|---|---|---|---|
| AC-05.1 | Ответ на карточку меняет `fsrs_state` и `due_at` без сети | build + live web | 🟢 |
| AC-05.2 | Очередь «сегодня» = карточки с `due_at ≤ now` | test/ревью `listDueSrsCards` | 🟢 |
| AC-05.3 | Оценка эссе с N ошибками создаёт N карточек `error_log` | live | 🟢 |
| AC-05.4 | Слабый ответ на шаге курса создаёт карточку с `concept_id` | test `test_study.py` | 🟢 |
| AC-05.5 | Учащийся с неязыковым предметом не получает AWL | test | ⚪ |
| AC-05.6 | Тип повторения, который отдаёт шаг курса, объявлен в реестре и имеет обработку на клиенте | test реестра + live | ⚪ |
| AC-05.7 | Планирование карточки < 16 мс на устройстве | device | ⚪ |

## Код

- Клиент: `src/shared/engine/scheduler/scheduler.ts`, `src/pages/review/ui/review-screen.tsx`, порт `LocalStore.listDueSrsCards/upsertSrsCard`.
- Backend: `core/srs.py` (`initial_fsrs_state`, `errors_to_card_partials`, `insert_cards`), `core/provisioning.py`, `modules/languages/generators.py` (`AWL_STARTER`, 10 слов), `modules/knowledge/study.py` (`_ensure_card`), миграция `0007_srs_concept_link`.

## Расхождения

| Расхождение | Задача |
|---|---|
| AWL выдаётся всем при регистрации, независимо от предмета; предмета при регистрации ещё нет | [P3-INV-02](../50-plans/phase-3-hardening.md) |
| Три типа повторения: `vocab_srs` (languages), `concept_srs` (ml), `srs` (knowledge, отдаёт шаг курса). Ни у одного нет рендерера Activity; повторение идёт экраном карточек | P3-SRS-01 (ADR-0015) |
| Прогресс FSRS не синхронизируется наверх | P3-SYNC-02 ([SPEC-03](./SPEC-03-sync-and-jobs.md)) |
| AWL — демо-выборка из 10 слов | [P5-WRT-03](../50-plans/phase-5-learning-expansion.md) |

## Открытые вопросы

- Оставлять ли SRS типом Activity. Предложение ([ADR-0015](../40-adr/0015-srs-is-a-card-queue.md)): повторение — очередь карточек, а не тип Activity; шаг курса ссылается на карточку узла.

## Журнал

| Дата | Изменение |
|---|---|
| 2026-09-30 | Создана из 02-logical §4, кода и долгов HANDOFF §6 |
