#!/usr/bin/env bash
# Run ONCE as root on a fresh Ubuntu 24.04 server: installs Docker, closes everything except ssh/web, adds swap, enables auto security updates.
set -euo pipefail
export DEBIAN_FRONTEND=noninteractive
apt-get update -y
apt-get install -y docker.io docker-compose-v2 git openssl ufw unattended-upgrades
systemctl enable --now docker
ufw default deny incoming; ufw default allow outgoing
ufw allow OpenSSH; ufw allow 80/tcp; ufw allow 443/tcp
ufw --force enable
if ! swapon --show | grep -q .; then
  fallocate -l 2G /swapfile && chmod 600 /swapfile && mkswap /swapfile && swapon /swapfile && echo '/swapfile none swap sw 0 0' >> /etc/fstab
fi
echo "Servidor listo. Siguiente: git clone https://github.com/NaimGQKC/new-claude.git && cd new-claude/mvp && ./install.sh"
