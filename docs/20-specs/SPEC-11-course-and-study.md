# SPEC-11 — Курс и прохождение шага

| | |
|---|---|
| **Статус** | `partial` — курс и петля работают; оценка шага не хранит версию узла; шаг `srs` не исполняется рендерером |
| **Требования** | FR-CRS-01..05, NFR-04, NFR-06, NFR-KG-4 |
| **Фаза** | [Ф2](../50-plans/phase-2-knowledge-model.md) · [Ф3](../50-plans/phase-3-hardening.md) |
| **Решения** | [ADR-0013](../40-adr/0013-course-as-developmental-simulation.md) |
| **Архитектура** | [30-architecture/05 §7](../30-architecture/05-knowledge-model.md#7-развитийная-модель-курса) |
| **Обновлено** | 2026-09-30 |

## Назначение

Провести учащегося от карты освоенности к цели по пути, который повторяет естественное углубление в предмет, и замкнуть петлю: задание → ответ → освоенность → граница.

## Поведение

**Построение пути** (`POST /graph/course/{domain}`, цель — ступень Блума, опционально узлы-интересы):

1. **Укоренение** (`rooting`). Непокрытые узлы ядра (`tier=core`, не `known`) — первыми, в порядке предпосылок, независимо от цели.
2. **Дифференциация** (`differentiation`). От границы вглубь по `prereq`/`specializes`, общее → частное. Узел вводится, только когда предпосылки пройдены или освоены (ЗБР).
3. **Ветвление** (`branch`). `derived`-ветки к заявленным интересам — только поверх ядра.
4. **Спираль** (`spiral`). Ядровые узлы, освоенные ниже цели, повторяются на более высокой ступени; теорию при этом заново не читают.

Под каждый узел — цепочка активностей:

```
concept_study (remember) → concept_recall (understand) → [concept_contrast, если есть misconception-ребро]
  → [concept_apply (apply), если цель ≥ apply] → srs (remember)
```

Каждый третий шаг перемежается повторением (interleaving). Пересборка пути сохраняет пройденное.

**Прохождение шага:**

1. `start` разворачивает шаг в Activity модуля `knowledge` (идемпотентно): `concept_study` и `srs` — offline, остальные — online. Payload берёт задание из кэша [SPEC-09](./SPEC-09-assessment.md). Активность, для которой задание не строится, пропускается. Заодно создаётся карточка удержания узла.
2. `answer` оценивает ответ, пишет `response` (единый лог), обновляет освоенность ([SPEC-10](./SPEC-10-placement.md)).
3. `score < 0.6` → карточка `error_log` по узлу; узел попадает в `weak`.
4. Шаг закрывается, **только** когда узел освоен: `estimate ≥ 0.75` и `confidence ≥ 0.6`. Кнопка «готово» (`complete`) — служебная.

## Контракт

| Метод | Путь | Вход | Выход |
|---|---|---|---|
| POST | `/graph/course/{domain}` | `{target_bloom='understand', interests: uuid[]}` | вид курса |
| GET | `/graph/course/{domain}` | — | `{domain, target, steps[], completed, total, current}` |
| POST | `/graph/course/{domain}/complete` | `{concept_id}` | вид курса |
| POST | `/graph/course/{domain}/step/{concept_id}/start` | — | `{conceptId, activities: [{id, type, connectivity, payload}]}` |
| POST | `/graph/course/{domain}/step/{concept_id}/answer` | `{activity_id, answer}` | `{score, explanation, mastery, stepCompleted}` |
| GET | `/graph/course/{domain}/weak` | — | `[{conceptId, title, …mastery}]`, по возрастанию `estimate` |

Шаг: `{conceptId, title, tier, reason: rooting|differentiation|branch|spiral, bloom, activities: [{type, bloom}], done}`.

`course(id, user_id, domain, target {bloom, concepts: [id интересов]}, path jsonb, progress {completed: []}, created_at)`.

## Критерии приёмки

| AC | Критерий | Проверка | Статус |
|---|---|---|---|
| AC-11.1 | Ядровые узлы идут раньше производных независимо от цели | test `test_course.py`, live | 🟢 |
| AC-11.2 | Узел без освоенных предпосылок не вводится раньше них | test | 🟢 |
| AC-11.3 | Узел с `misconception`-ребром получает `concept_contrast` | test | 🟢 |
| AC-11.4 | Пересборка сохраняет пройденные шаги | test | 🟢 |
| AC-11.5 | Шаг разворачивается в 4 активности с верной `connectivity`; повторный `start` не дублирует | test `test_study.py`, live | 🟢 |
| AC-11.6 | Ответ пишет строку `response` | test | 🟢 |
| AC-11.7 | Слабый ответ → карточка по узлу, узел в `weak`; верные ответы закрывают шаг | test, live | 🟢 |
| AC-11.8 | Оценка ответа на шаге хранит версию узла и id задания | test | ⚪ |
| AC-11.9 | Активность `srs` шага исполняется на клиенте (карточка узла) | live | ⚪ |
| AC-11.10 | Сквозной сценарий граф → плейсмент → курс → шаг → ответ проходит на устройстве | device | ⚪ |

## Код

`modules/knowledge/{course,study,mastery}.py`, эндпоинты в `router.py`. Клиент: `src/features/course/ui/course-path.tsx`, `src/features/concept-study`, `src/pages/course`, `src/pages/home/model/next-action.ts`.

## Расхождения

| Расхождение | Задача |
|---|---|
| `response.grade` шага = `{score, explanation, conceptId}` — без `conceptVersion` и id задания (NFR-06) | [P3-KG-03](../50-plans/phase-3-hardening.md) |
| Тип `srs` объявлен клиентом, рендерера нет; шаг `srs` не исполняется | P3-SRS-01 |
| Ответы на шагах идут напрямую в API и офлайн не работают, хотя `concept_study` помечен offline только для чтения теории | принято: проверка ответа требует сети; зафиксировать в ADR-0015 |
| Сквозной сценарий не проходился на устройстве | P3-DEV-03 |

## Журнал

| Дата | Изменение |
|---|---|
| 2026-09-30 | Создана из плана Ф2 (KG5) и кода |
