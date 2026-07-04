# Praxis

Персональная адаптивная обучающая платформа (iOS/Android) для изучения языков (TOEFL/IELTS) и технологий (ML/программирование).

📚 **Документация — единый источник правды:** [`docs/`](./docs/README.md)
🗺️ **План разработки:** [`docs/plans/`](./docs/plans/README.md) · текущая фаза — [Фаза 0 (каркас)](./docs/plans/phase-0-foundation.md)

---

## Структура репозитория (монорепо)

```
apps/            мобильный клиент (Expo/React Native) — переезжает сюда в WS6
services/api/    backend (FastAPI, Python, uv)
packages/
  core-engine/       доменно-независимое ядро (Activity, реестр, FSRS, порты)
  module-languages/  модуль «Языки» (TOEFL/IELTS)
  module-ml/         модуль «Программирование/ML»
  ui-kit/            общие UI-компоненты
docs/            архитектура, планы, (позже) business и deploy
```

- **Frontend / packages** — npm workspaces (Node ≥ 20).
- **Backend** — отдельное Python-окружение на **uv**, связано с клиентом только по HTTP.

## Быстрый старт

### TypeScript workspace (packages)

```bash
npm install          # установить зависимости всех workspace-пакетов
npm run typecheck    # проверка типов по всем пакетам
npm run lint         # ESLint
npm test             # юнит-тесты (vitest)
```

### Backend (появляется в WS2)

```bash
cd services/api
uv sync
uv run uvicorn core.app:app --reload   # http://localhost:8000/docs
# или: docker compose up
```

### Мобильный клиент (появляется в WS6)

```bash
cd apps/mobile
npx expo start
```

## Секреты

Скопировать [`.env.example`](./.env.example) → `.env` (в git не коммитится). Ключ Claude — **только** на backend, никогда в клиенте (инвариант №2).

## Соглашения

Инварианты системы и архитектурные принципы — в [docs/README.md](./docs/README.md#инварианты-системы-не-нарушать-при-реализации). Реализация ведётся строго по планам в [docs/plans/](./docs/plans/README.md).
