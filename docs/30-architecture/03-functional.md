# 03 — Функциональная архитектура: модули и сценарии

Какие модули есть в системе, какие типы Activity и рубрики они объявляют и как из них складываются сквозные сценарии. Абстракции (Activity, манифест, sync) — в [02 — Логический план](./02-logical.md); поведение каждой возможности с критериями приёмки — в [спеках](../20-specs/README.md); границы продукта и этапы — в [00-product/scope](../00-product/scope.md) и [50-plans](../50-plans/README.md).

> До 2026-09-30 здесь также лежали объём MVP, роадмап и метрики. Они перенесены: объём — в [scope](../00-product/scope.md), роадмап — в [план](../50-plans/README.md), метрики — в [metrics](../00-product/metrics.md).

---

## 1. Модуль `languages` (первичная цель: IELTS / TOEFL)

Экзамены проверяют четыре навыка. Механика эффективности у рецепции и продукции **разная** ([обоснование](../00-product/vision.md#педагогическое-обоснование)).

### 1.1 Типы Activity

| Тип | Навык | Connectivity | Механика | Спека | Состояние |
|---|---|---|---|---|---|
| `ielts_writing_task2` | Writing (продукция) | online + офлайн-fallback | Эссе → оценка по band descriptors → ошибки → образец | [SPEC-06](../20-specs/SPEC-06-writing.md) | ✅ |
| `ielts_writing_task1` | Writing | online | Описание графика/таблицы → оценка | [SPEC-16](../20-specs/SPEC-16-learning-expansion.md) | Ф5 |
| `reading_drill` | Reading (рецепция) | offline* | Passage + вопросы в формате экзамена, на время | [SPEC-15](../20-specs/SPEC-15-reception-drills.md) | Ф4 |
| `listening_drill` | Listening | offline* (аудио в кэше) | Аудио + вопросы, на время | [SPEC-15](../20-specs/SPEC-15-reception-drills.md) | Ф4 |
| `speaking_response` | Speaking (продукция) | online | Устный ответ → STT → оценка | [SPEC-14](../20-specs/SPEC-14-speaking.md) | Ф4 |
| `vocab_srs` | Vocabulary | offline | FSRS: AWL + error-log | [SPEC-05](../20-specs/SPEC-05-srs-and-error-log.md) | ✅ экраном повторения; тип — под вопросом ([ADR-0015](../40-adr/0015-srs-is-a-card-queue.md)) |

\* Детерминированные дриллы проверяются офлайн локально; разбор «почему дистрактор неверен» приходит online-обогащением при сети.

### 1.2 Рубрики

| Рубрика | Критерии | Состояние |
|---|---|---|
| `ielts_writing_task2` v1 | Task Response, Coherence and Cohesion, Lexical Resource, Grammatical Range and Accuracy → band 0–9 | ✅ |
| `ielts_writing_task1` | Task Achievement, Coherence and Cohesion, Lexical Resource, Grammatical Range and Accuracy | Ф5 |
| `toefl_writing_integrated`, `toefl_writing_independent` | по официальным рубрикам TOEFL | Ф5 |
| `ielts_speaking` | Fluency & Coherence, Lexical Resource, Grammatical Range & Accuracy, Pronunciation | Ф4 |

### 1.3 Лексика через error-log

Ошибки из письма, а позже и из речи, становятся карточками `srs_card {source: 'error_log'}`. Плюс стартовая колода **Academic Word List** (пока демо-выборка из 10 слов). Словарь учится не в отрыве, а по реальным слабым местам продукции.

---

## 2. Модуль `ml` (первичная цель: программирование / ML)

Механика: *прочитал → активно вспомнил → сделал → получил ревью*.

| Тип | Назначение | Connectivity | Спека | Состояние |
|---|---|---|---|---|
| `material_read` | Чтение материала | offline | [SPEC-07](../20-specs/SPEC-07-ml-track.md) | ✅ |
| `concept_recall` | Объяснить понятие своими словами → AI-проверка | online (с очередью) | [SPEC-07](../20-specs/SPEC-07-ml-track.md) | ✅ (переиспользуется шагом курса) |
| `concept_srs` | Удержание понятий | offline | [SPEC-05](../20-specs/SPEC-05-srs-and-error-log.md) | тип под вопросом ([ADR-0015](../40-adr/0015-srs-is-a-card-queue.md)) |
| `code_task` | Задача на код → ревью по критериям | online | [SPEC-16](../20-specs/SPEC-16-learning-expansion.md) | Ф5 |

Рубрики: `concept_check` v1 (Correctness, Completeness, Explanation, 0–5) — ✅; `ml_code_review` (Correctness, Numerical stability / Efficiency, Idiomatic style, Explanation) — Ф5.

**Импорт** (Ф5): PDF/Markdown → `material` → персональные узлы графа `source='material'` и вопросы `concept_recall` ([SPEC-16](../20-specs/SPEC-16-learning-expansion.md)).

---

## 3. Модуль `knowledge` (модель знаний)

Лежит над движком Activity и не зависит от предмета. Граф понятий, задания из теории узла, плейсмент и курс ([05](./05-knowledge-model.md)). Активности шага курса регистрируются этим модулем; `concept_recall` переиспользуется из `ml`: реестр запрещает объявлять один тип дважды.

| Тип | Назначение | Connectivity | Спека | Состояние |
|---|---|---|---|---|
| `concept_study` | Разобрать теорию узла с примерами | offline | [SPEC-11](../20-specs/SPEC-11-course-and-study.md) | ✅ |
| `concept_contrast` | Отличить понятие от типичного заблуждения | online | SPEC-11 | ✅ |
| `concept_apply` | Задача на применение понятия | online | SPEC-11 | ✅ |
| `srs` | Удержание понятия узла | offline | SPEC-11 | ⚠️ объявлен, не исполняется (P3-SRS-01) |
| *(`placement_probe`)* | Зонд плейсмента | online | [SPEC-10](../20-specs/SPEC-10-placement.md) | ✅ отдельным экраном, не как Activity |

AI-роли модуля: `build_graph`, `expand_node`, `generate_assessment`, `estimate_mastery`. Все используют доменно-нейтральный `AIGateway.structured`.

---

## 4. Сквозные сценарии

### 4.1 Начало работы

```
регистрация → онбординг: «что изучаете» + целевой уровень → profile.subject
  → граф предмета пуст? → построить черновик (любой пользователь, узлы draft)
  → плейсмент: зонды на границе знаний → карта освоенности
  → курс до цели → «Сегодня» показывает первый шаг с причиной
```

Спеки: [SPEC-12](../20-specs/SPEC-12-learner-experience.md), [SPEC-08](../20-specs/SPEC-08-knowledge-graph.md), [SPEC-10](../20-specs/SPEC-10-placement.md), [SPEC-11](../20-specs/SPEC-11-course-and-study.md).

### 4.2 Ежедневная сессия (offline-first)

```
открыл приложение (может быть офлайн)
  → «Сегодня»: одно действие по приоритету — шаг курса / повторение / плейсмент
  → шаг курса: теория офлайн → вопросы при сети → освоенность → шаг закрыт или узел в повторение
  → повторение: карточки due (FSRS, локально)
  → продукция (эссе): офлайн — черновой сигнал и job в очереди; при сети — полная оценка
```

### 4.3 Оценка продукции (мост offline → online)

```
эссе офлайн → локальный черновой сигнал (объём, абзацы, AWL)
  → сеть → sync push → job grade_writing → LLM по рубрике
  → разбор: 4 критерия + ошибки + образец
  → ошибки → error-log → карточки повторения → pull на клиент
```

Спеки: [SPEC-03](../20-specs/SPEC-03-sync-and-jobs.md), [SPEC-04](../20-specs/SPEC-04-ai-gateway-and-rubrics.md), [SPEC-06](../20-specs/SPEC-06-writing.md).

### 4.4 Петля освоения узла

```
узел графа → задание из его теории → ответ → response (единый лог) → освоенность → граница
          ↘ слабый ответ (score < 0.6) → карточка FSRS по узлу ↗
```

### 4.5 Рост графа

```
«Углубиться» в узел по направлению интереса → LLM → персональные узлы grown_llm
куратор: draft-узлы → вычитка → approve / tier=core → (Ф6) промоция персональных узлов в канон
```

---

## Связанные документы

[01 — Архитектура](./01-architecture.md) · [02 — Логический план](./02-logical.md) · [05 — Модель знаний](./05-knowledge-model.md) · [требования](../10-requirements/functional.md)
