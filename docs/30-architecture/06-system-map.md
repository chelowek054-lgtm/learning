# 06 — Карта системы

Функциональная карта: какие части есть, что каждая делает, как они связаны и где лежат в коде. Это путеводитель; детали — в [01](./01-architecture.md)…[05](./05-knowledge-model.md) и в [спеках](../20-specs/README.md). Состояние на 2026-09-30.

## 1. Контекст: кто с чем общается

```mermaid
flowchart LR
  L[Учащийся] -->|iOS / Android / web| C[Клиент Expo]
  A[Куратор] -->|/admin, экран графа| B
  C -->|HTTPS: sync, graph, auth| B[Backend FastAPI]
  B --> P[(PostgreSQL)]
  B -->|OpenAI-совместимый протокол| M[LLM-провайдер]
  B -.->|Ф4| S[STT / TTS]
  C --> Q[(SQLite на устройстве)]
```

Клиент работает без сети только с SQLite. Backend — единственный, кто говорит с LLM (инвариант №2).

## 2. Функциональные области

```mermaid
flowchart TB
  subgraph Клиент
    UX[Экраны: Сегодня, Курс, Граф, Повторение, Плейсмент, Профиль]
    DISP[ActivityDispatcher + реестр модулей]
    FEAT[Рендереры: письмо, вспомнить, материал, теория, вопрос]
    ENG[shared/engine: Activity, FSRS, порты]
    SYNC[Sync + очередь jobs]
    LS[(LocalStore SQLite)]
    UX --> DISP --> FEAT --> ENG
    ENG --> LS
    SYNC --> LS
  end
  subgraph Backend
    AUTH[Auth + роли]
    SYNCB[/sync, /jobs/]
    GW[AI-gateway + рубрики]
    KG[Модуль knowledge: граф, задания, плейсмент, курс]
    SRSB[SRS + error-log]
    ADM[Админка]
  end
  SYNC --> SYNCB --> GW
  SYNCB --> SRSB
  UX --> KG --> GW
  ADM --> KG
```

| Область | Что делает | Спека | Клиент | Backend |
|---|---|---|---|---|
| Движок Activity | Единый примитив; диспетчеризация по `type` | [SPEC-01](../20-specs/SPEC-01-activity-engine.md) | `shared/engine`, `widgets/module-registry` | `modules/*`, *(цель: реестр модулей)* |
| Аккаунт | Регистрация, вход, восстановление, роли | [SPEC-02](../20-specs/SPEC-02-auth-and-roles.md) | `pages/auth`, `entities/session` | `core/routers/auth.py` |
| Sync и очередь | Push/pull, отложенные AI-задачи | [SPEC-03](../20-specs/SPEC-03-sync-and-jobs.md) | `shared/api/sync-*`, `job-queue` | `core/routers/sync.py`, `core/jobs.py` |
| AI-gateway | Вызовы LLM, рубрики, заглушка | [SPEC-04](../20-specs/SPEC-04-ai-gateway-and-rubrics.md) | — | `core/ai_gateway` |
| Повторение | FSRS, error-log | [SPEC-05](../20-specs/SPEC-05-srs-and-error-log.md) | `pages/review`, `scheduler` | `core/srs.py` |
| Письмо | Эссе IELTS с оценкой | [SPEC-06](../20-specs/SPEC-06-writing.md) | `features/ielts-writing` | `modules/languages` |
| ML-трек | Материал, вспомнить | [SPEC-07](../20-specs/SPEC-07-ml-track.md) | `features/material-read`, `concept-recall` | `modules/ml` |
| Граф знаний | Канон + персональный слой | [SPEC-08](../20-specs/SPEC-08-knowledge-graph.md) | `features/graph-editor` | `modules/knowledge` |
| Задания | Из теории узла | [SPEC-09](../20-specs/SPEC-09-assessment.md) | — | `knowledge/assessment*.py` |
| Плейсмент | Карта освоенности | [SPEC-10](../20-specs/SPEC-10-placement.md) | `features/placement` | `knowledge/{mastery,placement}.py` |
| Курс | Путь и петля освоения | [SPEC-11](../20-specs/SPEC-11-course-and-study.md) | `features/course`, `concept-study` | `knowledge/{course,study}.py` |
| Опыт учащегося | Онбординг, «Сегодня», словари | [SPEC-12](../20-specs/SPEC-12-learner-experience.md) | `pages/*`, `shared/config/design.ts` | — |
| Администрирование | Панель, CLI, курирование | [SPEC-13](../20-specs/SPEC-13-admin-and-curation.md) | `graph-curation` | `core/admin.py`, `scripts/` |
| Речь, рецепция | Будущее | [SPEC-14](../20-specs/SPEC-14-speaking.md), [15](../20-specs/SPEC-15-reception-drills.md) | — | — |
| Расширение, релиз | Будущее | [SPEC-16](../20-specs/SPEC-16-learning-expansion.md), [17](../20-specs/SPEC-17-platform-and-release.md) | — | — |

## 3. Сквозной поток данных

```mermaid
sequenceDiagram
  participant У as Учащийся
  participant К as Клиент (SQLite)
  participant Б as Backend
  participant М as LLM
  У->>К: пишет эссе (без сети)
  К->>К: response + job pending, черновой сигнал
  К->>Б: sync push (при сети)
  Б->>М: оценка по рубрике (tool call)
  М-->>Б: Grade
  Б->>Б: response.grade, карточки error-log, job done
  К->>Б: sync pull
  Б-->>К: разбор + новые карточки
  У->>К: повторяет карточки (FSRS, офлайн)
```

## 4. Петля освоения узла

```mermaid
flowchart LR
  N[Узел графа: теория] --> T[Задание из теории]
  T --> O[Ответ]
  O --> R[(response)]
  R --> Mst[Освоенность: бета-модель]
  Mst --> F[Граница знаний]
  F --> Course[Курс: следующий шаг]
  Course --> N
  O -->|score < 0.6| Card[Карточка FSRS по узлу]
  Card --> Mst
```

## 5. Где что проверяется

Каталог проверок — [10-requirements/verification.md](../10-requirements/verification.md). Порядок задач — [50-plans/priorities.md](../50-plans/priorities.md).
