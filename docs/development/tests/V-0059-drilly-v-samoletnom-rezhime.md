---
id: V-0059
type: verification
title: Дриллы в самолётном режиме
status: approved
created: 2026-09-30
updated: 2026-10-01
kind: manual
command: 'cd learningFront && npx vitest run src/features/listening-drill src/features/reading-drill'
links:
  verifies: [R-0022, T-0036, T-0037, T-0038, T-0039]
---

# Дриллы в самолётном режиме

Manual. Доказывает: reading и listening проходятся без сети, аудио играет из кэша, лимит прослушиваний соблюдается, при отсутствии аудио — объяснение. Пройдена, когда пройдена руками на устройстве (задачи T-0036, T-0037). Открытый вопрос: число прослушиваний — экзаменационная строгость против пользы для обучения.

## Журнал

- 2026-09-30 · заведена из docs/inbox/checks-reception-drills.md · приложение
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-01 · возвращён в черновик · architect
- 2026-10-01 · на подтверждение · architect
- 2026-10-01 · подтверждён · architect
- 2026-10-04 · подключена команда прогона: listening-model.test (лимит прослушиваний, причины отказа слушать, разбор задания) и reading-model.test; режим полёта на устройстве не проверялся · claude
