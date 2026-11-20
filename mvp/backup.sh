#!/usr/bin/env bash
# Encrypted backup of chats, accounts, spend log and files -> ./backups/<date>.tar.enc  (AES-256, passphrase = BACKUP_PASSPHRASE in .env)
# Run daily with cron and copy the file off the server.  Restore: ./backup.sh --restore-help
set -euo pipefail
cd "$(dirname "$0")"
if [ "${1:-}" = "--restore-help" ]; then
  echo "Descifrar: openssl enc -d -aes-256-cbc -pbkdf2 -in backups/FECHA.tar.enc -pass env:BACKUP_PASSPHRASE | tar xz"
  echo "Después: mongorestore --archive --gzip < mongo.gz ; gunzip -c postgres.sql.gz | psql ; tar xzf files.tgz"; exit 0
fi
BACKUP_PASSPHRASE="$(grep ^BACKUP_PASSPHRASE= .env | cut -d= -f2-)"; export BACKUP_PASSPHRASE
[ -n "${BACKUP_PASSPHRASE:-}" ] || { echo "Falta BACKUP_PASSPHRASE en .env"; exit 1; }
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
docker compose exec -T mongo mongodump --archive --gzip > "$tmp/mongo.gz"
docker compose exec -T postgres pg_dump -U litellm litellm | gzip > "$tmp/postgres.sql.gz"
docker compose exec -T tools tar czf - -C /data files state > "$tmp/files.tgz"
mkdir -p backups
tar czf - -C "$tmp" . | openssl enc -aes-256-cbc -pbkdf2 -salt -pass env:BACKUP_PASSPHRASE > "backups/$(date +%F).tar.enc"
chmod 600 backups/*.tar.enc
echo "Copia cifrada guardada en backups/$(date +%F).tar.enc"
