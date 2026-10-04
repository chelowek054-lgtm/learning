---
id: V-0062
type: verification
title: Распознавание на заглушке
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
command: 'cd learningBack && uv run pytest tests/test_speaking.py -q'
links:
  verifies: [R-0023, T-0040, T-0041, T-0042, T-0043, T-0044, T-0049]
---

# Распознавание на заглушке

Integration, pytest: `будет: cd learningBack && uv run pytest tests/test_transcribe_job.py -q`. Доказывает: без ключа STT job transcribe работает на MockSTT; пустая или тихая запись даёт понятную ошибку, а не пустую оценку. Пройдена, когда тест написан вместе с T-0041. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-speaking.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-04 · подключена команда прогона: test_speaking (заглушка STT, тихая/пустая/слишком длинная запись — понятная ошибка, а не пустая оценка); настоящий провайдер не подключён · claude
