# 🟣 Pulso Bot · Omnicracia — Máquina perpetua de convencimiento

Bot de **Telegram** que le manda a cada persona, **1 a 1 y gratis**, el **Pulso diario** de Omnicracia,
le saca un **CONFIRMO** de un toque cada día (racha), responde dudas con el **FAQ** (preguntas reales,
voz del códice) y reactiva al que se apaga. Ciclo **perpetuo**: los 30 Pulsos se repiten por siempre.

**Costo de operar: $0** (la API de bots de Telegram no cobra por mensaje). Escala a cientos de miles.

---

## Qué hace, en corto
- **/start** → registra a la persona (y de dónde llegó, con el deep-link) y le da la bienvenida + botón *CONFIRMO*.
- **Pulso diario** → a una hora fija, a cada quien le toca el mensaje de su día (perpetuo, se repite el ciclo).
- **CONFIRMO** (botón o palabra) → sube su **racha** y le responde reafirmando su identidad. Es la (re)confirmación diaria del compromiso.
- **Onboarding de 3 toques** → bienvenida → por qué la disciplina gana → primera misión (trae a 1).
- **FAQ** → responde las preguntas reales (líder, legalidad, partido, costo, el plan, revocación, junta, aportar, etc.) con judo persuasivo y cierre que empuja un paso.
- **Reactivación** → al que lleva días sin confirmar, lo vuelve a jalar.
- **Botón "Pregúntale a Omnia"** → manda al clon Delphi (@Omnicracia_Omnia_bot) para dudas abiertas. Así este bot NO necesita la API cara de Delphi.

Todo el texto vive en **`content.py`** — lo editas sin tocar la lógica.

---

## Paso 1 · Crea el bot (gratis, 2 minutos)
1. En Telegram, escribe a **@BotFather** → `/newbot`.
2. Nombre visible: *Pulso Omnicracia* (o el que quieras). Usuario: algo que termine en `bot` (ej. `PulsoOmnicracia_bot`).
3. BotFather te da un **TOKEN** (algo como `123456789:AA...`). Guárdalo.
4. (Recomendado) `/setcommands` → pega:
   ```
   start - Entrar y arrancar mi racha
   ayuda - Ver qué puedo hacer
   ```
5. Tu **chat_id**: escríbele a **@userinfobot**, te lo dice (lo pones en `ADMIN_ID` para recibir /stats).

> **Nota:** este es un bot NUEVO y dedicado (no reusa a Omnia/Delphi). Omnia sigue tal cual para "preguntar lo que sea".

## Paso 2 · Configura
Copia `.env.example` a `.env` y llena `BOT_TOKEN` y `ADMIN_ID`. Ajusta hora si quieres (`SEND_HOUR`).

## Paso 3 · Enciéndelo (elige una opción)

### Opción A — Railway / Render (sin servidor propio, gratis o ~$5)
1. Sube esta carpeta a un repo de GitHub.
2. En **railway.app** (o render.com) → New Project → Deploy from GitHub.
3. Variables de entorno: pega las de tu `.env`.
4. Tipo de servicio: **Worker** (no web). Railway usa el `Procfile` (`python bot.py`).
5. Deploy. Listo — el bot queda encendido 24/7.

### Opción B — Una VPS baratita (~$5/mes, control total)
```bash
sudo apt update && sudo apt install -y python3-pip
pip3 install -r requirements.txt
cp .env.example .env   # y edítalo
set -a; source .env; set +a
python3 bot.py
# para dejarlo corriendo siempre, usa screen/tmux o un servicio systemd (ver abajo)
```

### Opción C — Probar en tu compu (unos minutos)
Igual que B, pero en tu máquina. Para producción usa A o B (deben estar siempre encendidos).

**systemd (para que reviva solo)** — crea `/etc/systemd/system/pulso.service`:
```
[Unit]
Description=Pulso Bot Omnicracia
After=network.target
[Service]
WorkingDirectory=/ruta/al/pulso_bot
EnvironmentFile=/ruta/al/pulso_bot/.env
ExecStart=/usr/bin/python3 bot.py
Restart=always
[Install]
WantedBy=multi-user.target
```
`sudo systemctl enable --now pulso`

---

## Paso 4 · Mete gente al bot (el funnel)
Comparte el **deep-link** con origen para medir de dónde llega cada quien:
- `https://t.me/TU_BOT?start=web` (desde la página / revocación)
- `https://t.me/TU_BOT?start=ig` (desde Instagram/ManyChat)
- `https://t.me/TU_BOT?start=tiktok`, `?start=fb`, `?start=qr`, etc.

El `start=...` queda guardado en cada usuario (columna `source`), así sabes qué canal jala más.

En omnicracia.com/revocacion pon 2 botones: *"Ya tengo Telegram → entra a Omnia/Pulso"* (deep-link) y *"Descarga Telegram"*.

---

## Comandos útiles (para ti)
- `/stats` → total, activos, cuántos confirmaron hoy.
- `/pulso_ya` → fuerza el envío del Pulso ahora mismo (para probar; normalmente se manda solo a la hora fija).

## Personalizar
- **Textos del Pulso / FAQ / onboarding:** `content.py`.
- **Hora del envío:** `SEND_HOUR` / `SEND_MIN` en `.env`.
- **Enlaces (Canal, Zoom, web, Omnia):** diccionario `LINKS` en `content.py`.

## Escala
SQLite aguanta cientos de miles. Para **millones**: (1) cambia `db.py` a Postgres (misma interfaz), y
(2) parte el envío diario en varios "workers" por rangos de `chat_id` (el `THROTTLE` mantiene ~20 msg/seg por worker;
con 3 workers son ~60/seg). La lógica del bot no cambia.

## Candados (no romper)
Cero mentiras (prueba social siempre real) · pacífico, legal, apartidista · sin líder · cero rojo ·
remate "Ellos necesitan de nosotros, no nosotros de ellos." · grito "SOY OMNICRACIA."
