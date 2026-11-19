# -*- coding: utf-8 -*-
"""
Persistencia del Pulso bot (SQLite).
Guarda a cada suscriptor, su posición en el ciclo del Pulso, su racha y su estado.
SQLite aguanta cientos de miles sin problema. Para millones, se migra a Postgres
cambiando solo este archivo (la lógica de bot.py no cambia).
"""
import sqlite3
import datetime as dt
from contextlib import contextmanager

DB_PATH = "pulso.db"


@contextmanager
def _conn():
    con = sqlite3.connect(DB_PATH, timeout=30)
    con.row_factory = sqlite3.Row
    try:
        yield con
        con.commit()
    finally:
        con.close()


def init_db():
    with _conn() as con:
        con.execute("""
        CREATE TABLE IF NOT EXISTS users (
            chat_id       INTEGER PRIMARY KEY,
            name          TEXT,
            username      TEXT,
            source        TEXT,              -- de dónde llegó (parámetro del deep-link)
            joined_at     TEXT,              -- ISO date
            pulso_index   INTEGER DEFAULT 0, -- posición en el ciclo (0..29), perpetuo
            racha         INTEGER DEFAULT 0, -- días consecutivos confirmados
            last_confirm  TEXT,              -- ISO date del último CONFIRMO
            last_sent     TEXT,              -- ISO date del último Pulso enviado
            status        TEXT DEFAULT 'active'  -- active | paused | blocked
        )""")
        con.execute("CREATE INDEX IF NOT EXISTS idx_status ON users(status)")


def today() -> str:
    return dt.date.today().isoformat()


def add_or_touch_user(chat_id, name, username, source=None):
    """Registra a quien da /start. Si ya existe, no pisa su progreso."""
    with _conn() as con:
        row = con.execute("SELECT chat_id FROM users WHERE chat_id=?", (chat_id,)).fetchone()
        if row is None:
            con.execute(
                "INSERT INTO users(chat_id,name,username,source,joined_at,status) VALUES(?,?,?,?,?,'active')",
                (chat_id, name, username, source, today()),
            )
            return True   # nuevo
        else:
            con.execute("UPDATE users SET name=?, username=?, status='active' WHERE chat_id=?",
                        (name, username, chat_id))
            return False  # ya existía


def set_status(chat_id, status):
    with _conn() as con:
        con.execute("UPDATE users SET status=? WHERE chat_id=?", (status, chat_id))


def get_user(chat_id):
    with _conn() as con:
        return con.execute("SELECT * FROM users WHERE chat_id=?", (chat_id,)).fetchone()


def record_confirm(chat_id):
    """Marca el CONFIRMO del día. Devuelve (racha_nueva, ya_confirmo_hoy)."""
    with _conn() as con:
        u = con.execute("SELECT racha,last_confirm FROM users WHERE chat_id=?", (chat_id,)).fetchone()
        if u is None:
            return (0, False)
        t = today()
        if u["last_confirm"] == t:
            return (u["racha"], True)   # ya confirmó hoy
        yesterday = (dt.date.today() - dt.timedelta(days=1)).isoformat()
        nueva = u["racha"] + 1 if u["last_confirm"] == yesterday else 1  # rompe racha si faltó
        con.execute("UPDATE users SET racha=?, last_confirm=?, status='active' WHERE chat_id=?",
                    (nueva, t, chat_id))
        return (nueva, False)


def advance_pulso(chat_id):
    """Avanza al siguiente día del ciclo (perpetuo: vuelve a 0 tras 29)."""
    with _conn() as con:
        u = con.execute("SELECT pulso_index FROM users WHERE chat_id=?", (chat_id,)).fetchone()
        if u is None:
            return
        nxt = (u["pulso_index"] + 1) % 30
        con.execute("UPDATE users SET pulso_index=?, last_sent=? WHERE chat_id=?",
                    (nxt, today(), chat_id))


def users_to_send(batch_limit=None):
    """Suscriptores activos a los que NO se les ha mandado el Pulso hoy."""
    with _conn() as con:
        q = "SELECT chat_id, pulso_index, racha FROM users WHERE status='active' AND (last_sent IS NULL OR last_sent != ?)"
        args = [today()]
        if batch_limit:
            q += " LIMIT ?"
            args.append(batch_limit)
        return con.execute(q, args).fetchall()


def lapsed_users(days=3):
    """Activos que llevan 'days' sin confirmar (para reactivar)."""
    cutoff = (dt.date.today() - dt.timedelta(days=days)).isoformat()
    with _conn() as con:
        return con.execute(
            "SELECT chat_id FROM users WHERE status='active' AND (last_confirm IS NULL OR last_confirm < ?)",
            (cutoff,),
        ).fetchall()


def stats():
    with _conn() as con:
        total = con.execute("SELECT COUNT(*) c FROM users").fetchone()["c"]
        active = con.execute("SELECT COUNT(*) c FROM users WHERE status='active'").fetchone()["c"]
        confirmed_today = con.execute("SELECT COUNT(*) c FROM users WHERE last_confirm=?", (today(),)).fetchone()["c"]
        return {"total": total, "active": active, "confirmed_today": confirmed_today}
