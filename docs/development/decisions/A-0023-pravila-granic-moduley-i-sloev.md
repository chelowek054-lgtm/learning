---
id: A-0023
type: decision
title: Правила границ модулей и слоёв
status: draft
created: 2026-10-05
updated: 2026-10-05
---

# Правила границ модулей и слоёв

Зачем: платформа с подключаемыми модулями (A-0020) держится на границах — модуль можно заменить, не ломая остальных, только если другие обращаются к нему через вход. Эти границы нужно проверять, а не помнить. До сих пор правила жили секцией `architecture` в манифесте — без причины и без источника; теперь они записаны решением и действуют, пока оно подтверждено.

Что решили:
- **Бэкенд.** Слои сверху вниз: `api → modules → core`, импорт только вниз, соседние модули обращаются друг к другу через вход. `modules/*` независимы — между ними только через родителя или `core`. `modules/*` закрыты (снаружи только `__init__.py`), `core` — открытая библиотека платформы: публичны все её подмодули, приватное помечено `_`. `core` технический, доменных модулей не знает.
- **Клиент.** FSD: `app → pages → widgets → features → entities → shared`, импорт только вниз, срезы одного слоя друг друга не знают. У `app` и `shared` срезов нет, их сегменты друг друга видят. UI-кит `shared/ui` не знает про `shared/api` и `shared/engine`.
- **Вне проверки.** Тесты, скрипты и миграции — по общей конвенции консоли.

Отвергнуто: единый вход-реэкспорт на весь `core` (файл-«бог», циклы, медленный старт, пользы для границ нет); оставить как есть (шум из ложных предупреждений приучает их не читать).

Последствия: `core/routers` и `core/app.py` — сборка приложения, а не ядро платформы, — переезжают в слой `api`; межмодульные импорты идут через вход; `shared/ui` перестаёт зависеть от `shared/api` и `shared/engine`; глубокий импорт `shared/lib/quiz` заменяется нормальным входом. Каждое такое исправление — отдельная задача.

```docdd-rules
{
  "shared": ["learningBack/core", "learningFront/src/shared"],
  "modules": [
    { "path": "learningBack/modules/*", "entry": "closed" },
    { "path": "learningBack/core", "entry": "open" }
  ],
  "independent": ["learningBack/modules/*"],
  "layers": [
    {
      "root": "learningFront/src",
      "order": ["app", "pages", "widgets", "features", "entities", "shared"],
      "slices": "isolated",
      "unsliced": ["app", "shared"]
    },
    { "root": "learningBack", "order": ["api", "modules", "core"], "slices": "via-entry" }
  ],
  "forbidden": [
    {
      "from": "learningFront/src/shared/ui",
      "to": ["learningFront/src/shared/api", "learningFront/src/shared/engine"],
      "why": "UI-кит не знает про API и движок"
    }
  ]
}
```

## Журнал

- 2026-10-05 · заведена черновиком · модель
