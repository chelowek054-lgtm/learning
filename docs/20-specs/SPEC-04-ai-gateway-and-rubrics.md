# SPEC-04 — AI-gateway, рубрики, стоимость

| | |
|---|---|
| **Статус** | `partial` — всё работает; остаётся решить судьбу неиспользуемого `generate()` |
| **Требования** | FR-AI-01..07, NFR-02, NFR-06, NFR-09, NFR-10 |
| **Фаза** | [Ф1](../50-plans/phase-1-mvp.md) · [Ф3](../50-plans/phase-3-hardening.md) |
| **Решения** | [ADR-0009](../40-adr/0009-llm-provider-as-config.md) |
| **Обновлено** | 2026-09-30 |

## Назначение

Держать все вызовы LLM в одной точке на backend: безопасность ключей, версионирование критериев, контроль стоимости, возможность сменить провайдера без правки кода.

## Поведение

1. **Выбор реализации.** Есть `LLM_API_KEY` → `OpenAICompatibleGateway`, нет → `MockAIGateway` с детерминированными ответами. Модули спрашивают `has_llm()`, а не переменную окружения.
2. **Оценка по рубрике** (`grade`): рубрика берётся из БД (последняя версия или конкретная), промпт = шаблон рубрики + задание из `payload` + ответ. Модель — `rubric.model`, если задана, иначе `LLM_MODEL_SCORING`. Результат запрашивается вызовом инструмента `submit_grade` по `GRADE_JSON_SCHEMA`, дополняется `rubricId` и `rubricVersion`.
3. **Структурированный вызов** (`structured(tool, description, schema, prompt)`) — доменно-нейтральный. Схемы и промпты предметов живут в модулях (граф, задания, оценка ответа).
4. **Транспорт** повторяет запрос до 3 раз: обрыв канала; 402 (бюджет подстраивается под остаток кредита); ответ текстом вместо вызова инструмента. `max_tokens` передаётся всегда.
5. **Кэш** (`llm_cache`, ключ — sha256 от модели, инструмента, схемы и промпта). Включается явно (`cache=True`) только там, где ответ детерминирован по входу: оценка по рубрике и оценка открытого ответа. Граф и рост графа не кэшируются: «перестроить» даёт новый результат. Задания по узлу кэшируются отдельно ([SPEC-09](./SPEC-09-assessment.md)). Сбой кэша — промах, а не ошибка.
6. **Учёт**: каждый ответ провайдера, включая оплаченные неудачные попытки, пишет `llm_usage` (пользователь из Bearer-токена запроса, назначение — инструмент, модель, токены). Сбой учёта не ломает вызов. `GET /usage/summary` (администратор) — расход по пользователю и назначению за период.
7. **Рубрики на свежей базе**: API при старте добавляет недостающие рубрики модулей (insert-if-absent, `(id, version)` не перезаписываются); без БД API всё равно стартует.

## Контракт

```python
class AIGateway(Protocol):
    def grade(self, rubric: Rubric, activity_payload: dict, answer: Any) -> dict  # Grade
    def generate(self, generator_id: str, params: dict) -> dict
    def structured(self, tool_name: str, description: str, schema: dict, prompt: str) -> dict
```

`Grade`:

```ts
{ rubricId, rubricVersion, criteria: [{name, score, max, comment}], overall?, errors: [{kind, excerpt, correction, explanation}], exemplar?, gradedOfflineFallback? }
```

`rubric(id, version, module, model, prompt, schema)`, PK `(id, version)`. Реестр рубрик:

| Рубрика | Модуль | Критерии |
|---|---|---|
| `ielts_writing_task2` v1 | languages | Task Response, Coherence and Cohesion, Lexical Resource, Grammatical Range and Accuracy (0–9) |
| `concept_check` v1 | ml | Correctness, Completeness, Explanation (0–5) |

Конфиг: `LLM_BASE_URL` (RouterAI), `LLM_API_KEY`, `LLM_MODEL_GENERATION`, `LLM_MODEL_SCORING`, `LLM_MAX_TOKENS` (16384), `LLM_TIMEOUT_SECONDS`, `LLM_SITE_URL`, `LLM_SITE_TITLE`.

`llm_usage(id, user_id null, purpose, model, prompt_tokens, completion_tokens, created_at)` (миграция `0009`); `llm_cache(key, payload jsonb, created_at)` (миграция `0012`). Стоимость в деньгах не считается: у провайдеров она разная, считать по токенам.

## Критерии приёмки

| AC | Критерий | Проверка | Статус |
|---|---|---|---|
| AC-04.1 | Без ключа все сценарии проходят на заглушке | test (conftest гасит ключ) | 🟢 |
| AC-04.2 | Смена провайдера — только `.env` | live на RouterAI 2026-08-25 | 🟢 |
| AC-04.3 | Обрыв, 402 и текст вместо инструмента повторяются | test `test_openai_gateway.py` | 🟢 |
| AC-04.4 | `grade` содержит `rubricId` и `rubricVersion` | ревью `openai_compatible.py`, `mock.py` | 🟢 |
| AC-04.5 | Слаг модели не зашит в рубрику; пустой → из конфига | миграция `0008`, live | 🟢 |
| AC-04.6 | Токены каждого вызова учтены по пользователю и типу | test `test_usage.py` | 🟢 |
| AC-04.7 | Повторный вызов с `cache=True` и тем же входом берётся из кэша; без `cache` — нет | test `test_llm_cache.py` | 🟢 |
| AC-04.8 | Свежая база после миграций получает рубрики без `seed.py` | live 2026-09-30 (0 → 2 рубрики), test | 🟢 |
| AC-04.9 | Ключ LLM отсутствует в клиенте и в git | grep (NFR-02) | 🟢 |

## Код

`core/ai_gateway/{__init__,base,mock,openai_compatible}.py`, `core/usage.py`, `core/llm_cache.py`, `core/routers/usage.py`, `core/config.py`, рубрики `modules/languages/rubrics.py`, `modules/ml/rubrics.py`, сид `scripts/seed.py`, миграция `0008_clear_vendor_model_pins`.

## Расхождения

| Расхождение | Задача |
|---|---|
| `generate()` в протоколе не используется ни одним модулем | удалить из протокола или реализовать — решить до Ф4 |
| В живой БД стенда осталась рубрика `ml_code_review v1` от заглушки Ф0: в коде её нет, рубрика Ф5 ([P5-CODE-01](../50-plans/phase-5-learning-expansion.md)) займёт этот id | при P5-CODE-01 перезаписать новой версией |

## Журнал

| Дата | Изменение |
|---|---|
| 2026-09-30 | Создана из 02-logical §6–7 и кода; снят ложный статус «сделано» у учёта токенов и кэша |
| 2026-09-30 | P3-AI-01..03: рубрики при старте, учёт токенов, кэш оценки |
