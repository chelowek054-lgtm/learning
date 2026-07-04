# 02 — Логический план

Модель данных, движок Activity, модульная система, FSRS, синхронизация и очередь задач. Технический стек — в [01 — Архитектура](./01-architecture.md); конкретные фичи — в [03 — Функциональный план](./03-functional.md).

---

## 1. Центральная абстракция: Activity

Всё обучающее взаимодействие — это **Activity**. Ядро не знает, «язык» это или «ML»; оно диспетчеризует по `type`, а специфику берёт из модуля.

```ts
type Connectivity = 'offline' | 'online';

interface Activity {
  id: string;
  module: string;            // 'languages' | 'ml' | ...
  type: string;              // 'ielts_writing' | 'srs_review' | 'concept_recall' | ...
  connectivity: Connectivity;
  payload: Record<string, unknown>;   // структура задаётся модулем
  createdAt: string;
  dueAt?: string;            // для SRS-активностей
}
```

`payload` — JSONB на сервере, TEXT(JSON) в SQLite. Его схему валидирует **модуль**, а не ядро.

### Классификация типов Activity (обоснование в [00 — Обзор](../README.md#ключевой-педагогический-вывод-обоснование-архитектуры))

| Категория | Тип навыка | Примеры типов |
|---|---|---|
| `srs_review` | Удержание фактов | карточки: слово↔перевод, концепт↔объяснение |
| `exam_drill` | Рецепция (тайминг+формат) | IELTS reading passage, listening MCQ |
| `input_comprehension` | Рецепция (вход) | чтение/аудио выше уровня + вопросы |
| `graded_production` | Продукция | эссе, устный ответ, задача с кодом |

---

## 2. Модель данных

Обе оси разделения (connectivity, module) — это **колонки**, а не отдельные схемы. Добавить тему = строки с новым `module`; добавить офлайн-фичу = `connectivity='offline'`.

### 2.1 Основные таблицы

```sql
-- Пользователь
user (
  id            uuid pk,
  email         text,
  created_at    timestamptz,
  profile       jsonb           -- цели, целевой балл TOEFL/IELTS, уровень
)

-- Единица взаимодействия
activity (
  id            uuid pk,
  user_id       uuid fk,
  module        text,           -- 'languages' | 'ml'
  type          text,           -- 'ielts_writing' | 'srs_review' | ...
  connectivity  text,           -- 'offline' | 'online'
  payload       jsonb,
  created_at    timestamptz,
  due_at        timestamptz null
)

-- ЕДИНЫЙ EVENT LOG (растёт офлайн, источник для FSRS и адаптации)
response (
  id                uuid pk,
  activity_id       uuid fk,
  user_id           uuid fk,
  user_answer       jsonb,       -- текст эссе / выбор / код
  grade             jsonb null,  -- результат скоринга (по рубрике) или null пока pending
  local_created_at  timestamptz, -- время на устройстве (offline-first)
  synced            boolean default false
)

-- SRS-состояние карточки (FSRS)
srs_card (
  id            uuid pk,
  user_id       uuid fk,
  module        text,
  front         jsonb,          -- вопрос/стимул
  back          jsonb,          -- ответ/объяснение
  source        text,           -- 'error_log' | 'awl' | 'imported' | 'generated'
  fsrs_state    jsonb,          -- {stability, difficulty, reps, lapses, ...}
  due_at        timestamptz,
  created_at    timestamptz
)

-- МОСТ offline → online
job (
  id            uuid pk,
  user_id       uuid fk,
  type          text,           -- 'grade_writing' | 'generate_cards' | 'grade_code' | ...
  status        text,           -- 'pending' | 'running' | 'done' | 'failed'
  input_ref     jsonb,          -- ссылка на response/activity + параметры
  result        jsonb null,
  attempts      int default 0,
  created_at    timestamptz,
  updated_at    timestamptz
)

-- Учебные материалы (кэшируются локально для офлайн-чтения)
material (
  id            uuid pk,
  user_id       uuid fk null,   -- null = общий, иначе персональный
  module        text,
  source        text,           -- 'pdf' | 'note' | 'generated' | 'seed'
  title         text,
  content       jsonb,          -- текст/структура
  created_at    timestamptz
)

-- Рубрики-оценщики (версионируются; см. инвариант №6)
rubric (
  id            text,           -- 'ielts_writing_task2'
  version       int,
  module        text,
  model         text,           -- 'claude-opus-4-8' | 'claude-sonnet-4-6'
  prompt        text,           -- шаблон промпта-оценщика
  schema        jsonb,          -- ожидаемая структура grade
  pk (id, version)
)
```

### 2.2 Локальная (SQLite) vs серверная (Postgres)

| Таблица | SQLite (клиент) | Postgres (сервер) | Роль |
|---|---|---|---|
| `activity` | ✅ | ✅ | двусторонняя синхронизация |
| `response` | ✅ (источник) | ✅ | клиент пишет офлайн → синк наверх |
| `srs_card` | ✅ (источник) | ✅ (зеркало) | планирование локально |
| `job` | ✅ (создаётся офлайн) | ✅ (исполняется) | мост |
| `material` | ✅ (кэш для чтения) | ✅ (источник) | синк вниз |
| `rubric` | ❌ | ✅ | только сервер |
| `user` | частично (профиль) | ✅ | синк профиля |

---

## 3. Модульная система

Модуль — плагин над доменно-независимым ядром. Регистрируется через **манифест**.

### 3.1 Контракт манифеста (клиент)

```ts
interface ModuleManifest {
  id: string;                       // 'languages'
  title: string;                    // 'Языки'
  activityTypes: ActivityTypeDef[]; // какие типы поддерживает
  renderers: Record<string, ActivityRenderer>;  // type -> React-компонент
  localGraders?: Record<string, LocalGrader>;    // офлайн-fallback проверки
  importers?: ImporterDef[];        // пайплайны импорта контента
  schedulerConfig?: SchedulerConfig;// как часто повторять
}

interface ActivityTypeDef {
  type: string;                     // 'ielts_writing'
  connectivity: Connectivity;       // требует ли сети по умолчанию
  payloadSchema: JSONSchema;        // валидация payload
  producesErrorLog?: boolean;       // питает ли SRS через error-log
}

// Офлайн-fallback: мгновенный черновой сигнал без LLM
type LocalGrader = (answer: unknown, payload: unknown) => Partial<Grade>;
```

### 3.2 Контракт модуля (backend)

```python
class ModuleBackend(Protocol):
    id: str
    def rubrics(self) -> list[Rubric]: ...          # промпты-оценщики
    def generators(self) -> dict[str, Generator]: ...# генерация контента
    def grade(self, activity, answer) -> Grade: ...  # вызов LLM по рубрике
```

### 3.3 Регистрация

Ядро при старте собирает манифесты всех подключённых модулей в реестр. Диспетчеризация: `activity.type` → модуль → рендерер/грейдер. **Ни одной ветки `if module == 'languages'` в ядре** — только табличный lookup.

Добавление новой темы (напр. `math`) = новый пакет `module-math` + `modules/math/` на бэке. Ядро не трогается.

---

## 4. FSRS-планировщик

- Библиотека **ts-fsrs** на клиенте, работает офлайн.
- Состояние карточки — в `srs_card.fsrs_state`.
- Отзыв пользователя (Again/Hard/Good/Easy) → `response` + пересчёт `fsrs_state` и `due_at`.
- Планировщик читает **только `response`** (инвариант №4): очередь на сегодня = `srs_card WHERE due_at <= now`.

### Связь продукции и SRS через error-log

```
graded_production завершён → grade содержит errors[]
   → для каждой значимой ошибки создаётся srs_card {source: 'error_log'}
     (например: неверная коллокация → карточка на правильную коллокацию)
   → карточка попадает в обычный FSRS-цикл
```

Так письмо/речь/код напрямую усиливают запоминание слабых мест. `producesErrorLog: true` в `ActivityTypeDef` включает это поведение.

---

## 5. Job Queue и синхронизация

### 5.1 Жизненный цикл job

```
offline: создан pending ──► sync push ──► running (backend)
                                            │
                              ┌─────────────┴───────────┐
                          success                     fail
                              │                         │
                            done                 attempts++ ; retry/failed
                              │
                    sync pull ──► клиент применяет result
```

### 5.2 Алгоритм sync (двухфазный)

```
PUSH (клиент → сервер):
  1. Отправить новые response (synced=false) и pending job.
  2. Отправить изменения srs_card (fsrs_state, due_at).
  3. Пометить отправленное synced=true по ack сервера.

PULL (сервер → клиент):
  4. Забрать done-jobs (результаты скоринга/генерации).
  5. Забрать новый/обновлённый material и generated srs_card.
  6. Применить результаты, обновить error-log → SRS.
```

### 5.3 Разрешение конфликтов

- **Уровень записи, last-write-wins** по `local_created_at` / `updated_at`.
- `response` иммутабелен после создания (только дополняется `grade`) → конфликтов почти нет.
- `srs_card.fsrs_state` — LWW; при мульти-девайсе допустим редкий откат интервала (приемлемо для MVP; полноценный CRDT — вне scope).
- **Идемпотентность jobs:** `job.id` генерируется на клиенте (UUID) → повторная отправка не создаёт дубль.

---

## 6. AI-gateway (backend)

Единая точка вызова LLM. Отвечает за:

- **Выбор модели** per-rubric (`rubric.model`).
- **Подстановку в шаблон** промпта рубрики + payload + ответ пользователя.
- **Структурированный вывод**: результат валидируется по `rubric.schema` (grade — строгий JSON: баллы по критериям, ошибки, образец).
- **Кэш**: генерация детерминированного контента кэшируется по хэшу входа.
- **Учёт расходов**: логирование токенов per-user/per-type.
- **Версионирование**: изменение рубрики → новая `version`, старые ответы сохраняют ссылку на версию, по которой оценивались.

```
POST /jobs {type: grade_writing, input_ref}
  → gateway.load_rubric('ielts_writing_task2', latest)
  → gateway.call(model=rubric.model, prompt=render(rubric.prompt, activity, answer))
  → validate(result, rubric.schema)
  → сохранить в response.grade + сгенерировать error-log карточки
```

---

## 7. Модель Grade (результат скоринга)

```ts
interface Grade {
  rubricId: string;
  rubricVersion: number;
  criteria: { name: string; score: number; max: number; comment: string }[];
  overall?: number;            // напр. band 6.5
  errors: {                    // → питают error-log/SRS
    kind: string;              // 'collocation' | 'grammar' | 'coherence' | ...
    excerpt: string;
    correction: string;
    explanation: string;
  }[];
  exemplar?: string;           // образцовый переписанный вариант
  gradedOfflineFallback?: boolean;  // true = черновой локальный сигнал
}
```

---

## Связанные документы

- Стек и топология — [01 — Архитектура](./01-architecture.md).
- Конкретные типы Activity по модулям и сценарии — [03 — Функциональный план](./03-functional.md).
