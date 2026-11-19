# -*- coding: utf-8 -*-
"""
PULSO BOT · Omnicracia — Máquina perpetua de convencimiento, persuasión y (re)confirmación.

Qué hace, para siempre y gratis:
  • Captura a quien le da /start (con el origen del deep-link).
  • Le manda el PULSO diario 1:1 (ciclo perpetuo de 30 días que se repite por siempre).
  • Cada mensaje cierra con un CONFIRMO de un toque -> sube la RACHA (reconfirmación del compromiso).
  • Onboarding de 3 toques, FAQ persuasivo (preguntas reales), reactivación del que se apaga,
    y un botón "Pregúntale a Omnia" (el clon Delphi) para dudas abiertas.

Costo de operar: $0 (API de bots de Telegram). Escala a cientos de miles con el throttle incluido.
"""
import os
import re
import asyncio
import logging
import datetime as dt
import unicodedata
from zoneinfo import ZoneInfo

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.error import Forbidden, RetryAfter, TimedOut
from telegram.ext import (
    Application, CommandHandler, MessageHandler, CallbackQueryHandler,
    ContextTypes, filters,
)

import db
import content as C

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("pulso")

# ----------------------------------------------------------------- CONFIG (variables de entorno)
BOT_TOKEN = os.environ["BOT_TOKEN"]                       # de BotFather
ADMIN_ID  = int(os.environ.get("ADMIN_ID", "0"))         # tu chat_id para /stats
TZ        = ZoneInfo(os.environ.get("TZ", "America/Mexico_City"))
SEND_HOUR = int(os.environ.get("SEND_HOUR", "20"))       # hora local del Pulso diario (20 = 8 PM)
SEND_MIN  = int(os.environ.get("SEND_MIN", "0"))
THROTTLE  = float(os.environ.get("THROTTLE", "0.05"))    # seg entre mensajes (~20/seg, seguro)
LAPSE_DAYS = int(os.environ.get("LAPSE_DAYS", "3"))      # días sin confirmar -> reactivar


# ----------------------------------------------------------------- HELPERS
def norm(s: str) -> str:
    s = s.lower().strip()
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
    return s

def confirm_kb(button_text="💜 Hoy confirmo"):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(button_text, callback_data="confirm")],
        [InlineKeyboardButton("💬 Pregúntale a Omnia", url=C.LINKS["omnia_bot"]),
         InlineKeyboardButton("📣 El Canal", url=C.LINKS["canal"])],
    ])

async def send_md(bot, chat_id, text, reply_markup=None):
    """Envío robusto: respeta FLOOD_WAIT y saca de la lista a quien bloqueó el bot."""
    try:
        await bot.send_message(chat_id, text, parse_mode=ParseMode.MARKDOWN,
                               reply_markup=reply_markup, disable_web_page_preview=True)
        return True
    except Forbidden:
        db.set_status(chat_id, "blocked")   # bloqueó el bot -> fuera de la lista
        return False
    except RetryAfter as e:
        await asyncio.sleep(e.retry_after + 1)
        return await send_md(bot, chat_id, text, reply_markup)
    except TimedOut:
        await asyncio.sleep(1)
        return False
    except Exception as e:
        log.warning("send fail %s: %s", chat_id, e)
        return False


# ----------------------------------------------------------------- /start
async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user
    source = ctx.args[0] if ctx.args else None            # t.me/bot?start=ORIGEN
    db.add_or_touch_user(u.id, u.full_name, u.username, source)
    await send_md(ctx.bot, u.id, C.ONBOARDING["t1_welcome"],
                  reply_markup=confirm_kb("💜 Confirmo mi compromiso diario"))


# ----------------------------------------------------------------- Botón CONFIRMO (y texto CONFIRMO)
async def do_confirm(bot, chat_id, ctx):
    racha, already = db.record_confirm(chat_id)
    if already:
        await send_md(bot, chat_id, C.SYS["already_confirmed"].format(racha=racha))
        return
    if racha == 1:
        # primer CONFIRMO de la vida -> toque 2 del onboarding + programa el toque 3
        await send_md(bot, chat_id, C.ONBOARDING["t2_after_first_confirm"])
        if ctx and ctx.job_queue:
            ctx.job_queue.run_once(_send_t3, when=dt.timedelta(hours=20),
                                   data={"chat_id": chat_id}, name=f"t3-{chat_id}")
    else:
        await send_md(bot, chat_id, C.racha_message(racha))

async def on_confirm_button(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer("¡Confirmado! 💜")
    await do_confirm(ctx.bot, q.from_user.id, ctx)

async def _send_t3(ctx: ContextTypes.DEFAULT_TYPE):
    chat_id = ctx.job.data["chat_id"]
    await send_md(ctx.bot, chat_id, C.ONBOARDING["t3_first_mission"])


# ----------------------------------------------------------------- Texto libre: comandos cortos + FAQ
async def on_text(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_user.id
    txt = update.message.text or ""
    n = norm(txt)

    # comandos por palabra
    if n in ("confirmo", "confirmado", "aqui sigo", "presente"):
        return await do_confirm(ctx.bot, chat_id, ctx)
    if "soy omnicracia" in n:
        await do_confirm(ctx.bot, chat_id, ctx)
        return await send_md(ctx.bot, chat_id, "📣 *" + C.GRITO + "* ¡Así se grita! 💜")
    if n in ("pausa", "pausar", "stop", "baja", "de baja"):
        db.set_status(chat_id, "paused")
        return await send_md(ctx.bot, chat_id, C.SYS["paused"])
    if n in ("reanudar", "volver", "regresar", "continuar"):
        db.set_status(chat_id, "active")
        return await send_md(ctx.bot, chat_id, C.SYS["resumed"])
    if n in ("hecho", "listo", "ya"):
        return await send_md(ctx.bot, chat_id, C.SYS["mission_done"])
    if n in ("canon", "codice"):
        return await send_md(ctx.bot, chat_id, C.CANON_POCKET)
    if n in ("ayuda", "help", "menu", "comandos"):
        return await send_md(ctx.bot, chat_id, C.SYS["help"])

    # FAQ por "contiene" (preguntas reales)
    for keys, answer in C.FAQ:
        if any(k in n for k in keys):
            return await send_md(ctx.bot, chat_id, answer,
                                  reply_markup=confirm_kb("💜 Confirmo mi día"))

    # fallback persuasivo
    await send_md(ctx.bot, chat_id, C.SYS["fallback"],
                  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💬 Pregúntale a Omnia", url=C.LINKS["omnia_bot"])]]))


# ----------------------------------------------------------------- EL PULSO DIARIO (perpetuo)
async def job_pulso(ctx: ContextTypes.DEFAULT_TYPE):
    rows = db.users_to_send()
    log.info("Pulso diario -> %d suscriptores", len(rows))
    sent = 0
    for r in rows:
        idx = r["pulso_index"] % 30
        titulo, cuerpo, boton = C.PULSO[idx]
        header = f"🟣 *PULSO · {titulo}*\n\n"
        ok = await send_md(ctx.bot, r["chat_id"], header + cuerpo, reply_markup=confirm_kb(boton))
        if ok:
            db.advance_pulso(r["chat_id"])   # avanza su ciclo (perpetuo)
            sent += 1
        await asyncio.sleep(THROTTLE)
    log.info("Pulso enviado a %d", sent)


# ----------------------------------------------------------------- REACTIVACIÓN (al que se apaga)
async def job_reactivar(ctx: ContextTypes.DEFAULT_TYPE):
    rows = db.lapsed_users(LAPSE_DAYS)
    for r in rows:
        msg = ("Oye, te extrañamos. 💜 El movimiento no para: cada día somos más. "
               "No dejes que se te apague la racha — México necesita a los constantes, y tú eres uno.\n\n"
               "Vuelve de un toque 👇")
        await send_md(ctx.bot, r["chat_id"], msg, reply_markup=confirm_kb("🔥 Aquí sigo, confirmo"))
        await asyncio.sleep(THROTTLE)
    log.info("Reactivación -> %d", len(rows))


# ----------------------------------------------------------------- /stats (solo admin)
async def stats(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    s = db.stats()
    await send_md(ctx.bot, ADMIN_ID,
                  f"📊 *Pulso bot*\nTotal: {s['total']}\nActivos: {s['active']}\nConfirmaron hoy: {s['confirmed_today']}")

# disparo manual del Pulso (solo admin, por si quieres probar)
async def forzar_pulso(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    await job_pulso(ctx)


# ----------------------------------------------------------------- MAIN
def main():
    db.init_db()
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ayuda", lambda u, c: on_text(u, c)))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("pulso_ya", forzar_pulso))
    app.add_handler(CallbackQueryHandler(on_confirm_button, pattern="^confirm$"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))

    # trabajos diarios
    jq = app.job_queue
    jq.run_daily(job_pulso, time=dt.time(hour=SEND_HOUR, minute=SEND_MIN, tzinfo=TZ), name="pulso")
    jq.run_daily(job_reactivar, time=dt.time(hour=SEND_HOUR + 2 if SEND_HOUR < 22 else 11, minute=30, tzinfo=TZ),
                 name="reactivar")

    log.info("Pulso bot arriba. Envío diario %02d:%02d %s", SEND_HOUR, SEND_MIN, TZ)
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
