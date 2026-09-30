# Praxis

Персональная адаптивная обучающая платформа (iOS/Android) для изучения языков (TOEFL/IELTS) и технологий (ML/программирование).

Этот репозиторий — **git-суперпроект**: документация + два сабмодуля.

```
learning/                 ← суперпроект (docs — источник правды)
├── docs/                 DocDD: продукт, требования, спеки, архитектура, ADR, планы
├── learningFront/        сабмодуль: клиент (Expo/React Native, FSD)
└── learningBack/         сабмодуль: backend (FastAPI, Python, uv)
```

- **learningFront** — фронтенд по **Feature-Sliced Design**. Доменно-независимое ядро — в `src/shared/engine`. См. [docs/architecture/04-frontend-fsd.md](./docs/30-architecture/04-frontend-fsd.md).
- **learningBack** — backend, связан с клиентом только по HTTP. Ключ LLM-провайдера — только здесь (инвариант №2).

## Где проект сейчас

**[`ROADMAP.md`](./ROADMAP.md)** — дашборд и журнал вех. План реализации — **[`docs/50-plans/`](./docs/50-plans/README.md)**. Документация ведётся по **DocDD** ([правила](./docs/README.md#правила-docdd)).

| Фаза | Статус |
|---|---|
| [Ф0 — Каркас](./docs/50-plans/phase-0-foundation.md) | ✅ 34/34 |
| [Ф1 — MVP](./docs/50-plans/phase-1-mvp.md) | 🟡 31/33 (2 переоткрыты → Ф3) |
| [Ф2 — Модель знаний](./docs/50-plans/phase-2-knowledge-model.md) | ✅ 30/30 |
| [Ф3 — Укрепление](./docs/50-plans/phase-3-hardening.md) | ⚪ **следующая** · 1/26 |
| [Ф4 — Речь и рецепция](./docs/50-plans/phase-4-speech-reception.md) | ⚪ 0/27 |
| [Ф5 — Расширение обучения](./docs/50-plans/phase-5-learning-expansion.md) | ⚪ 0/16 |
| [Ф6 — Продукт и релиз](./docs/50-plans/phase-6-product-release.md) | ⚪ 0/18 |

## Документация — единый источник правды

- 📚 [`docs/`](./docs/README.md) — карта и правила DocDD
- 🎯 [`00-product`](./docs/00-product/README.md) · 📋 [`10-requirements`](./docs/10-requirements/README.md) · 📐 [`20-specs`](./docs/20-specs/README.md) · 🏛️ [`30-architecture`](./docs/30-architecture/README.md) · ⚖️ [`40-adr`](./docs/40-adr/README.md) · 🗂️ [`50-plans`](./docs/50-plans/README.md)
- 🔁 [`docs/HANDOFF.md`](./docs/HANDOFF.md) — запуск и грабли среды

## Клонирование (с сабмодулями)

```bash
git clone --recurse-submodules <url>
# или после обычного клона:
git submodule update --init --recursive
```

## Запуск

**Весь стенд (Postgres + API) через docker-compose из корня** — оркестрация всех сервисов живёт здесь (масштабируется на будущие микросервисы/внешние сервисы). Данные контейнеров — в `./.data` (вне git).

```bash
cp .env.example .env          # ЕДИНСТВЕННЫЙ .env проекта: стенд, backend и клиент
docker compose up --build     # Postgres + миграции + API + pgAdmin
```

| Сервис | Адрес | Примечание |
|---|---|---|
| API (Swagger) | http://localhost:8000/docs | |
| Postgres | `localhost:5432` | креды из `.env` |
| pgAdmin | http://localhost:5050 | без логина; подключение «Praxis (docker)» уже прописано, пароль спросит при первом коннекте |
| Админка | http://localhost:8000/admin | вход только для администратора — завести его нужно самому (см. ниже) |

pgAdmin — dev-инструмент, приложение с ним не связано. Поднять стенд без него: `docker compose up postgres api`.

**Администратор** заводится из CLI, как `manage.py createsuperuser` в Django:

```bash
docker compose exec api uv run python -m scripts.createsuperuser
```

Спросит email и пароль. Существующий пользователь при этом повышается до администратора. Без интерактива — `--noinput --email … --password …` (или `PRAXIS_SUPERUSER_EMAIL`/`PRAXIS_SUPERUSER_PASSWORD`).

Отдельные сервисы для разработки:

```bash
# Клиент (Expo)
cd learningFront && npm install && npx expo start

# Только backend локально (Postgres можно поднять из корня: docker compose up -d postgres)
cd learningBack && uv sync && uv run uvicorn core.app:app --reload
```

> **DevOps-раскладка:** `docker-compose.yml`, `.env.example`, `./.data` — в корне (оркестрация). `Dockerfile` каждого сервиса — в его сабмодуле (build-рецепт). Так добавление нового сервиса = новый блок в корневом compose + свой Dockerfile в его репозитории.
