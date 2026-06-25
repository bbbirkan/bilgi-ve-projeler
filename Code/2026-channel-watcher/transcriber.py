"""Apify pintostudio ile transkript çek — sadece DB'de transkript olmayan videolar"""
import os, requests, time
from pathlib import Path
from db import get_conn, transcript_exists

APIFY_ACTOR = "pintostudio/youtube-transcript-scraper"


def get_apify_token() -> str:
    for env_file in ["/root/.sovereign_env", "/root/.hermes/.env"]:
        try:
            for line in Path(env_file).read_text().splitlines():
                if line.startswith("APIFY_API_TOKEN=") or line.startswith("APIFY_TOKEN="):
                    return line.split("=", 1)[1].strip()
        except FileNotFoundError:
            pass
    return os.environ.get("APIFY_API_TOKEN", "")


def fetch_transcript(video_id: str, token: str) -> str | None:
    url = f"https://www.youtube.com/watch?v={video_id}"
    run_url = f"https://api.apify.com/v2/acts/{APIFY_ACTOR.replace('/', '~')}/runs"
    try:
        r = requests.post(
            run_url,
            params={"token": token, "waitForFinish": 60},
            json={"videoUrl": url, "language": "en"},
            timeout=90
        )
        r.raise_for_status()
        dataset_id = r.json()["data"].get("defaultDatasetId")
        if not dataset_id:
            return None

        items_r = requests.get(
            f"https://api.apify.com/v2/datasets/{dataset_id}/items",
            params={"token": token},
            timeout=30
        )
        items = items_r.json()
        if items:
            return items[0].get("transcript") or items[0].get("text") or ""
    except Exception as e:
        print(f"  Transkript hata ({video_id}): {e}")
    return None


def run_transcribe(new_videos: list[dict]) -> list[dict]:
    """Sadece yeni videolar için transkript çek."""
    token = get_apify_token()
    if not token:
        print("APIFY_API_TOKEN yok!")
        return []

    todo = [v for v in new_videos if not transcript_exists(v["video_id"])]
    print(f"  Transkript çekilecek: {len(todo)} video")

    done = []
    with get_conn() as conn:
        for v in todo:
            print(f"  Çekiliyor: {v['title'][:50]}...")
            text = fetch_transcript(v["video_id"], token)
            if text:
                conn.execute(
                    "INSERT OR REPLACE INTO transcripts (video_id, content) VALUES (?,?)",
                    (v["video_id"], text)
                )
                v["transcript"] = text
                done.append(v)
                print(f"  ✓ {len(text)} karakter")
            else:
                print(f"  ✗ Transkript alınamadı")
            time.sleep(1)
        conn.commit()

    print(f"  Transkript tamamlanan: {len(done)}/{len(todo)}")
    return done


if __name__ == "__main__":
    from db import init_db, get_conn
    init_db()
    with get_conn() as conn:
        rows = conn.execute(
            """SELECT v.video_id, v.title, v.url FROM videos v
               LEFT JOIN transcripts t ON v.video_id=t.video_id
               WHERE t.video_id IS NULL LIMIT 3"""
        ).fetchall()
    videos = [dict(r) for r in rows]
    run_transcribe(videos)
