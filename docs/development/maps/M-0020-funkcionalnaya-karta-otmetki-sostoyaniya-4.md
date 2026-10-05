---
id: M-0020
type: map
title: 'Функциональная карта: отметки состояния (4)'
status: approved
created: 2026-10-04
updated: 2026-10-04
---

# Функциональная карта: отметки состояния (4)

Черновик: составлен моделью, не подтверждён. Прочитайте, поправьте руками
то, что модель не поняла, и подтвердите — до этого карта на общую картину
не влияет.

```docdd-functional
{
  "added": {
    "capabilities": [
      {
        "id": "method-contract",
        "title": "Единый контракт способа изучения",
        "parent": "method-switch",
        "status": "implemented",
        "note": "core/methods.py задаёт контракт StudyMethod (способ, шаг, тип активности, офлайн); несколько модулей (srs, mnemonic, ml, languages, knowledge) объявляют свои способы через него, выбор идёт через for_purpose и профиль пользователя."
      },
      {
        "id": "mastery-evidence",
        "title": "Свидетельство об освоении, не зависящее от способа",
        "parent": "method-switch",
        "status": "implemented",
        "note": "core/evidence.py — единый формат Evidence (узел, ступень Блума, результат 0..1, источник), dispatch передаёт его модулям, которые хранят освоенность; подключено к API и нескольким способам."
      },
      {
        "id": "domain-levels",
        "title": "Уровень примитивности вычисляется из графа областей",
        "parent": "domain-graph",
        "status": "implemented",
        "note": "modules/knowledge/domains.py: levels() считает уровень как глубину в графе областей (самый длинный путь от опоры), не назначается руками; отдано через API /graph/domains и /graph/domains/{key}/chain."
      },
      {
        "id": "path-volume-preview",
        "title": "Предпросмотр объёма пути и выбор полного или интуитивного варианта",
        "parent": "goal-intake",
        "status": "implemented",
        "note": "modules/knowledge/path_volume.py считает полный и интуитивный варианты объёма пути (области, понятия) до построения графа; есть эндпоинт /graph/goal/{goal}/volume и экран в goal-intake на фронте (V-0090 подтверждён)."
      }
    ]
  }
}
```

## Журнал

- 2026-10-04 · заведена черновиком · модель
- 2026-10-04 · на подтверждение · architect
- 2026-10-04 · подтверждён · architect
