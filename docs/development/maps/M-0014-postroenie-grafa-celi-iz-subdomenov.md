---
id: M-0014
type: map
title: Построение графа цели из субдоменов
status: draft
created: 2026-10-02
updated: 2026-10-02
---

# Построение графа цели из субдоменов

Сейчас граф области строится одним запросом (до 20 узлов). Крупная цель требует разбиения на субдомены, каждый из которых строится отдельным запросом как примитивная область, а итоговый граф — их объединение со связями-предпосылками через границы субдоменов.

```docdd-functional
{
  "added": {
    "capabilities": [
      {
        "id": "goal-subdomain-split",
        "title": "Разбиение цели на субдомены",
        "parent": "base-graph-build",
        "status": "not_implemented",
        "note": "Граф строится одним запросом; разбиения на субдомены и правки человеком нет"
      },
      {
        "id": "goal-tree-assembly",
        "title": "Сборка графа цели из субдоменов",
        "parent": "base-graph-build",
        "status": "not_implemented"
      }
    ],
    "relations": [
      {
        "from": "goal-subdomain-split",
        "to": "goal-tree-assembly",
        "type": "feeds",
        "summary": "разбиение определяет, какие субдомены строятся и затем собираются в граф цели"
      },
      {
        "from": "goal-tree-assembly",
        "to": "graph-reuse",
        "type": "uses",
        "summary": "уже построенный субдомен не строится заново, а подключается через переиспользование"
      }
    ]
  }
}
```

## Журнал

- 2026-10-02 · заведена из docs/inbox/base-graph-subdomains.md · приложение
