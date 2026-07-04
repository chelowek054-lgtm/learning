# 04 — Фронтенд: архитектура Feature-Sliced Design (FSD)

Организация клиента (`learningFront/`) по методологии **Feature-Sliced Design**. Дополняет [01 — Архитектуру](./01-architecture.md) (стек) и [02 — Логический план](./02-logical.md) (движок, модули). Backend — отдельный репозиторий (`learningBack/`).

> **Контекст репозитория:** корень `D:\work\learning` — git-суперпроект с сабмодулями `learningFront` (этот документ) и `learningBack` (FastAPI). `docs/` живёт в суперпроекте.

---

## 1. Почему FSD ложится на Praxis

FSD делит фронтенд на **слои** (по ответственности) → **слайсы** (по бизнес-области) → **сегменты** (`ui`/`model`/`lib`/`api`/`config`). Слои импортируют строго вниз.

Ключевое совпадение с архитектурой Praxis: **доменно-независимое ядро** ([инвариант №3](../README.md#инварианты-системы-не-нарушать-при-реализации)) — это в точности нижний слой FSD **`shared`**, который по определению не содержит бизнес-специфики. Модули-домены (languages, ml) распределяются по верхним слоям как слайсы.

---

## 2. Слои (сверху вниз)

| Слой | Ответственность в Praxis | Может импортировать |
|---|---|---|
| **`app`** | Инициализация, провайдеры, роутинг (expo-router), **композиционный корень**: регистрация модулей в реестре ядра | всё ниже |
| **`pages`** | Экраны (screens): Home, Review, Writing, Material… | widgets → shared |
| **`widgets`** | Составные блоки: `ActivityDispatcher` (рендер по `activity.type`), `TodayQueue` | features → shared |
| **`features`** | Взаимодействия по типам Activity: `vocab-review`, `ielts-writing`, `concept-recall`, `code-task` | entities → shared |
| **`entities`** | Бизнес-сущности: `activity`, `srs-card`, `response`, `module` | shared |
| **`shared`** | Переиспользуемое без бизнес-специфики: **`engine`** (ядро), `ui`, `api`, `config`, `lib` | — (низ) |

Правило импортов: слой видит только слои **ниже** и «нейтральные» сегменты своего уровня по правилам FSD. Апорт вверх запрещён.

---

## 3. Где живёт доменно-независимое ядро

Бывший `core-engine` целиком переезжает в **`src/shared/engine`**:

```
src/shared/engine/
  types/       Activity, Connectivity, Grade, Response
  module/      ModuleManifest, ModuleRegistry (табличный lookup)
  scheduler/   обёртка ts-fsrs (Scheduler)
  ports/       LocalStore, SyncClient, JobQueue (интерфейсы)
  index.ts     публичный API ядра
```

**Инвариант №3 в терминах FSD:** `shared/engine` не импортирует из `entities`/`features`/… и не содержит доменных строк (`languages`/`ml`/`ielts`…). Проверяется grep'ом (см. DoD в плане).

---

## 4. Куда ложатся домены (languages / ml)

Praxis-«модуль» — это бандл: типы Activity + рендереры + (на бэке) рубрики. В FSD он **не отдельная папка-плагин**, а распределяется:

- **Рендерер типа Activity** → слайс в `features` (напр. `features/ielts-writing`, `features/vocab-review`, `features/concept-recall`).
- **Сущности** (`activity`, `srs-card`, `response`) → `entities`.
- **Манифест модуля** (какие типы Activity в него входят, их `connectivity`, `producesErrorLog`) → **композиционный корень** `src/app/modules/{languages,ml}.ts`: манифест импортирует рендереры-features и регистрирует их в реестре ядра.

> ⚠️ **Важно (expo-router):** каталог `src/app` сканируется expo-router через `require.context` и **исполняет** все файлы внутри. Поэтому не-роутовый код (метаданные модулей, их сборка, тесты) НЕ должен лежать под `src/app` — иначе expo-router ругается на «missing default export», а тест-файл падает (`vitest` вне раннера). Метаданные и сборка манифестов вынесены в `entities/module`; вызов регистрации — в роут-обёртке `_layout.tsx`.

```
src/entities/module/       // НЕ сканируется роутером
  languages.ts   // чистые метаданные типов Activity (без RN)
  ml.ts
  registry.ts    // buildManifest (метаданные + рендерер) + initModuleRegistry/getModuleRegistry
  index.ts

src/app/_layout.tsx        // composition root: getModuleRegistry() → <ModuleRegistryProvider>
```

Реестр читается вниз через контекст `shared/lib` (pages/widgets НЕ импортируют app и entities напрямую для этого). Так «плагинность» модулей выражена явно, а ядро остаётся доменно-независимым.

---

## 5. Согласование с expo-router

expo-router использует файловый роутинг из `src/app`. Ключевое правило: **`src/app` содержит ТОЛЬКО роуты** (роутер исполняет всё внутри — см. предупреждение в §4).

- Файлы-роуты (`src/app/index.tsx`, `explore.tsx`, `_layout.tsx`) — **тонкие**: импортируют экран из `src/pages` и рендерят; `_layout.tsx` дополнительно создаёт реестр и оборачивает провайдером.
- Любой не-роутовый код (метаданные, сборка, провайдеры-хелперы, тесты) — вне `src/app` (в `entities`, `shared`, `widgets`).

```
src/app/index.tsx
  → export { HomeScreen as default } from '@/pages/home'
```

Экран (`pages/home`) — уже FSD-компонент, роут не содержит логики.

---

## 6. Путь-алиасы и границы

- Алиас `@/*` → `src/*` (уже настроен в `tsconfig.json`). Импорты: `@/shared/engine`, `@/entities/activity`, `@/features/vocab-review`.
- Публичный API слайса — через его `index.ts` (barrel). Импорт «вглубь» слайса запрещён правилами FSD.
- Контроль границ: линт (кандидат — `steiger` / `eslint-plugin-boundaries`) добавляется отдельной задачей; на старте — grep-проверка ядра + код-ревью.

---

## 7. Итоговая структура `learningFront`

```
learningFront/
  src/
    app/            FSD app-слой + expo-router роуты + composition root (регистрация модулей)
    pages/          экраны
    widgets/        ActivityDispatcher, TodayQueue
    features/       по типам Activity (vocab-review, ielts-writing, concept-recall, …)
    entities/       activity, srs-card, response, module
    shared/
      engine/       доменно-независимое ядро (ex core-engine)
      ui/           ui-kit
      api/          http-клиент, sync-адаптер
      config/       env, константы
      lib/          утилиты
    components/      ← существующие компоненты шаблона (постепенно раскладываются по shared/ui, widgets)
    constants/, hooks/  ← аналогично мигрируют в shared
  app.json, tsconfig.json, package.json
```

Существующий scaffold (`components/`, `constants/`, `hooks/`) мигрирует в FSD-слои постепенно, не ломая приложение.

---

## Связанные документы

- [01 — Архитектура](./01-architecture.md) · [02 — Логический план](./02-logical.md) · [03 — Функциональный план](./03-functional.md)
- План работ — [Фаза 0](../plans/phase-0-foundation.md)
