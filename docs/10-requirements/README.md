# 10 — Требования

Раздел отвечает на вопрос **«что»** должна делать система, без описания того, как это сделано.

| Документ | Содержание |
|---|---|
| [functional.md](./functional.md) | Функциональные требования `FR-<ГРУППА>-<NN>` с критериями приёмки |
| [non-functional.md](./non-functional.md) | Инварианты системы и нефункциональные требования `NFR-<NN>` |
| [verification.md](./verification.md) | Каталог проверок: команды, прогоны, матрица «требование → чем проверяется» |

## Формат

Требование описывается строкой таблицы:

| Поле | Смысл |
|---|---|
| **ID** | `FR-<ГРУППА>-<NN>`. Номер не переиспользуется, даже если требование отклонено |
| **Требование** | Что система делает, с точки зрения пользователя или системы. Формулировка «Система …» / «Учащийся может …» |
| **Приёмка** | Наблюдаемый результат, по которому требование считается выполненным |
| **Спека** | Какая спека его раскрывает |
| **Статус** | `implemented` · `partial` · `accepted` (принято, не начато) · `proposed` · `deferred` · `rejected` |

Статус требования **выводится** из статусов задач плана. Последняя сверка с кодом: **2026-09-30** (сабмодули `learningBack@09b3aca`, `learningFront@77b25ca`).

## Группы

| Группа | Область | Спека |
|---|---|---|
| `ENG` | Движок Activity и модульная система | [SPEC-01](../20-specs/SPEC-01-activity-engine.md) |
| `AUTH` | Аккаунт, вход, восстановление, роли | [SPEC-02](../20-specs/SPEC-02-auth-and-roles.md) |
| `SYNC` | Offline-first хранение, синхронизация, очередь задач | [SPEC-03](../20-specs/SPEC-03-sync-and-jobs.md) |
| `AI` | AI-gateway, рубрики, стоимость | [SPEC-04](../20-specs/SPEC-04-ai-gateway-and-rubrics.md) |
| `SRS` | Интервальное повторение и error-log | [SPEC-05](../20-specs/SPEC-05-srs-and-error-log.md) |
| `WRT` | Письменная продукция (IELTS/TOEFL) | [SPEC-06](../20-specs/SPEC-06-writing.md) |
| `ML` | Трек технологий: материал, вспоминание, код, импорт | [SPEC-07](../20-specs/SPEC-07-ml-track.md), [SPEC-16](../20-specs/SPEC-16-learning-expansion.md) |
| `KG` | Граф знаний: канон, персональный слой, рост, курирование | [SPEC-08](../20-specs/SPEC-08-knowledge-graph.md) |
| `ASM` | Задания из теории узла | [SPEC-09](../20-specs/SPEC-09-assessment.md) |
| `PLC` | Адаптивный плейсмент | [SPEC-10](../20-specs/SPEC-10-placement.md) |
| `CRS` | Курс и прохождение шага | [SPEC-11](../20-specs/SPEC-11-course-and-study.md) |
| `UX` | Опыт учащегося: онбординг, «Сегодня», язык интерфейса | [SPEC-12](../20-specs/SPEC-12-learner-experience.md) |
| `ADM` | Администрирование и курирование | [SPEC-13](../20-specs/SPEC-13-admin-and-curation.md) |
| `SPK` | Речь (Speaking) | [SPEC-14](../20-specs/SPEC-14-speaking.md) |
| `RCP` | Рецепция: чтение и аудирование | [SPEC-15](../20-specs/SPEC-15-reception-drills.md) |
| `PRD` | Продукт и релиз | [SPEC-17](../20-specs/SPEC-17-platform-and-release.md) |
