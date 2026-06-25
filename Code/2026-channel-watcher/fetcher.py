"""Apify ile YouTube kanal videolarını çek — DB'de olmayan yeni videolar"""
import json, os, time, requests
from pathlib import Path
from db import get_conn, video_exists

APIFY_TOKEN = os.environ.get("APIFY_API_TOKEN", "")

# Her kanaldan max kaç video kontrol edelim
MAX_PER_CHANNEL = 5


def get_apify_token() -> str:
    if APIFY_TOKEN:
        return APIFY_TOKEN
    for env_file in ["/root/.sovereign_env", "/root/.hermes/.env"]:
        try:
            for line in Path(env_file).read_text().splitlines():
                if line.startswith("APIFY_API_TOKEN=") or line.startswith("APIFY_TOKEN="):
                    return line.split("=", 1)[1].strip()
        except FileNotFoundError:
            pass
    return ""


def fetch_channel_videos(handles: list[str], token: str) -> list[dict]:
    """Apify youtube-scraper ile birden fazla kanalın son videolarını çek."""
    start_urls = [
        {"url": f"https://www.youtube.com/{h}/videos"}
        for h in handles
    ]

    payload = {
        "startUrls": start_urls,
        "maxResultsShorts": 0,
        "maxResultStreams": 0,
        "maxResults": MAX_PER_CHANNEL,
    }

    # Run actor
    run_url = "https://api.apify.com/v2/acts/streamers~youtube-scraper/runs"
    r = requests.post(
        run_url,
        params={"token": token, "waitForFinish": 120},
        json=payload,
        timeout=150
    )
    r.raise_for_status()
    run_data = r.json()
    dataset_id = run_data["data"].get("defaultDatasetId")
    if not dataset_id:
        print("  Dataset ID alınamadı")
        return []

    # Get results
    items_url = f"https://api.apify.com/v2/datasets/{dataset_id}/items"
    items_r = requests.get(items_url, params={"token": token, "limit": 2000}, timeout=30)
    items_r.raise_for_status()
    return items_r.json()


def save_new_videos(videos: list[dict]) -> list[dict]:
    """Yeni (DB'de olmayan) videoları kaydet, listesini döndür."""
    new = []
    with get_conn() as conn:
        for v in videos:
            vid_id = v.get("id") or v.get("videoId", "")
            if not vid_id or video_exists(vid_id):
                continue

            # Kanal handle'ından channel_id bul
            handle = v.get("channelHandle") or v.get("channelUrl", "").split("@")[-1]
            ch_row = conn.execute(
                "SELECT id FROM channels WHERE handle LIKE ?", (f"%{handle}%",)
            ).fetchone()
            channel_id = ch_row["id"] if ch_row else None

            conn.execute(
                """INSERT OR IGNORE INTO videos
                   (video_id, channel_id, title, published_at, url, duration_sec)
                   VALUES (?,?,?,?,?,?)""",
                (
                    vid_id,
                    channel_id,
                    v.get("title", ""),
                    v.get("date") or v.get("publishedAt", ""),
                    v.get("url") or f"https://www.youtube.com/watch?v={vid_id}",
                    v.get("duration", 0),
                )
            )
            new.append({
                "video_id": vid_id,
                "title": v.get("title", ""),
                "channel": v.get("channelName", handle),
                "url": v.get("url") or f"https://www.youtube.com/watch?v={vid_id}",
                "published_at": v.get("date") or v.get("publishedAt", ""),
            })
        conn.commit()
    return new


def run_fetch() -> list[dict]:
    token = get_apify_token()
    if not token:
        print("APIFY_API_TOKEN bulunamadı!")
        return []

    with get_conn() as conn:
        rows = conn.execute("SELECT handle FROM channels WHERE active=1").fetchall()
    handles = [r["handle"] for r in rows]

    print(f"  {len(handles)} kanal kontrol ediliyor...")

    # Batch: 50'şer kanal gönder (Apify limit)
    all_videos = []
    batch_size = 50
    for i in range(0, len(handles), batch_size):
        batch = handles[i:i + batch_size]
        print(f"  Batch {i//batch_size + 1}: {len(batch)} kanal...")
        try:
            videos = fetch_channel_videos(batch, token)
            all_videos.extend(videos)
            time.sleep(2)
        except Exception as e:
            print(f"  Batch hata: {e}")

    print(f"  Toplam çekilen video: {len(all_videos)}")
    new = save_new_videos(all_videos)
    print(f"  Yeni video (DB'de yok): {len(new)}")
    return new


if __name__ == "__main__":
    from db import init_db
    init_db()
    new = run_fetch()
    for v in new:
        print(f"  + {v['channel']}: {v['title']}")
