# SPEC-01 — Движок Activity и модульная система

| | |
|---|---|
| **Статус** | `implemented` (2026-09-30) |
| **Требования** | FR-ENG-01..06, NFR-03, NFR-05 |
| **Фаза** | [Ф0](../50-plans/phase-0-foundation.md) · [Ф3](../50-plans/phase-3-hardening.md) |
| **Решения** | [ADR-0003](../40-adr/0003-client-expo-fsd.md), [ADR-0011](../40-adr/0011-knowledge-as-module-cow.md) |
| **Обновлено** | 2026-09-30 |

## Назначение

Дать один примитив, **Activity**, через который проходит любое учебное взаимодействие, и способ подключать предметы модулями, не трогая ядро ([vision](../00-product/vision.md#педагогическое-обоснование)).

## Поведение

1. При старте клиента composition root собирает манифесты всех модулей и регистрирует их в реестре ядра.
2. Экран получает Activity и просит у реестра рендерер по `activity.type`. Если рендерера нет, показывается плейсхолдер `NotImplementedActivity`.
3. Название и подсказку типа экран берёт из реестра (`getActivityTitle`). Незнакомый тип отображается своим слугом: это заметно и лучше пустоты.
4. Рендерер завершает Activity вызовом `onComplete(draft)`. Запись ответа в лог и постановку задач делает не ядро, а feature через `shared/api`.
5. Если тип объявил офлайн-грейдер, feature вызывает его сразу и показывает черновой сигнал.
6. На backend модуль подключается через `core.modules` ([ADR-0019](../40-adr/0019-backend-module-registry.md)): роутер, рубрики, типы оцениваемых jobs, провижининг по предмету и представления админки. Ядро вызывает их по реестру, не зная имён модулей.

## Контракт

**Клиент** (`learningFront/src/shared/engine`):

```ts
interface Activity { id; userId; module; type; connectivity: 'offline'|'online'; payload; createdAt; dueAt? }
interface ActivityTypeDef { type; title; hint?; connectivity; payloadSchema; producesErrorLog? }
interface ModuleManifest { id; title; activityTypes; renderers; localGraders?; importers?; schedulerConfig? }
class ModuleRegistry {
  registerModule(m)              // ошибка при повторе модуля или коллизии type
  getRenderer(type) / getLocalGrader(type)
  getActivityType(type) / getActivityTitle(type) / getModuleIdForType(type)
}
```

**Зарегистрированные модули и типы** (источник — `entities/module/*.ts`):

| Модуль | Типы | Рендерер есть |
|---|---|---|
| `languages` | `ielts_writing_task2`, `ielts_writing_task1`, `reading_drill`, `listening_drill`, `speaking_response`, `vocab_srs` | только `ielts_writing_task2` |
| `ml` | `material_read`, `concept_recall`, `concept_srs`, `code_task` | `material_read`, `concept_recall` |
| `knowledge` | `concept_study`, `concept_contrast`, `concept_apply`, `srs` | `concept_study`, `concept_contrast`, `concept_apply` |

Повторения (`vocab_srs`, `concept_srs`, `srs`) проходятся экраном повторения по карточкам, а не рендерером Activity. См. [SPEC-05](./SPEC-05-srs-and-error-log.md#расхождения).

**Backend** (`core/modules.py`, `FR-ENG-06`):

```python
class BackendModule:            # всё необязательное, по умолчанию no-op
    id: str
    def router(self) -> APIRouter | None
    def rubrics(self) -> list[dict]                    # сидятся в `rubric` при старте API
    def grade_jobs(self) -> dict[str, str]             # job.type → модуль карточек error-log
    def provision(self, session, user_id, subject, now) -> None  # стартовый контент под предмет
    def admin_views(self) -> list
```

Подключённые модули — `INSTALLED_MODULES` (по умолчанию `modules.languages,modules.ml,modules.knowledge`); каждый пакет экспортирует `backend`.

## Критерии приёмки

| AC | Критерий | Проверка | Статус |
|---|---|---|---|
| AC-01.1 | Регистрация модуля с уже занятым `type` бросает ошибку с именами обоих модулей | test `registry.test.ts` | 🟢 |
| AC-01.2 | Повторная регистрация модуля бросает ошибку | test `registry.test.ts` | 🟢 |
| AC-01.3 | Диспетчеризация по `type` работает без ветвлений по имени модуля | test + grep `if.*module ===` по `shared/engine` пуст | 🟢 |
| AC-01.4 | Тип без рендерера открывается плейсхолдером | live web | 🟢 |
| AC-01.5 | `shared/engine` не импортирует React и не содержит доменных строк | grep (см. NFR-03) | 🟢 |
| AC-01.6 | `learningBack/core` не импортирует `modules.*` и не содержит имён модулей | test `test_core_does_not_know_modules` + скрипт инвариантов | 🟢 |
| AC-01.7 | Новый модуль backend подключается строкой в `INSTALLED_MODULES` | test `test_modules.py` | 🟢 |

## Код

- Клиент: `src/shared/engine/{types,module,ports,scheduler}`, `src/entities/module/{languages,ml,knowledge}.ts` (метаданные), `src/widgets/module-registry/index.ts` (сборка манифестов с рендерерами, `initModuleRegistry`), `src/widgets/activity-dispatcher`, `src/shared/ui/not-implemented-activity.tsx`, провайдер реестра `src/shared/lib/module-registry-context.tsx`.
- Backend: `core/modules.py` (контракт и реестр), `modules/{languages,ml,knowledge}/__init__.py` (объект `backend`), потребители реестра — `core/app.py`, `core/jobs.py`, `core/admin.py`, `core/routers/auth.py`. `scripts/seed.py` вне `core/` и может импортировать модули напрямую.

## Расхождения

Расхождений нет.


## Журнал

| Дата | Изменение |
|---|---|
| 2026-09-30 | Создана из 02-logical §1, §3 и кода; зафиксировано нарушение NFR-03 на backend |
| 2026-09-30 | P3-INV-01: реестр модулей backend, нарушение закрыто (ADR-0019) |
