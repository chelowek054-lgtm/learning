# SPEC-07 — ML-трек: материал и вспоминание понятия

| | |
|---|---|
| **Статус** | `implemented` (live web + backend live) |
| **Требования** | FR-ML-01..02 |
| **Фаза** | [Ф1](../50-plans/phase-1-mvp.md) |
| **Обновлено** | 2026-09-30 |

## Назначение

Доказать вторичную гипотезу: тот же движок Activity без изменений обслуживает технический предмет. Цикл: *прочитал → вспомнил своими словами → получил проверку → слабое ушло в повторение*.

## Поведение

1. `material_read` (offline): учащийся читает текст материала. Материал приходит с сервера (`/content/materials` или `payload` активности) и доступен без сети.
2. `concept_recall` (online, с очередью): учащийся отвечает на вопрос о понятии своими словами. Ответ сохраняется офлайн, ставится job `grade_concept` с рубрикой `concept_check`.
3. При сети ответ оценивается по трём критериям (0–5): Correctness, Completeness, Explanation. Неточности становятся карточками повторения.

Со времени Фазы 2 основной путь изучения технических предметов — курс по графу ([SPEC-11](./SPEC-11-course-and-study.md)), где `concept_recall` переиспользуется как активность шага. Отдельный ML-трек остаётся для материалов вне графа.

## Контракт

- `material_read.payload`: `{title, text}`. `material(id, user_id null=общий, module, source: pdf|note|generated|seed, title, content jsonb)`.
- `concept_recall.payload`: `{prompt, concept}` (трек) или `{conceptId, item, bloom}` (шаг курса).
- `GET /content/materials` → `[{id, module, title, content}]` — общие и свои.

## Критерии приёмки

| AC | Критерий | Проверка | Статус |
|---|---|---|---|
| AC-07.1 | Материал открывается без сети | live web | 🟢 |
| AC-07.2 | Ответ на `concept_recall` оценён по `concept_check`; неточности в повторении | live | 🟢 |
| AC-07.3 | Сценарий проходит на устройстве | device | ⚪ [P3-DEV-02](../50-plans/phase-3-hardening.md) |

## Код

- Клиент: `src/features/material-read`, `src/features/concept-recall`.
- Backend: `core/routers/content.py`, `modules/ml/rubrics.py` (`CONCEPT_CHECK`), `modules/ml/generators.py` (`concept_recall_from_material`, пока не вызывается), `core/provisioning.py` (демо-активности).

## Расхождения

| Расхождение | Задача |
|---|---|
| `concept_recall_from_material` не вызывается нигде; генерация вопросов из материала отложена до импорта | [P5-IMP-04](../50-plans/phase-5-learning-expansion.md) |

## Журнал

| Дата | Изменение |
|---|---|
| 2026-09-30 | Создана из 03-functional §2 и плана Ф1 |
