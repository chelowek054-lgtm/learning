# Карта возможностей системы

## Зачем

Показать, из каких возможностей состоит Praxis и как они опираются друг на друга: ядро движка, аккаунт, синхронизация, AI, повторение, граф знаний и то, что строится над ним.

## Возможности (родитель → потомки)

- Движок Activity и модули — основа для всего остального.
  - Аккаунт и роли.
  - Синхронизация и очередь задач.
  - AI-gateway, рубрики, стоимость.
  - Интервальное повторение и журнал ошибок.
  - Письмо IELTS, ML-трек, речь, чтение и аудирование.
  - Граф знаний.
    - Задания из теории узла.
    - Адаптивный плейсмент.
    - Курс и прохождение шага.
  - Опыт учащегося и администрирование.
  - Платформа и релиз.

## Где что в коде

- Движок Activity: Единый примитив; диспетчеризация по `type`. Клиент: `shared/engine`, `widgets/module-registry`. Backend: `modules/*`, *(цель: реестр модулей)*.
- Аккаунт: Регистрация, вход, восстановление, роли. Клиент: `pages/auth`, `entities/session`. Backend: `core/routers/auth.py`.
- Sync и очередь: Push/pull, отложенные AI-задачи. Клиент: `shared/api/sync-*`, `job-queue`. Backend: `core/routers/sync.py`, `core/jobs.py`.
- AI-gateway: Вызовы LLM, рубрики, заглушка. Клиент: —. Backend: `core/ai_gateway`.
- Повторение: FSRS, error-log. Клиент: `pages/review`, `scheduler`. Backend: `core/srs.py`.
- Письмо: Эссе IELTS с оценкой. Клиент: `features/ielts-writing`. Backend: `modules/languages`.
- ML-трек: Материал, вспомнить. Клиент: `features/material-read`, `concept-recall`. Backend: `modules/ml`.
- Граф знаний: Канон + персональный слой. Клиент: `features/graph-editor`. Backend: `modules/knowledge`.
- Задания: Из теории узла. Клиент: —. Backend: `knowledge/assessment*.py`.
- Плейсмент: Карта освоенности. Клиент: `features/placement`. Backend: `knowledge/{mastery,placement}.py`.
- Курс: Путь и петля освоения. Клиент: `features/course`, `concept-study`. Backend: `knowledge/{course,study}.py`.
- Опыт учащегося: Онбординг, «Сегодня», словари. Клиент: `pages/*`, `shared/config/design.ts`. Backend: —.
- Администрирование: Панель, CLI, курирование. Клиент: `graph-curation`. Backend: `core/admin.py`, `scripts/`.
- Речь, рецепция: Будущее. Клиент: —. Backend: —.
- Расширение, релиз: Будущее. Клиент: —. Backend: —.

## Не выяснено

Не выяснено: нужна ли отдельная функциональная карта по возможностям, или достаточно карты кодовой базы.
