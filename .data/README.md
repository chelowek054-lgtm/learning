# .data — данные контейнеров (суперпроект)

Локальное хранилище персистентных данных всех сервисов `docker-compose` (bind-mount). **Вне git** (см. корневой `.gitignore`).

- `.data/postgres/` — том Postgres (`/var/lib/postgresql/data`).
- Будущие сервисы (Redis, MinIO и т.п.) кладут данные сюда же в свои подпапки.

Docker создаёт подпапки автоматически при `docker compose up`. Сброс БД:

```bash
docker compose down
rm -rf .data/postgres
```
