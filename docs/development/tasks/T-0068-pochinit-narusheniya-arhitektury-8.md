---
id: T-0068
type: task
title: 'Починить нарушения архитектуры: 8'
status: backlog
change: fix
created: 2026-10-05
updated: 2026-10-05
links:
  affects: [M-0004]
---

# Починить нарушения архитектуры: 8

Нарушения правил архитектуры из точной проверки по подтверждённой карте кода
(docs/07-maps.md, «Модули и публичный вход»). Правится код, а не карты: после правки
импорты в картах нужно переописать.

- `arch_entry_bypassed` — `learningBack/core/app.py:14`: Импорт `learningBack/core/routers/auth.py` идёт в глубину модуля `learningBack/core/routers`, в обход его входа (__init__.py). Обращайтесь к входу `learningBack/core/routers` — или опубликуйте нужное через него.
- `arch_entry_bypassed` — `learningBack/core/app.py:14`: Импорт `learningBack/core/routers/content.py` идёт в глубину модуля `learningBack/core/routers`, в обход его входа (__init__.py). Обращайтесь к входу `learningBack/core/routers` — или опубликуйте нужное через него.
- `arch_entry_bypassed` — `learningBack/core/app.py:14`: Импорт `learningBack/core/routers/jobs.py` идёт в глубину модуля `learningBack/core/routers`, в обход его входа (__init__.py). Обращайтесь к входу `learningBack/core/routers` — или опубликуйте нужное через него.
- `arch_entry_bypassed` — `learningBack/core/app.py:14`: Импорт `learningBack/core/routers/sync.py` идёт в глубину модуля `learningBack/core/routers`, в обход его входа (__init__.py). Обращайтесь к входу `learningBack/core/routers` — или опубликуйте нужное через него.
- `arch_entry_bypassed` — `learningBack/core/app.py:19`: Импорт `learningBack/core/routers/usage.py` идёт в глубину модуля `learningBack/core/routers`, в обход его входа (__init__.py). Обращайтесь к входу `learningBack/core/routers` — или опубликуйте нужное через него.
- `arch_parent_import` — `learningBack/core/ai_gateway/__init__.py:12`: Подмодуль `learningBack/core/ai_gateway` импортирует своего родителя `learningBack/core` (`learningBack/core/config.py`). Родитель собирает детей, а не наоборот: нужное детям вынесите в общий модуль ниже.
- `arch_parent_import` — `learningBack/core/ai_gateway/__init__.py:13`: Подмодуль `learningBack/core/ai_gateway` импортирует своего родителя `learningBack/core` (`learningBack/core/models.py`). Родитель собирает детей, а не наоборот: нужное детям вынесите в общий модуль ниже.
- `arch_parent_import` — `learningBack/core/ai_gateway/base.py:5`: Подмодуль `learningBack/core/ai_gateway` импортирует своего родителя `learningBack/core` (`learningBack/core/models.py`). Родитель собирает детей, а не наоборот: нужное детям вынесите в общий модуль ниже.

## Журнал

- 2026-10-05 · заведена · приложение
