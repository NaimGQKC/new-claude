#!/usr/bin/env bash
# One-command setup: creates .env with fresh secrets, asks for the two things only a person can give, starts everything.
set -euo pipefail
cd "$(dirname "$0")"
command -v docker >/dev/null || { echo "Instala Docker primero: https://docs.docker.com/engine/install/"; exit 1; }
if [ ! -f .env ]; then
  cp .env.example .env
  rnd() { openssl rand -hex "$1"; }
  sed -i "s|^LITELLM_MASTER_KEY=.*|LITELLM_MASTER_KEY=sk-$(rnd 16)|; s|^POSTGRES_PASSWORD=.*|POSTGRES_PASSWORD=$(rnd 16)|; \
          s|^CREDS_KEY=.*|CREDS_KEY=$(rnd 32)|; s|^CREDS_IV=.*|CREDS_IV=$(rnd 16)|; \
          s|^JWT_SECRET=.*|JWT_SECRET=$(rnd 32)|; s|^JWT_REFRESH_SECRET=.*|JWT_REFRESH_SECRET=$(rnd 32)|" .env
  read -rp "Clave de OpenRouter (openrouter.ai/keys): " k
  sed -i "s|^OPENROUTER_API_KEY=.*|OPENROUTER_API_KEY=$k|" .env
  read -rp "Dominio (ej. chat.miempresa.com) o Enter para probar en este equipo: " d
  if [ -n "$d" ]; then sed -i "s|^DOMAIN=.*|DOMAIN=$d|; s|^PUBLIC_URL=.*|PUBLIC_URL=https://$d|" .env; fi
  chmod 600 .env
fi
docker compose up -d --build
echo; echo "Listo. Abre: $(grep ^PUBLIC_URL= .env | cut -d= -f2)"
echo "Crea tu cuenta con el botón 'Registrarse'. Después puedes poner ALLOW_REGISTRATION=false en .env."
