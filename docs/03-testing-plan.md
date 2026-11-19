# Getting people to test it

Goal of the test: find out whether small-business people use it a second time, and whether they trust the cost. Nothing else.

## Setup (free, no cloud server)
- Run the stack with Docker on your own PC (`mvp/install.sh`).
- Share it with a free Cloudflare quick tunnel: `cloudflared tunnel --url http://localhost` gives a temporary https link. The PC must stay on.
- Close public sign-up (`ALLOW_REGISTRATION=false`) and create each tester's account by hand.
- Safety nets: set `MONTHLY_CAP_EUR` (for example 10) and the OpenRouter key's own $ limit. Tell testers: **no real client data**, because OpenRouter does not keep data in the EU.

## Who
5 to 10 people who run or work in a small business: a physio clinic, a real-estate agent, an accountant, a shop, a restaurant. Friends and family of friends count. People close to the target are better than tech friends.

## What to ask them to do (day 1, 15 minutes)
1. Tell the assistant what you do.
2. Paste a real-looking email and ask for a reply.
3. Ask for a spreadsheet, a document or an image you would actually use.
4. Ask one question you would normally google, with "investiga".

## What to measure
- **Day 2 and day 7 return:** did they open it again without being asked?
- **What they asked for most** (the decision log in the server output shows action and model per message).
- **Cost:** average spend per person in "Mi gasto"; did the estimates surprise them?
- **Three questions at the end:** Would you use it instead of what you use now? What was missing? What would you pay per month?

## Message to send testers (Spanish)
Hola, estoy probando un asistente de IA pensado para pequeños negocios: redacta emails, crea documentos e imágenes y busca información con fuentes. Solo pagas lo que usas, y de momento es gratis para ti. ¿Lo pruebas 15 minutos esta semana y me cuentas qué te ha parecido? Por favor, no uses datos reales de clientes.
