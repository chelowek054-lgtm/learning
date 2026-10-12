---
id: T-0159
type: task
title: Сборка теории узла из утверждений со ссылками
status: in_review
change: feature
created: 2026-10-12
updated: 2026-10-13
links:
  implements: [R-0075]
  depends_on: [T-0149]
  verified_by: [V-0134]
  affects: [M-0051]
---

# Сборка теории узла из утверждений со ссылками

Замена построения по требованию в modules/knowledge/theory.py на сборку из принятых утверждений по хешу набора; разделы со ссылками на утверждения.

## Журнал

- 2026-10-12 · заведена из docs/inbox/sborka-uzla-i-bank-zadaniy-bez-llm-pri-obuchenii.md · приложение
- 2026-10-13 · learningBack#80 (влит), CI main зелёный: node_compile.py — один запрос на понятие по хэшу набора утверждений, разделы со ссылками на утверждения, предложение без ссылки отбрасывается · claude
