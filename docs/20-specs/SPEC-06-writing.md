# SPEC-06 — Письмо IELTS Task 2

| | |
|---|---|
| **Статус** | `implemented` (live web + backend live; на устройстве не проверено — NFR-18) |
| **Требования** | FR-WRT-01..03, FR-ENG-05, FR-SRS-03 |
| **Фаза** | [Ф1](../50-plans/phase-1-mvp.md) |
| **Обновлено** | 2026-09-30 |

## Назначение

Проверить главную гипотезу продукта ([scope](../00-product/scope.md#главная-гипотеза)): AI-оценка эссе по официальным критериям с разбором ошибок, которые затем тренируются повторением.

## Поведение

1. Учащийся открывает Activity `ielts_writing_task2`: видит задание (`payload.prompt`) и поле ввода со счётчиком слов.
2. **Отправка работает без сети.** Ответ пишется в `response`, ставится job `grade_writing` с `rubricId='ielts_writing_task2'`.
3. **Черновой сигнал** сразу, офлайн: локальный грейдер оценивает объём (порог 250 слов), структуру абзацев и покрытие AWL. Сигнал помечен `gradedOfflineFallback: true` и не выдаётся за оценку.
4. **При сети** запускается sync; сервер оценивает эссе по рубрике. Разбор содержит 4 критерия с баллами 0–9 и комментариями, `overall` (среднее, округлённое до 0.5), ошибки с исправлением и объяснением, образец переписанных предложений.
5. Ошибки становятся карточками повторения ([SPEC-05](./SPEC-05-srs-and-error-log.md)).

## Контракт

`payload`: `{prompt: string}`. `user_answer`: текст эссе. Job: `{type: 'grade_writing', inputRef: {responseId, rubricId: 'ielts_writing_task2'}}`. `grade` — формат [SPEC-04](./SPEC-04-ai-gateway-and-rubrics.md#контракт).

## Критерии приёмки

| AC | Критерий | Проверка | Статус |
|---|---|---|---|
| AC-06.1 | Эссе отправляется без сети; черновой сигнал показан сразу и помечен черновым | live web | 🟢 |
| AC-06.2 | После sync разбор содержит 4 критерия, `overall`, ошибки, образец | live (RouterAI) | 🟢 |
| AC-06.3 | Ошибки из разбора появились в очереди повторения | live | 🟢 |
| AC-06.4 | Весь сценарий проходит на устройстве в самолётном режиме с последующим включением сети | device | ⚪ [P3-DEV-02](../50-plans/phase-3-hardening.md) |

## Код

- Клиент: `src/features/ielts-writing/ui/ielts-writing-activity.tsx`, `src/features/ielts-writing/lib/local-grader.ts`, `src/shared/ui/grade-view.tsx`, `src/shared/api/grading.ts`.
- Backend: `modules/languages/rubrics.py` (`IELTS_WRITING_TASK2`), `core/jobs.py`.

## Журнал

| Дата | Изменение |
|---|---|
| 2026-09-30 | Создана из 03-functional §1 и плана Ф1 |
