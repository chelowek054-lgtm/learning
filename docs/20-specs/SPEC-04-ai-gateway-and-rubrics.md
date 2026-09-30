# SPEC-04 — AI-gateway, рубрики, стоимость

| | |
|---|---|
| **Статус** | `partial` — вызовы, заглушка и рубрики работают; учёта токенов нет, кэш только у заданий, рубрики сидятся руками |
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
5. **Кэш** (цель): детерминированная генерация с тем же входом не оплачивается повторно. Сейчас кэшируются только задания по узлу ([SPEC-09](./SPEC-09-assessment.md)).
6. **Учёт** (цель): каждый вызов пишет токены, модель, пользователя и тип задачи.
7. **Рубрики на свежей базе** (цель): доступны после `alembic upgrade head` без ручного `seed`.

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

Цель `FR-AI-05` — таблица `llm_usage(id, user_id, job_type|role, model, prompt_tokens, completion_tokens, cost, created_at)`.

## Критерии приёмки

| AC | Критерий | Проверка | Статус |
|---|---|---|---|
| AC-04.1 | Без ключа все сценарии проходят на заглушке | test (conftest гасит ключ) | 🟢 |
| AC-04.2 | Смена провайдера — только `.env` | live на RouterAI 2026-08-25 | 🟢 |
| AC-04.3 | Обрыв, 402 и текст вместо инструмента повторяются | test `test_openai_gateway.py` | 🟢 |
| AC-04.4 | `grade` содержит `rubricId` и `rubricVersion` | ревью `openai_compatible.py`, `mock.py` | 🟢 |
| AC-04.5 | Слаг модели не зашит в рубрику; пустой → из конфига | миграция `0008`, live | 🟢 |
| AC-04.6 | Токены каждого вызова учтены по пользователю и типу | test | ⚪ |
| AC-04.7 | Повторный `structured` с тем же входом берётся из кэша | test | ⚪ |
| AC-04.8 | Свежая база после миграций оценивает эссе без `seed.py` | live | ⚪ |
| AC-04.9 | Ключ LLM отсутствует в клиенте и в git | grep (NFR-02) | 🟢 |

## Код

`core/ai_gateway/{__init__,base,mock,openai_compatible}.py`, `core/config.py`, рубрики `modules/languages/rubrics.py`, `modules/ml/rubrics.py`, сид `scripts/seed.py`, миграция `0008_clear_vendor_model_pins`.

## Расхождения

| Расхождение | Задача |
|---|---|
| Учёта токенов нет, хотя Ф1 (`P1-WS3-03`) отмечала его сделанным | [P3-AI-02](../50-plans/phase-3-hardening.md) |
| Кэша генерации по хэшу входа нет (`P1-WS3-03` отмечала сделанным); кэш есть только у заданий | P3-AI-03 |
| Рубрики появляются только после ручного `scripts/seed.py`; без них job падает `Рубрика не найдена` | P3-AI-01 |
| `generate()` в протоколе не используется ни одним модулем | P3-AI-03 (решить: удалить или реализовать) |

## Журнал

| Дата | Изменение |
|---|---|
| 2026-09-30 | Создана из 02-logical §6–7 и кода; снят ложный статус «сделано» у учёта токенов и кэша |
