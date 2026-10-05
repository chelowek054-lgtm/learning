---
id: V-0091
type: verification
title: 'Сверка с общими практиками: SOLID и DRY'
status: approved
created: 2026-10-05
updated: 2026-10-05
kind: manual
---

# Сверка с общими практиками: SOLID и DRY

Проверено по A-0004 (SOLID и DRY). Исключены из рассмотрения `.venv`, `node_modules`, `.claude/worktrees`.

## Расхождения

**DRY — повтор правила «неразбираемый id → 404» в backend.** Блок
```python
try:
    node_uuid = uuid.UUID(node_id)
except ValueError:
    raise HTTPException(status.HTTP_404_NOT_FOUND, "узел не найден") from None
```
буквально повторён минимум шесть раз: `learningBack/modules/knowledge/router.py:83-86, 395-398, 684-687` и `learningBack/core/routers/content.py:51-54, 107-110`. При этом в `learningBack/modules/languages/api.py:24` то же правило уже вынесено в приватный хелпер `_id()`. Поменять правило (например, код ответа) — значит править шесть мест вместо одного. Стоит завести общий хелпер (например, в `core/deps.py`) и применить его во всех перечисленных местах, по образцу `languages/api.py`.

**S — `learningBack/modules/knowledge/router.py` (907 строк) держит несколько причин для изменения в одном файле.** Модуль уже выносит логически отдельные API в собственные роутеры (`cross_links_api.py`, `domains_api.py`), но сам `router.py` продолжает смешивать секции с разными поводами для правки: курирование канона (`/canon/*`), диалог постановки цели (`/goal/*`), генерация заданий (`/nodes/*/assessment`), адаптивный плейсмент (`/placement/*`), прохождение курса (`/course/*`), приём материалов (`/materials/*`), персональный слой узлов/рёбер. Это расходится с паттерном, который модуль сам же применяет к соседним частям — стоит разнести эти секции по отдельным роутерам так же, как уже сделано для cross-links и domains.

**DRY (умеренно) — формулировка правила оценки продублирована в промптах рубрик.** Правило «overall — среднее, округлённое до 0.5» и фраза о разборе ошибок с улучшенным образцом повторены буквально в 4+ рубриках: `learningBack/modules/languages/rubrics.py` (IELTS_WRITING_TASK2, IELTS_WRITING_TASK1, TOEFL_WRITING_INDEPENDENT, TOEFL_WRITING_INTEGRATED) и `learningBack/modules/ml/rubrics.py` (CONCEPT_CHECK, ML_CODE_REVIEW). Оговорка: это текст промпта, а не код, и шкалы у рубрик разные по существу (0-9 vs 0-5) — полное обобщение не всегда оправдано, находка не критична.

## Соответствует без оговорок

- **D (инверсия зависимостей)** — `core/ai_gateway/base.AIGateway` как протокол, `get_ai_gateway()` отдаёт конкретную реализацию только по признаку наличия ключа; на фронтенде `shared/engine/ports/*` — чистые интерфейсы, `shared/api/*` — их реализации без обратных конкретных импортов.
- **O (открыт/закрыт)** — диспетчеризация активностей на фронте через реестр (`useModuleRegistry().getRenderer`), на backend через `core/modules.py` (`job_handler_for`, `grade_job_modules`, `study_methods`) — новый модуль добавляется без правки ядра.
- **L (подстановка Лисков)** — `BackendModule` в `core/modules.py` даёт безопасные no-op по умолчанию, `validate_modules()` явно проверяет соответствие заявленного и реализованного.
- **I (разделение интерфейсов)** — `BackendModule` формально широкий, но методы no-op по умолчанию, а `manifest.provides` + `actual_provides()` заставляет декларировать реально поддерживаемое — осознанная компенсация, не нарушение.
- **DRY в остальном** — общая логика (FSRS-хелперы, errors→card, AI-схемы) вынесена в общие модули, предметные данные не копируются между backend и frontend без причины.

## Журнал

- 2026-10-05 · заведена · приложение
- 2026-10-05 · на подтверждение · architect
- 2026-10-05 · подтверждён · architect
