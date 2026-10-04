---
id: V-0063
type: verification
title: Оценка по ielts_speaking
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
command: 'cd learningBack && uv run pytest tests/test_speaking.py -q'
links:
  verifies: [R-0023, T-0040, T-0041, T-0042, T-0043, T-0044, T-0049]
---

# Оценка по ielts_speaking

Unit, pytest: `будет: cd learningBack && uv run pytest tests/test_speaking_rubric.py -q`. Доказывает: четыре критерия и band; у Pronunciation есть пометка об ограничении оценки по тексту; ошибки речи становятся карточками. Пройдена, когда тест написан вместе с T-0042 и T-0043. Состояние: ещё нет — появится вместе с задачей.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-speaking.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-04 · подключена команда прогона: test_speaking (метрики темпа и пауз, рубрика ielts_speaking с пометкой о произношении, ошибки речи → карточки error_log); оценка настоящей моделью не проверялась · claude
