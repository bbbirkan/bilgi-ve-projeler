"""SQLite DB — Sovereign Channel Watcher"""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "channels.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS channels (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    handle      TEXT UNIQUE NOT NULL,
    category    TEXT NOT NULL,
    cat_num     INTEGER NOT NULL,
    active      INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS videos (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    video_id     TEXT UNIQUE NOT NULL,
    channel_id   INTEGER REFERENCES channels(id),
    title        TEXT,
    published_at TEXT,
    url          TEXT,
    duration_sec INTEGER,
    fetched_at   TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS transcripts (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    video_id     TEXT UNIQUE REFERENCES videos(video_id),
    content      TEXT,
    fetched_at   TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS analyses (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    video_id     TEXT UNIQUE REFERENCES videos(video_id),
    summary      TEXT,
    destination  TEXT,
    insight      TEXT,
    analyzed_at  TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS suggestions (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    video_id     TEXT REFERENCES videos(video_id),
    report_date  TEXT,
    approved     INTEGER DEFAULT 0,
    applied      INTEGER DEFAULT 0,
    created_at   TEXT DEFAULT (datetime('now'))
);
"""

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_conn() as conn:
        conn.executescript(SCHEMA)
    print(f"DB hazır: {DB_PATH}")

def video_exists(video_id: str) -> bool:
    with get_conn() as conn:
        row = conn.execute("SELECT 1 FROM videos WHERE video_id=?", (video_id,)).fetchone()
        return row is not None

def transcript_exists(video_id: str) -> bool:
    with get_conn() as conn:
        row = conn.execute("SELECT 1 FROM transcripts WHERE video_id=?", (video_id,)).fetchone()
        return row is not None

if __name__ == "__main__":
    init_db()
