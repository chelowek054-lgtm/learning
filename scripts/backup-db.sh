#!/usr/bin/env bash
# Резервная копия базы Praxis (T-0031, R-0020). Запуск из корня суперпроекта, по расписанию (cron):
#
#   scripts/backup-db.sh [каталог] [сколько дней хранить]
#
# Кладёт сжатый дамп praxis-ГГГГММДД-ЧЧММСС.sql.gz в каталог (по умолчанию ./.data/backups) и
# удаляет дампы старше срока (по умолчанию 14 дней). Дамп без проверки восстановления — не
# бэкап: после копии запускается scripts/restore-check.sh.
set -euo pipefail
cd "$(dirname "$0")/.."

DIR="${1:-.data/backups}"
KEEP_DAYS="${2:-14}"
COMPOSE="${COMPOSE:-docker compose}"
PGUSER="${POSTGRES_USER:-praxis}"
PGDB="${POSTGRES_DB:-praxis}"

mkdir -p "$DIR"
STAMP="$(date +%Y%m%d-%H%M%S)"
FILE="$DIR/praxis-$STAMP.sql.gz"

# --clean --if-exists: дамп можно накатить на непустую базу; --no-owner: не зависит от имени роли.
$COMPOSE exec -T postgres pg_dump -U "$PGUSER" -d "$PGDB" --clean --if-exists --no-owner | gzip > "$FILE"

if [ ! -s "$FILE" ] || [ "$(gzip -dc "$FILE" | head -c 1 | wc -c)" -eq 0 ]; then
  rm -f "$FILE"
  echo "Резервная копия пуста — отмена" >&2
  exit 1
fi

find "$DIR" -name 'praxis-*.sql.gz' -mtime "+$KEEP_DAYS" -delete
echo "$FILE"
