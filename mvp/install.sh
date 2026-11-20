#!/usr/bin/env bash
# One-command setup: creates .env with fresh secrets, asks for the two things only a person can give, starts everything.
set -euo pipefail
cd "$(dirname "$0")"
command -v docker >/dev/null || { echo "Instala Docker primero: https://docs.docker.com/engine/install/"; exit 1; }
if [ ! -f .env ]; then
  if docker volume ls -q | grep -q "_pg_data$"; then
    echo "Ya existen datos de una instalación anterior pero falta el archivo .env."
    echo "Si quieres empezar de cero (se borran los datos): docker compose down -v   y vuelve a ejecutar ./install.sh"; exit 1
  fi
  cp .env.example .env
  rnd() { openssl rand -hex "$1"; }
  sed -i "s|^LITELLM_MASTER_KEY=.*|LITELLM_MASTER_KEY=sk-$(rnd 16)|; s|^POSTGRES_PASSWORD=.*|POSTGRES_PASSWORD=$(rnd 16)|; \
          s|^CREDS_KEY=.*|CREDS_KEY=$(rnd 32)|; s|^CREDS_IV=.*|CREDS_IV=$(rnd 16)|; \
          s|^JWT_SECRET=.*|JWT_SECRET=$(rnd 32)|; s|^JWT_REFRESH_SECRET=.*|JWT_REFRESH_SECRET=$(rnd 32)|" .env
  # Values can come from the environment (for scripts) or be asked.
  k="${OPENROUTER_API_KEY:-}"; [ -n "$k" ] || read -rp "Clave de OpenRouter (openrouter.ai/keys): " k
  sed -i "s|^OPENROUTER_API_KEY=.*|OPENROUTER_API_KEY=$k|" .env
  d="${DOMAIN:-}"; [ -n "$d" ] || read -rp "Dominio (ej. chat.miempresa.com) o Enter para probar en este equipo: " d
  if [ -n "$d" ]; then
    sed -i "s|^DOMAIN=.*|DOMAIN=$d|; s|^PUBLIC_URL=.*|PUBLIC_URL=https://$d|; s|^ALLOW_REGISTRATION=.*|ALLOW_REGISTRATION=false|" .env
    c="${MONTHLY_CAP_EUR:-}"; [ -n "$c" ] || read -rp "Límite de gasto mensual en euros (Enter = 20): " c
    sed -i "s|^MONTHLY_CAP_EUR=.*|MONTHLY_CAP_EUR=${c:-20}|" .env
  fi
  # Backups are encrypted with a generated passphrase
  sed -i "s|^BACKUP_PASSPHRASE=.*|BACKUP_PASSPHRASE=$(rnd 24)|" .env
  # Admin password for the spending page (user: admin)
  ap="${ADMIN_PASSWORD:-$(rnd 8)}"
  ah="$(docker run --rm caddy:2 caddy hash-password --plaintext "$ap")"
  sed -i "s|^ADMIN_HASH=.*|ADMIN_HASH='$ah'|" .env
  echo "Página de gasto: usuario admin, contraseña $ap   (anótala; no se vuelve a mostrar)"
  # Days to keep conversations
  rd="${RETENTION_DAYS:-}"; [ -n "$rd" ] || read -rp "¿Cuántos días guardar las conversaciones? (Enter = 90): " rd
  rd="${rd:-90}"; sed -i "s|^RETENTION_DAYS=.*|RETENTION_DAYS=$rd|" .env
  sed -i "s|generalChatRetention: .*|generalChatRetention: $((rd*24))    # $rd days (set by install.sh)|" librechat/librechat.yaml
  # How staff log in
  if [ -n "${d:-}" ]; then
    lp="${LOGIN_PROVIDER:-}"; [ -n "$lp" ] || read -rp "¿Cómo entra tu equipo? 1) cuenta de Google  2) cuenta de Microsoft  3) correo y contraseña [3]: " lp
    dom="${EMAIL_DOMAIN:-}"
    case "${lp:-3}" in
      1|google)
        [ -n "$dom" ] || read -rp "Dominio de correo de la empresa (ej. miempresa.com): " dom
        gid="${GOOGLE_CLIENT_ID:-}"; [ -n "$gid" ] || read -rp "Google Client ID: " gid
        gsec="${GOOGLE_CLIENT_SECRET:-}"; [ -n "$gsec" ] || read -rp "Google Client Secret: " gsec
        sed -i "s|^ALLOW_EMAIL_LOGIN=.*|ALLOW_EMAIL_LOGIN=false|; s|^ALLOW_SOCIAL_LOGIN=.*|ALLOW_SOCIAL_LOGIN=true|; s|^ALLOW_SOCIAL_REGISTRATION=.*|ALLOW_SOCIAL_REGISTRATION=true|; s|^ALLOWED_REGISTRATION_DOMAINS=.*|ALLOWED_REGISTRATION_DOMAINS=$dom|; s|^GOOGLE_CLIENT_ID=.*|GOOGLE_CLIENT_ID=$gid|; s|^GOOGLE_CLIENT_SECRET=.*|GOOGLE_CLIENT_SECRET=$gsec|" .env
        echo "En Google Cloud, añade esta URI de redirección autorizada: https://$d/oauth/google/callback" ;;
      2|microsoft)
        [ -n "$dom" ] || read -rp "Dominio de correo de la empresa (ej. miempresa.com): " dom
        tid="${MS_TENANT_ID:-}"; [ -n "$tid" ] || read -rp "Microsoft Directory (tenant) ID: " tid
        mid="${MS_CLIENT_ID:-}"; [ -n "$mid" ] || read -rp "Microsoft Application (client) ID: " mid
        msec="${MS_CLIENT_SECRET:-}"; [ -n "$msec" ] || read -rp "Microsoft Client Secret: " msec
        sed -i "s|^ALLOW_EMAIL_LOGIN=.*|ALLOW_EMAIL_LOGIN=false|; s|^ALLOW_SOCIAL_LOGIN=.*|ALLOW_SOCIAL_LOGIN=true|; s|^ALLOW_SOCIAL_REGISTRATION=.*|ALLOW_SOCIAL_REGISTRATION=true|; s|^ALLOWED_REGISTRATION_DOMAINS=.*|ALLOWED_REGISTRATION_DOMAINS=$dom|; s|^OPENID_ISSUER=.*|OPENID_ISSUER=https://login.microsoftonline.com/$tid/v2.0|; s|^OPENID_CLIENT_ID=.*|OPENID_CLIENT_ID=$mid|; s|^OPENID_CLIENT_SECRET=.*|OPENID_CLIENT_SECRET=$msec|; s|^OPENID_SESSION_SECRET=.*|OPENID_SESSION_SECRET=$(rnd 32)|" .env
        echo "En Microsoft Entra, añade esta URI de redirección (Web): https://$d/oauth/openid/callback" ;;
      *) : ;;
    esac
  fi
  chmod 600 .env
fi
docker compose up -d ${COMPOSE_UP_ARGS:---build}
echo; echo "Listo. Abre: $(grep ^PUBLIC_URL= .env | cut -d= -f2)"
if grep -q '^ALLOW_REGISTRATION=false' .env; then
  echo "El registro público está cerrado. Crea cuentas con: ./add-user.sh correo@ejemplo.com \"Nombre Apellido\""
else
  echo "Crea tu cuenta con el botón 'Registrarse'."
fi
