---
id: M-0046
type: map
title: 'Схема пути во весь экран: плашка узла и подсветка выбранного'
status: approved
created: 2026-10-12
updated: 2026-10-12
---

# Схема пути во весь экран: плашка узла и подсветка выбранного

Со слов заметки: на «Пути» в режимах «Дерево» и «Карта» схема читается плохо — рёбра идут диагоналями через узлы, заголовки обрезаны, окно схемы маленькое. Три новые возможности внутри уже существующей `graph-map-view`.

```docdd-functional
{
  "added": {
    "capabilities": [
      {
        "id": "scheme-fullscreen",
        "title": "Полноэкранный режим схемы пути",
        "parent": "graph-map-view",
        "status": "not_implemented",
        "note": "Кнопки «во весь экран» нет, окно схемы зажато между поиском, фильтрами и масштабом"
      },
      {
        "id": "scheme-node-focus",
        "title": "Плашка узла и подсветка выбранного пути",
        "parent": "graph-map-view",
        "status": "not_implemented",
        "note": "Нет ни плашки с описанием узла, ни приглушения остального графа при выборе"
      },
      {
        "id": "scheme-edge-routing",
        "title": "Читаемые рёбра и подписи на схеме пути",
        "parent": "graph-map-view",
        "status": "partial",
        "note": "Рёбра есть, но рисуются прямыми диагоналями поверх узлов; заголовки колонок и имена узлов обрезаются"
      }
    ],
    "relations": [
      {
        "from": "scheme-node-focus",
        "to": "scheme-fullscreen",
        "type": "depends",
        "summary": "плашка и подсветка появляются в полноэкранном режиме схемы"
      }
    ]
  }
}
```

## Журнал

- 2026-10-12 · заведена из docs/inbox/shema-puti-na-ves-ekran-i-podsvetka-vybrannogo.md · приложение
- 2026-10-12 · на подтверждение · architect
- 2026-10-12 · подтверждён · architect
