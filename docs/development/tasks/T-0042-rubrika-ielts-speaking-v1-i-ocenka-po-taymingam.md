---
id: T-0042
type: task
title: Рубрика ielts_speaking v1 и оценка по таймингам
status: done
change: feature
created: 2026-09-30
updated: 2026-10-04
links:
  implements: [R-0023]
  decided_by: [A-0009]
  depends_on: [T-0041]
  verified_by: [V-0063]
  affects: [M-0003, M-0011]
---

# Рубрика ielts_speaking v1 и оценка по таймингам

Рубрика (Fluency & Coherence, Lexical Resource, Grammatical Range & Accuracy, Pronunciation → band 0–9), регистрация через реестр модулей. Оценка: текст + тайминги слов (темп, паузы) → Grade; у Pronunciation — пометка ограничения. features/speaking: задание → запись → отправка → разбор.

## Журнал

- 2026-09-30 · заведена из docs/inbox/speaking.md · приложение
- 2026-10-01 · добавлены связи вне приложения: decided_by A-0009 · claude
- 2026-10-04 · взята в работу: рубрика ielts_speaking v1, метрики темпа и пауз, оценка jobом grade_speaking с пометкой о произношении (learningBack PR 34); экран features/speaking в клиенте не сделан · claude
- 2026-10-04 · сделан экран speaking_response в клиенте (learningFront PR 22); рубрика и оценка — learningBack PR 34 · claude
- 2026-10-04 · на проверку: тесты проходят; оценка настоящей моделью и разбор на экране не проверялись; разбор пока виден как оценка в журнале ответов, отдельного вида нет · claude
- 2026-10-04 · готова · проверки подтверждены и прошли в отчёте 2026-10-04 · claude
