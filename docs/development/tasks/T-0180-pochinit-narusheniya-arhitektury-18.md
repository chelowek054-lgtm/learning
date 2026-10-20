---
id: T-0180
type: task
title: 'Починить нарушения архитектуры: 18'
status: in_review
change: fix
created: 2026-10-20
updated: 2026-10-20
links:
  implements: [R-0040]
  affects: [M-0052, M-0053]
---

# Починить нарушения архитектуры: 18

Нарушения правил архитектуры из точной проверки по подтверждённой карте кода
(docs/07-maps.md, «Модули и публичный вход»). Правится код, а не карты: после правки
импорты в картах нужно переописать.

- `arch_entry_bypassed` — `learningFront/src/features/course/model/draft.ts:3`: Импорт `learningFront/src/shared/i18n/translate.ts` идёт в глубину модуля `learningFront/src/shared/i18n`, в обход его входа (`index.ts, index.tsx, index.js`). Обращайтесь к входу `learningFront/src/shared/i18n` — или опубликуйте нужное через него. Правило: встроенный минимум.
- `arch_entry_bypassed` — `learningFront/src/features/course/model/group-steps.ts:3`: Импорт `learningFront/src/shared/i18n/translate.ts` идёт в глубину модуля `learningFront/src/shared/i18n`, в обход его входа (`index.ts, index.tsx, index.js`). Обращайтесь к входу `learningFront/src/shared/i18n` — или опубликуйте нужное через него. Правило: встроенный минимум.
- `arch_entry_bypassed` — `learningFront/src/features/goal-intake/model/steps.ts:1`: Импорт `learningFront/src/shared/i18n/translate.ts` идёт в глубину модуля `learningFront/src/shared/i18n`, в обход его входа (`index.ts, index.tsx, index.js`). Обращайтесь к входу `learningFront/src/shared/i18n` — или опубликуйте нужное через него. Правило: встроенный минимум.
- `arch_entry_bypassed` — `learningFront/src/features/graph-editor/model/build-progress.ts:4`: Импорт `learningFront/src/shared/i18n/translate.ts` идёт в глубину модуля `learningFront/src/shared/i18n`, в обход его входа (`index.ts, index.tsx, index.js`). Обращайтесь к входу `learningFront/src/shared/i18n` — или опубликуйте нужное через него. Правило: встроенный минимум.
- `arch_entry_bypassed` — `learningFront/src/features/graph-editor/model/legend.ts:5`: Импорт `learningFront/src/shared/i18n/translate.ts` идёт в глубину модуля `learningFront/src/shared/i18n`, в обход его входа (`index.ts, index.tsx, index.js`). Обращайтесь к входу `learningFront/src/shared/i18n` — или опубликуйте нужное через него. Правило: встроенный минимум.
- `arch_entry_bypassed` — `learningFront/src/features/graph-editor/model/overview.ts:21`: Импорт `learningFront/src/shared/i18n/translate.ts` идёт в глубину модуля `learningFront/src/shared/i18n`, в обход его входа (`index.ts, index.tsx, index.js`). Обращайтесь к входу `learningFront/src/shared/i18n` — или опубликуйте нужное через него. Правило: встроенный минимум.
- `arch_entry_bypassed` — `learningFront/src/features/graph-editor/model/scheme.ts:4`: Импорт `learningFront/src/shared/i18n/translate.ts` идёт в глубину модуля `learningFront/src/shared/i18n`, в обход его входа (`index.ts, index.tsx, index.js`). Обращайтесь к входу `learningFront/src/shared/i18n` — или опубликуйте нужное через него. Правило: встроенный минимум.
- `arch_entry_bypassed` — `learningFront/src/features/graph-editor/model/stage-groups.ts:3`: Импорт `learningFront/src/shared/i18n/translate.ts` идёт в глубину модуля `learningFront/src/shared/i18n`, в обход его входа (`index.ts, index.tsx, index.js`). Обращайтесь к входу `learningFront/src/shared/i18n` — или опубликуйте нужное через него. Правило: встроенный минимум.
- `arch_entry_bypassed` — `learningFront/src/features/prior-test/model/report.ts:3`: Импорт `learningFront/src/shared/i18n/translate.ts` идёт в глубину модуля `learningFront/src/shared/i18n`, в обход его входа (`index.ts, index.tsx, index.js`). Обращайтесь к входу `learningFront/src/shared/i18n` — или опубликуйте нужное через него. Правило: встроенный минимум.
- `arch_entry_bypassed` — `learningFront/src/features/push-settings/model/push-model.ts:3`: Импорт `learningFront/src/shared/i18n/translate.ts` идёт в глубину модуля `learningFront/src/shared/i18n`, в обход его входа (`index.ts, index.tsx, index.js`). Обращайтесь к входу `learningFront/src/shared/i18n` — или опубликуйте нужное через него. Правило: встроенный минимум.
- `arch_entry_bypassed` — `learningFront/src/features/skill-profile/model/profile-model.ts:9`: Импорт `learningFront/src/shared/i18n/translate.ts` идёт в глубину модуля `learningFront/src/shared/i18n`, в обход его входа (`index.ts, index.tsx, index.js`). Обращайтесь к входу `learningFront/src/shared/i18n` — или опубликуйте нужное через него. Правило: встроенный минимум.
- `arch_entry_bypassed` — `learningFront/src/features/sources/model/gaps-model.ts:3`: Импорт `learningFront/src/shared/i18n/translate.ts` идёт в глубину модуля `learningFront/src/shared/i18n`, в обход его входа (`index.ts, index.tsx, index.js`). Обращайтесь к входу `learningFront/src/shared/i18n` — или опубликуйте нужное через него. Правило: встроенный минимум.
- `arch_entry_bypassed` — `learningFront/src/features/sources/model/sources-model.ts:3`: Импорт `learningFront/src/shared/i18n/translate.ts` идёт в глубину модуля `learningFront/src/shared/i18n`, в обход его входа (`index.ts, index.tsx, index.js`). Обращайтесь к входу `learningFront/src/shared/i18n` — или опубликуйте нужное через него. Правило: встроенный минимум.
- `arch_entry_bypassed` — `learningFront/src/shared/api/error-text.ts:2`: Импорт `learningFront/src/shared/i18n/translate.ts` идёт в глубину модуля `learningFront/src/shared/i18n`, в обход его входа (`index.ts, index.tsx, index.js`). Обращайтесь к входу `learningFront/src/shared/i18n` — или опубликуйте нужное через него. Правило: встроенный минимум.
- `arch_entry_bypassed` — `learningFront/src/shared/api/error-text.ts:3`: Импорт `learningFront/src/shared/i18n/ru.ts` идёт в глубину модуля `learningFront/src/shared/i18n`, в обход его входа (`index.ts, index.tsx, index.js`). Обращайтесь к входу `learningFront/src/shared/i18n` — или опубликуйте нужное через него. Правило: встроенный минимум.
- `arch_entry_bypassed` — `learningFront/src/shared/api/sources-api.ts:6`: Импорт `learningFront/src/shared/i18n/translate.ts` идёт в глубину модуля `learningFront/src/shared/i18n`, в обход его входа (`index.ts, index.tsx, index.js`). Обращайтесь к входу `learningFront/src/shared/i18n` — или опубликуйте нужное через него. Правило: встроенный минимум.
- `arch_entry_bypassed` — `learningFront/src/shared/ui/theme-mode.ts:3`: Импорт `learningFront/src/shared/i18n/translate.ts` идёт в глубину модуля `learningFront/src/shared/i18n`, в обход его входа (`index.ts, index.tsx, index.js`). Обращайтесь к входу `learningFront/src/shared/i18n` — или опубликуйте нужное через него. Правило: встроенный минимум.
- `arch_entry_bypassed` — `learningFront/src/test-setup.ts:1`: Импорт `learningFront/src/shared/i18n/translate.ts` идёт в глубину модуля `learningFront/src/shared/i18n`, в обход его входа (`index.ts, index.tsx, index.js`). Обращайтесь к входу `learningFront/src/shared/i18n` — или опубликуйте нужное через него. Правило: встроенный минимум.

## Журнал

- 2026-10-20 · заведена · приложение
- 2026-10-20 · в работе · claude
- 2026-10-20 · на проверке · claude: чистая часть перевода вынесена в модуль shared/i18n-core со своим входом (learningFront #60, #61), свидетельства карт обновлены (learning #65); проверка архитектуры консоли — 0 нарушений, 0 ошибок карт
