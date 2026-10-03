---
id: V-0090
type: verification
title: Предпросмотр объёма пути перед построением
status: draft
created: 2026-10-03
updated: 2026-10-03
kind: manual
command: 'cd learningBack && uv run pytest tests/test_path_volume.py -q && cd ../learningFront && npx vitest run src/features/goal-intake'
links:
  verifies: [R-0038]
---

# Предпросмотр объёма пути перед построением

Чем проверяется: после подтверждения цели экран показывает список базовых областей и число понятий до начала построения графа; выбор интуитивного варианта исключает часть базовых областей, и граф строится без них.

## Журнал

- 2026-10-03 · заведена из docs/inbox/foundation-levels.md · приложение
- 2026-10-03 · подключена команда прогона: test_path_volume (полный и интуитивный объём, оценка до построения, области без графа, выбор не нужен при цели «понять») и dialog.test; экран на устройстве не проверялся · claude
