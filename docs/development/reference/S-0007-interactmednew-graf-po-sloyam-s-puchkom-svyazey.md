---
id: S-0007
type: reference
title: 'InteractMedNew: граф по слоям с пучком связей и легендой-переключателем'
status: approved
created: 2026-10-12
updated: 2026-10-12
summary: Узлы по столбцам-слоям, связи пучком дуг только между соседними столбцами, легенда — переключатели вида связи с цветом и числом, щелчок закрепляет фокус
kind: technique
source: 'InteractMedNew: code/frontend/app/widgets/graph-overview/ui/GraphOverview.vue'
fetched: 2026-10-12
---

# InteractMedNew: граф по слоям с пучком связей и легендой-переключателем

Раскладка от переключателей видов связи не меняется (узлы не прыгают). Щелчок по узлу закрепляет фокус — выделены его связи, рядом панель со связями списком; щелчок по пустому месту снимает. Групп и свёртки связей нет — только слои и фокус.

## Журнал

- 2026-10-12 · заведена из docs/inbox/legenda-vezde-gde-est-graf.md, docs/inbox/skhema-puti-gruppirovka-svyazey-vmesto-pautiny.md · приложение
- 2026-10-12 · на подтверждение · architect
- 2026-10-12 · подтверждён · architect
