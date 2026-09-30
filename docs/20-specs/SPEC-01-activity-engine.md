# SPEC-01 — Движок Activity и модульная система

| | |
|---|---|
| **Статус** | `partial` — клиент готов; backend-ядро знает имена модулей |
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
6. На backend модуль подключает свой роутер, рубрики, генераторы и хуки провижининга через контракт. Ядро backend вызывает их по реестру, не зная имён модулей.

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

**Backend** (целевой контракт, `FR-ENG-06`):

```python
class ModuleBackend(Protocol):
    id: str
    router: APIRouter | None
    def rubrics(self) -> list[dict]: ...                 # сидятся в `rubric`
    def job_handlers(self) -> dict[str, JobHandler]: ... # job.type → обработчик
    def provision(self, session, user, subject) -> None: ...  # стартовый контент под предмет
```

## Критерии приёмки

| AC | Критерий | Проверка | Статус |
|---|---|---|---|
| AC-01.1 | Регистрация модуля с уже занятым `type` бросает ошибку с именами обоих модулей | test `registry.test.ts` | 🟢 |
| AC-01.2 | Повторная регистрация модуля бросает ошибку | test `registry.test.ts` | 🟢 |
| AC-01.3 | Диспетчеризация по `type` работает без ветвлений по имени модуля | test + grep `if.*module ===` по `shared/engine` пуст | 🟢 |
| AC-01.4 | Тип без рендерера открывается плейсхолдером | live web | 🟢 |
| AC-01.5 | `shared/engine` не импортирует React и не содержит доменных строк | grep (см. NFR-03) | 🟢 |
| AC-01.6 | `learningBack/core` не импортирует `modules.*` и не содержит имён модулей | grep (см. NFR-03) | 🔴 |
| AC-01.7 | Новый модуль backend подключается одной строкой регистрации | ревью + тест реестра backend | ⚪ |

## Код

- Клиент: `src/shared/engine/{types,module,ports,scheduler}`, `src/entities/module/{languages,ml,knowledge}.ts` (метаданные), `src/widgets/module-registry/index.ts` (сборка манифестов с рендерерами, `initModuleRegistry`), `src/widgets/activity-dispatcher`, `src/shared/ui/not-implemented-activity.tsx`, провайдер реестра `src/shared/lib/module-registry-context.tsx`.
- Backend: `modules/{languages,ml}/__init__.py` (метаданные `ACTIVITY_TYPES`), `modules/knowledge/__init__.py` (роутер). Подключение — прямыми импортами в `core/app.py`, `core/provisioning.py`, `core/jobs.py`, `scripts/seed.py`.

## Расхождения

| Расхождение | Задача |
|---|---|
| `core/provisioning.py` импортирует `modules.languages.generators` | [P3-INV-01](../50-plans/phase-3-hardening.md) |
| `core/jobs.py` держит карту `grade_writing → languages`, `grade_concept → ml` | P3-INV-01 |
| `core/app.py` импортирует роутер `modules.knowledge` напрямую | P3-INV-01 (регистрация через реестр модулей) |
| В [30-architecture/04](../30-architecture/04-frontend-fsd.md) сборка реестра описана в `entities/module/registry.ts`, в коде — `widgets/module-registry` | исправлено в документе 2026-09-30 |

## Журнал

| Дата | Изменение |
|---|---|
| 2026-09-30 | Создана из 02-logical §1, §3 и кода; зафиксировано нарушение NFR-03 на backend |
