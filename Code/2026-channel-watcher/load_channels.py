"""youtube_channels.json'dan seçili kategorileri DB'ye yükle"""
import json, sqlite3
from pathlib import Path
from db import get_conn, init_db

CHANNELS_JSON = Path("/root/youtube_channels.json")
TARGET_CATS   = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 11: 12}  # index → cat_num

def load():
    init_db()
    data = json.loads(CHANNELS_JSON.read_text())
    categories = data["categories"]

    total = 0
    with get_conn() as conn:
        for idx, cat in enumerate(categories):
            if idx not in TARGET_CATS:
                continue
            cat_num  = TARGET_CATS[idx]
            cat_name = cat["name"]
            for ch in cat.get("channels", []):
                handle = ch.get("handle", "").strip()
                name   = ch.get("name", handle)
                if not handle:
                    continue
                try:
                    conn.execute(
                        "INSERT OR IGNORE INTO channels (name, handle, category, cat_num) VALUES (?,?,?,?)",
                        (name, handle, cat_name, cat_num)
                    )
                    total += 1
                except sqlite3.IntegrityError:
                    pass
        conn.commit()

    print(f"{total} kanal işlendi (yeni olanlar eklendi)")

    with get_conn() as conn:
        rows = conn.execute(
            "SELECT cat_num, category, COUNT(*) as n FROM channels GROUP BY cat_num ORDER BY cat_num"
        ).fetchall()
        for r in rows:
            print(f"  [{r['cat_num']}] {r['category']}: {r['n']} kanal")

if __name__ == "__main__":
    load()
