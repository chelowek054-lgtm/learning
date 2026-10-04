---
id: T-0043
type: task
title: Ошибки речи становятся карточками error-log
status: in_review
change: feature
created: 2026-09-30
updated: 2026-10-04
links:
  implements: [R-0023]
  depends_on: [T-0042]
  verified_by: [V-0063]
  affects: [M-0003, M-0011]
---

# Ошибки речи становятся карточками error-log

После разбора speaking ошибки попадают в SRS тем же путём, что ошибки письма (source='error_log').

## Журнал

- 2026-09-30 · заведена из docs/inbox/speaking.md · приложение
- 2026-10-04 · взята в работу, сделана: ошибки речи идут в SRS общим путём оценки (source=error_log), проверено цепочкой запись → расшифровка → оценка → карточки (learningBack PR 34) · claude
- 2026-10-04 · на проверку: тест проходит; на устройстве не проверялось · claude
