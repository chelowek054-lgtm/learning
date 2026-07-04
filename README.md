# Praxis

Персональная адаптивная обучающая платформа (iOS/Android) для изучения языков (TOEFL/IELTS) и технологий (ML/программирование).

Этот репозиторий — **git-суперпроект**: документация + два сабмодуля.

```
learning/                 ← суперпроект (docs — источник правды)
├── docs/                 архитектура, планы, (позже) business и deploy
├── learningFront/        сабмодуль: клиент (Expo/React Native, FSD)
└── learningBack/         сабмодуль: backend (FastAPI, Python, uv)
```

- **learningFront** — фронтенд по **Feature-Sliced Design**. Доменно-независимое ядро — в `src/shared/engine`. См. [docs/architecture/04-frontend-fsd.md](./docs/architecture/04-frontend-fsd.md).
- **learningBack** — backend, связан с клиентом только по HTTP. Ключ Claude — только здесь (инвариант №2).

## Документация — единый источник правды

- 📚 [`docs/`](./docs/README.md) — обзор, инварианты, глоссарий
- 🏛️ [`docs/architecture/`](./docs/architecture/README.md) — архитектурный, логический, функциональный, FSD-планы
- 🗺️ [`docs/plans/`](./docs/plans/README.md) — план разработки · текущая фаза: [Фаза 0](./docs/plans/phase-0-foundation.md)

## Клонирование (с сабмодулями)

```bash
git clone --recurse-submodules <url>
# или после обычного клона:
git submodule update --init --recursive
```

## Запуск

```bash
# Клиент
cd learningFront && npm install && npx expo start

# Backend (появляется в WS2)
cd learningBack && uv sync && uv run uvicorn core.app:app --reload
```
