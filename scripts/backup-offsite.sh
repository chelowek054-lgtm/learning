#!/usr/bin/env bash
# Вынос свежих копий базы и объектов за пределы сервера (T-0031). Запуск на сервере из cron после backup-db.sh:
#
#   OFFSITE_TARGET=user@backup-host:/srv/praxis-backups scripts/backup-offsite.sh
#
# Копирует каталог .data/backups по rsync/SSH; ничего не удаляет на стороне получателя.
set -euo pipefail
cd "$(dirname "$0")/.."
: "${OFFSITE_TARGET:?Задайте OFFSITE_TARGET=user@host:/каталог}"
rsync -az --partial .data/backups/ "$OFFSITE_TARGET/"
echo "✓ копии отправлены в $OFFSITE_TARGET"
