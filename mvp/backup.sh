#!/usr/bin/env bash
# Copies all data (chats, accounts, spend log, generated files) to ./backups/<date>. Run daily with cron; copy the folder off the server.
set -euo pipefail
cd "$(dirname "$0")"
d="backups/$(date +%F)"; mkdir -p "$d"
docker compose exec -T mongo mongodump --archive --gzip > "$d/mongo.gz"
docker compose exec -T postgres pg_dump -U litellm litellm | gzip > "$d/postgres.sql.gz"
docker compose exec -T tools tar czf - -C /data files > "$d/files.tgz"
cp .env "$d/env.backup" && chmod 600 "$d/env.backup"
echo "Copia guardada en $d"
