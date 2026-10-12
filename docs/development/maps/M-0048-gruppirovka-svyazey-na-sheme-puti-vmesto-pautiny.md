---
id: M-0048
type: map
title: Группировка связей на схеме пути вместо «паутины»
status: approved
created: 2026-10-12
updated: 2026-10-12
---

# Группировка связей на схеме пути вместо «паутины»

На реальном графе (6 этапов, ~30 понятий, десятки связей) схема читается плохо: связи между колонками сливаются в сетку. Нужен обзор уровнями (этапы-блоки → раскрытый этап → выбранное понятие), а не всегда полный рисунок.

```docdd-functional
{
  "added": {
    "capabilities": [
      {
        "id": "scheme-grouping",
        "title": "Группировка связей по этапам на схеме пути",
        "parent": "graph-map-view",
        "status": "not_implemented",
        "note": "Сейчас все связи рисуются всегда; на крупном графе это нечитаемо",
        "priority": "should",
        "horizon": "next"
      },
      {
        "id": "scheme-overview-stages",
        "title": "Обзор по этапам со свёрнутыми связями",
        "parent": "scheme-grouping"
      },
      {
        "id": "scheme-stage-expand",
        "title": "Раскрытие этапа на месте",
        "parent": "scheme-grouping"
      }
    ]
  }
}
```

## Журнал

- 2026-10-12 · заведена из docs/inbox/skhema-puti-gruppirovka-svyazey-vmesto-pautiny.md · приложение
- 2026-10-12 · на подтверждение · architect
- 2026-10-12 · подтверждён · architect
