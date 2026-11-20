#!/usr/bin/env bash
# Light self-check you can run any time (on the machine that runs the stack). Prints OK / PROBLEMA per item. Not a pen test.
cd "$(dirname "$0")/.."
URL="${1:-$(grep ^PUBLIC_URL= .env 2>/dev/null | cut -d= -f2)}"; URL="${URL:-http://localhost}"
K=""; case "$URL" in *localhost*) K="-k";; esac   # self-signed certificate on localhost
ok(){ echo "OK        $1"; }; bad(){ echo "PROBLEMA  $1"; }
[ "$(stat -c %a .env 2>/dev/null)" = "600" ] && ok ".env solo legible por su dueño" || bad ".env debería tener permisos 600"
grep -qE "=(change-me|sk-change-me)$" .env 2>/dev/null && bad "hay contraseñas de ejemplo en .env" || ok "sin contraseñas de ejemplo en .env"
grep -q "^ALLOW_REGISTRATION=true" .env 2>/dev/null && bad "el registro público está abierto" || ok "registro público cerrado"
code=$(curl -s $K -o /dev/null -w "%{http_code}" "$URL/gasto"); [ "$code" = "401" ] && ok "/gasto pide contraseña" || bad "/gasto devolvió $code (debería pedir contraseña: 401)"
hdr=$(curl -sI $K "$URL/"); for h in x-content-type-options x-frame-options; do echo "$hdr" | grep -qi "$h" && ok "cabecera $h" || bad "falta cabecera $h"; done
case "$URL" in https://*) echo "$hdr" | grep -qi strict-transport && ok "HSTS activo" || bad "falta HSTS";; *) echo "AVISO     sin https (modo local)";; esac
pub=$(docker compose ps --format '{{.Service}} {{.Publishers}}' 2>/dev/null | grep -E "mongo|postgres|litellm" | grep -E "0\.0\.0\.0|:::" )
[ -z "$pub" ] && ok "bases de datos y router no expuestos a internet" || bad "puertos expuestos: $pub"
grep -E "image:.*(:latest|[a-z]$)" docker-compose.yml >/dev/null && bad "hay imágenes sin versión fija" || ok "imágenes con versión fija"
docker compose exec -T librechat printenv ALLOW_EMAIL_LOGIN 2>/dev/null | grep -q true && echo "AVISO     login con correo y contraseña activo (ok para pruebas; en producción usa Google/Microsoft)"
