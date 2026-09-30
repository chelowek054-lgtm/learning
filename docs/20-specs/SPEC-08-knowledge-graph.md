# SPEC-08 — Граф знаний: канон, персональный слой, рост

| | |
|---|---|
| **Статус** | `partial` — чтение, построение, курирование, персональный слой и рост работают; персональные узлы без версии, перегенерация сопоставляет по заголовку |
| **Требования** | FR-KG-01..08, NFR-KG-1..6, NFR-15 |
| **Фаза** | [Ф2](../50-plans/phase-2-knowledge-model.md) · [Ф3](../50-plans/phase-3-hardening.md) |
| **Решения** | [ADR-0011](../40-adr/0011-knowledge-as-module-cow.md), [ADR-0016](../40-adr/0016-empty-domain-built-by-learner.md) |
| **Архитектура** | [30-architecture/05](../30-architecture/05-knowledge-model.md) |
| **Обновлено** | 2026-09-30 |

## Назначение

Сделать структуру предмета явной: граф понятий с теорией в узлах, общий для всех (канон) и растущий под каждого (персональный слой). Граф — основа плейсмента, курса и генерации заданий.

## Поведение

1. **Чтение.** `GET /graph/{domain}` отдаёт эффективный граф: канонические узлы и рёбра домена, перекрытые персональным слоем пользователя. Новый пользователь ничего не копирует: все узлы `origin='inherited'`.
2. **Построение пустой области.** Любой пользователь вызывает `canon/build`, если в домене нет узлов. LLM возвращает до `max_nodes` (2–20, по умолчанию 8) узлов с теорией, тиром, `confidence` и рёбрами. Узлы сохраняются `source='llm'`, `status='draft'`. Повторный build или `refresh` — только администратор. Существующий узел с непригодной теорией дополняется, если черновик лучше; версия растёт.
3. **Курирование канона** (администратор): создать или изменить узел (правка теории → `version+1`), создать ребро, пересчитать centrality, подтвердить узел (`approve`, можно сменить тир).
4. **Core-детекция.** Centrality = доля узлов, транзитивно зависящих от данного по `prereq`/`specializes`. Кандидат в ядро: centrality ≥ 0.5 **или** узел уже помечен `core`, в том числе LLM при построении. В ядро переводит куратор.
5. **Персональный слой.** Перекрыть теорию канонического узла (`origin='edited'`); создать свой узел и ребро; изменить или удалить свои. Канон при этом не меняется.
6. **Рост.** `expand(concept_id, direction)`: LLM предлагает узлы в направлении интереса; они становятся персональными (`origin='grown_llm'`), рёбра восстанавливаются по ключам, несвязанный узел цепляется к исходному.
7. **Домен в URL** кодируется: предмет с кириллицей работает во всех запросах.

## Контракт

Эндпоинты графа (всего под `/graph` 25 эндпоинтов, 14 — граф, ниже; 11 — задания, плейсмент и курс, в SPEC-09..11):

| Метод | Путь | Право | Назначение |
|---|---|---|---|
| GET | `/{domain}` | user | Эффективный граф |
| POST | `/canon/build` | user, если домен пуст; иначе admin | `{domain, topic, refresh=false, max_nodes=8}` |
| POST | `/canon/nodes` | admin | Создать канонический узел |
| PUT | `/canon/nodes/{id}` | admin | Изменить; правка `content` → `version+1` |
| POST | `/canon/edges` | admin | Создать ребро |
| POST | `/canon/recompute-centrality` | admin | `{domain}` → `[{id, title, tier, centrality, dependents, suggestedCore}]` |
| POST | `/canon/nodes/{id}/approve` | admin | `{tier?}` → `status='approved'` |
| POST | `/nodes` | user | Свой узел `{domain, title, content}` |
| POST | `/nodes/{base_id}/override` | user | Перекрыть теорию канона |
| PUT / DELETE | `/user-nodes/{id}` | user (владелец) | Изменить / удалить свой узел |
| POST / DELETE | `/user-edges[/{id}]` | user (владелец) | Своё ребро |
| POST | `/expand` | user | `{concept_id, direction}` → эффективный граф |

Эндпоинты заданий, плейсмента и курса — в SPEC-09..11.

Узел эффективного графа: `{id, kind: canonical|personal, userConceptId, title, tier, centrality, content, bloomLevels, difficulty, version, mastery, status (locked|frontier|learning|known — персональный слой), origin (inherited|edited|grown_llm), reviewStatus (draft|approved — только у канонических)}`. Персональный узел всегда `tier='derived'`, `version=1`.

Теория узла (`NodeContent`): `{summary, sections: [{heading, body, examples[], counter_examples[]}], references: [{title, url?}]}`. Узел пригоден для заданий (`is_groundable`), если есть хотя бы один раздел с телом.

Типы рёбер: `prereq`, `specializes`, `part_of`, `related`, `contrasts`, `misconception`, `example`.

Данные — [30-architecture/05 §4](../30-architecture/05-knowledge-model.md#4-модель-данных).

## Критерии приёмки

| AC | Критерий | Проверка | Статус |
|---|---|---|---|
| AC-08.1 | Новый пользователь видит канон; все узлы `inherited`, строк `user_concept` не создано | test `test_cow.py`, live | 🟢 |
| AC-08.2 | Оверрайд виден только автору; канон не изменился | test `test_cow.py` | 🟢 |
| AC-08.3 | Build в пустом домене → 200 любому; повторный build не-админом → 403; узлы `draft` | test `test_graph_access.py` | 🟢 |
| AC-08.4 | `canon/*` для не-админа → 403 | test `test_graph_access.py` | 🟢 |
| AC-08.5 | Centrality: корневая предпосылка 1.0, лист 0.0; `suggestedCore` по порогу или пометке | test `test_centrality.py`, live | 🟢 |
| AC-08.6 | Кривая форма `content` от клиента → 422; мусор от LLM отброшен, узел сохранён | test `test_content.py` | 🟢 |
| AC-08.7 | Персональные узлы одного домена не видны в другом | test, миграция `0006` | 🟢 |
| AC-08.8 | `expand` создаёт связанные персональные узлы `grown_llm` | live | 🟢 |
| AC-08.9 | Предмет «Теория музыки» проходит build и чтение | live web 2026-08-25 | 🟢 |
| AC-08.10 | Правка своего узла поднимает версию; по нему генерируются задания | test | ⚪ |
| AC-08.11 | Перегенерация, где модель переименовала узел, не создаёт дубль | test | ⚪ |

## Код

`modules/knowledge/{models,schemas,cow,centrality,content,ai,router}.py`, миграции `0003`, `0006`. Клиент: `src/shared/api/graph-api.ts`, `src/entities/concept`, `src/features/graph-editor/ui/{graph-map,graph-curation}.tsx`, `src/pages/graph`.

## Расхождения

| Расхождение | Задача |
|---|---|
| Персональные узлы всегда `version=1` (`resolve_node`); задания по ним не генерируются | [P3-KG-01](../50-plans/phase-3-hardening.md) |
| Build/refresh сопоставляет узлы по `title`: переименование моделью даёт дубль | P3-KG-02 |
| `effective_graph` грузит все узлы домена целиком (рёбра уже фильтруются в SQL) | P3-KG-04 |
| В 05 §4 модель `user_concept` без поля `title`, в коде оно есть (для своих узлов) | исправлено в документе 2026-09-30 |

## Открытые вопросы

Гранулярность узла; калибровка порога core-детекции; граф для языкового домена ([SPEC-16](./SPEC-16-learning-expansion.md)). Реестр — [30-architecture/05 §11](../30-architecture/05-knowledge-model.md#11-открытые-вопросы).

## Журнал

| Дата | Изменение |
|---|---|
| 2026-09-30 | Создана из 05-knowledge-model, плана Ф2 и кода |
