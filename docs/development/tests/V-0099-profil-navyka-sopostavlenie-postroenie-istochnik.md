---
id: V-0099
type: verification
title: Профиль навыка, сопоставление, построение, источники и полнота
status: approved
created: 2026-10-07
updated: 2026-10-07
kind: manual
links:
  verifies: [R-0048, R-0049, R-0050, R-0051, R-0052, R-0053, R-0054]
---

# Профиль навыка, сопоставление, построение, источники и полнота

Чем проверяется: метки этапа и уровня сохраняются и отдаются; профиль чистится от мусора и ограничивается размером по уровню; области сопоставляются по близости с тремя исходами; граф строится скелетом со связями и не дублирует существующее; для новой области ставятся поиск и разбор источников; отчёт полноты называет недостающее.
Команда: `cd learningBack && uv run pytest tests/test_stage_level.py tests/test_skill_profile.py tests/test_profile_match.py tests/test_profile_build.py tests/test_profile_sources.py tests/test_profile_coverage.py -q && cd ../learningFront && npx vitest run src/features/skill-profile`

## Журнал

- 2026-10-07 · заведена · приложение
- 2026-10-07 · на подтверждение · architect
- 2026-10-07 · подтверждён · architect
- 2026-10-07 · проверяет и требования R-0049…R-0054, заведённые консолью по той же заметке; их собственные проверки V-0100…V-0105 ручные, команда одна — здесь · claude
