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

```
src/app/
  modules/
    languages.ts   // ModuleManifest: собирает features языков → registry
    ml.ts          // ModuleManifest: собирает features ml → registry
  providers/       // store, query, theme
  _layout.tsx      // роут-обёртка: провайдеры + вызов регистрации модулей
```

Так «плагинность» модулей выражена явно и в единственном месте (composition root), а ядро остаётся доменно-независимым.

---

## 5. Согласование с expo-router

expo-router использует файловый роутинг из `src/app`. В Praxis этот каталог совмещает **FSD-слой `app`** и **роуты**:

- Файлы-роуты (`src/app/index.tsx`, `explore.tsx`, `_layout.tsx`) — **тонкие**: только импортируют экран из `src/pages` и рендерят.
- Вся инициализация (провайдеры, регистрация модулей) — в `src/app/_layout.tsx` + `src/app/{providers,modules}`.

```
src/app/index.tsx
  → import { HomeScreen } from '@/pages/home'
  → export default HomeScreen
```

Экран (`pages/home`) — уже FSD-компонент, роут не содержит логики. Это стандартный приём Expo + FSD (один каталог `src/app` под роутинг и app-слой), без второго «app».

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
