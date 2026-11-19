#!/usr/bin/env bash
# Create an account (sign-up is closed on a public server). Usage: ./add-user.sh email@example.com "Full Name" [password]
set -euo pipefail
cd "$(dirname "$0")"
email="${1:?Uso: ./add-user.sh correo@ejemplo.com \"Nombre Apellido\" [contraseña]}"
name="${2:?Falta el nombre}"
pass="${3:-$(openssl rand -base64 12 | tr -d '/+=' | cut -c1-12)A1!}"
user="$(echo "${email%@*}" | tr -cd 'a-zA-Z0-9._-')"
docker compose exec -T librechat npm run create-user -- "$email" "$name" "$user" "$pass" --email-verified=true >/dev/null
echo "Cuenta creada. Correo: $email   Contraseña: $pass   (pídele que la cambie al entrar)"
