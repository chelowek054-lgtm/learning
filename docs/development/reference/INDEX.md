# Справочник проекта

Сгенерировано приложением, не править: источник — справки (S-…) и подтверждённая карта кода (docs/13-reference.md).

## Модули проекта
Что уже написано. Прежде чем заводить новое — посмотри, нет ли такого.

### Инфраструктура — Выкладка, резервные копии и проверки процесса — зона девопса; с сервером связана через общие ресурсы и связи, а не вложенностью.
### Клиент — Приложение на Expo (iOS, Android, веб), собранное по FSD: то, с чем работает учащийся и куратор.
### Сервер — Бэкенд на FastAPI: API, предметные модули, ядро, схема базы и тесты — всё, что выкладывается как сервер.

## Внешние решения
- **RouterAI Jev: модель решений вместо текста** (S-0001, api, 2026-10-07) — Jev — не чат-модель: получает state и questions с заранее известными вариантами и возвращает вероятности/выбор/оценку вместо текста; тарифицируются только входные токены → docs/development/reference/S-0001-routerai-jev-model-resheniy-vmesto-teksta.md
- **RouterAI: плагины (web, file-parser) и мультимодальные входы** (S-0002, api, 2026-10-07) — Плагины web/file-parser включаются массивом plugins без предварительной настройки; мультимодальные входы (изображения, PDF, аудио, видео) идут через /chat/completions типами контента в messages[].content → docs/development/reference/S-0002-routerai-plaginy-web-file-parser-i-multimodalnye.md
- **RouterAI: выбор провайдера, @-синтаксис, список endpoint-ов** (S-0003, api, 2026-10-07) — Объект provider (order/only/ignore/allow_fallbacks/country) и @-синтаксис в строке model управляют маршрутизацией запроса к конкретному провайдеру модели; GET /models/{author}/{model}/endpoints отдаёт список провайдеров с ценами и лимитами → docs/development/reference/S-0003-routerai-vybor-provaydera-sintaksis-spisok-endpo.md
- **RouterAI: параметры генерации (sampling parameters)** (S-0004, api, 2026-10-07) — RouterAI принимает единый набор параметров генерации (temperature, top_p, top_k, penalties, max_tokens, response_format, tools, verbosity и др.) и передаёт провайдер-специфичные как есть → docs/development/reference/S-0004-routerai-parametry-generacii-sampling-parameters.md
- **RouterAI: режимы обработки flex и priority (service tiers)** (S-0005, api, 2026-10-07) — Поле service_tier на уровне запроса меняет цену и скорость без смены модели: flex дешевле и медленнее (строгий, ошибка если недоступен), priority дороже и быстрее (мягко деградирует до default) → docs/development/reference/S-0005-routerai-rezhimy-obrabotki-flex-i-priority-servi.md

## Приёмы и данные
- **docdd-console: группы карты и легенда уровня** (S-0006, technique, 2026-10-12) — Три уровня (обзор-группы/группа/элемент) со свёрнутыми связями-счётчиками между группами; легенда собирается из тех же правил отрисовки, что красят схему → docs/development/reference/S-0006-docdd-console-gruppy-karty-i-legenda-urovnya.md
- **InteractMedNew: граф по слоям с пучком связей и легендой-переключателем** (S-0007, technique, 2026-10-12) — Узлы по столбцам-слоям, связи пучком дуг только между соседними столбцами, легенда — переключатели вида связи с цветом и числом, щелчок закрепляет фокус → docs/development/reference/S-0007-interactmednew-graf-po-sloyam-s-puchkom-svyazey.md
