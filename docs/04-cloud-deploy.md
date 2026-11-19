# Run it in the cloud (about 20 minutes)

**Cost:** server about €6-10 per month (from €5.49 + VAT for the smallest at Hetzner; you need the 4 GB RAM size: the stack uses about 1.6 GB idle, 2 GB would be tight), plus a domain at about €10 per year, plus model usage (cents per person per day). Check the price when you create the server.

## 1. Create the server
1. Create an account at hetzner.com and a **Cloud** server: Ubuntu 24.04, **at least 4 GB RAM**, location **Falkenstein, Nuremberg or Helsinki** (EU), add your SSH key.
2. Note the server's IP address.

## 2. Point a web address at it
- Buy a cheap domain (any registrar) and create an **A record**: `chat.yourdomain.com` -> the server IP.
- Quick option with no domain: use `1-2-3-4.sslip.io` (your IP with dashes). It works, but the free certificate may fail if too many people share that name.

## 3. Install (on the server, as root)
```bash
ssh root@YOUR_SERVER_IP
curl -fsSL https://raw.githubusercontent.com/NaimGQKC/new-claude/claude/modest-brahmagupta-ksrq84/mvp/deploy/server-setup.sh | bash
git clone https://github.com/NaimGQKC/new-claude.git && cd new-claude/mvp
./install.sh
```
`server-setup.sh` installs Docker, closes every port except ssh and the web, adds swap and turns on automatic security updates.
`install.sh` asks for your OpenRouter key, the domain, and a monthly spending limit (default 20 EUR), creates all secrets, and starts everything.
The first start downloads about 3 GB; wait a few minutes, then open `https://chat.yourdomain.com`.

## 4. Create accounts for testers
Public sign-up is closed on a server. Create each account yourself and send them the password:
```bash
./add-user.sh maria@ejemplo.com "María López"
```

## 5. Keep it safe and cheap
- Spending: the app stops at `MONTHLY_CAP_EUR` (in `.env`). Also set a dollar limit on the OpenRouter key itself (openrouter.ai/keys) as a second brake.
- Backups: `./backup.sh` copies chats, accounts, spend log and files to `backups/`. Run it daily (`crontab -e`: `0 3 * * * cd /root/new-claude/mvp && ./backup.sh`) and download the folder now and then.
- Updates: `cd new-claude/mvp && git pull && docker compose up -d --build`.
- Watch it: `docker compose logs -f tools` shows one line per message: what was asked (action), which model, the estimated cost.
- Look at spending: `https://chat.yourdomain.com/gasto`.

## 6. Before real customers (not needed for friendly testers)
- Tell testers: **no real client data**. The MVP sends prompts through OpenRouter, which does not keep data in the EU.
- Move to an EU host (OVH, T-Systems, Berget...) by editing `litellm/config.yaml`, review the Kimi license, and add terms and a privacy notice.
- The code repository is public. It contains no keys (`.env` is never committed), but anyone can read it.
