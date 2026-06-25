#!/usr/bin/env python3
"""
YT-Vault — Apify ile YouTube kanal video listesi çekici
Kullanım: python3 fetch_channel.py "@GrahamStephan" [--max 100]
"""

import os, sys, json, time, argparse
import urllib.request, urllib.error

TOKEN = os.environ.get("APIFY_API_TOKEN", "")
ACTOR = "grow_media~youtube-channel-video-scraper"
BASE  = "https://api.apify.com/v2"

def run_actor(channel_handle: str, max_videos: int = 500) -> list:
    if not TOKEN:
        print("HATA: APIFY_API_TOKEN bulunamadı. source /root/.sovereign_env")
        sys.exit(1)

    handle = channel_handle.lstrip("@")
    handle = f"@{handle}" if not handle.startswith("http") else handle

    payload = json.dumps({
        "channelHandle": handle,
        "maxVideos": max_videos
    }).encode()

    print(f"[YT-Vault] Başlatılıyor: {handle} (max {max_videos} video)")

    # Run başlat
    req = urllib.request.Request(
        f"{BASE}/acts/{ACTOR}/runs?token={TOKEN}",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req) as r:
        run = json.load(r)

    run_id = run["data"]["id"]
    dataset_id = run["data"]["defaultDatasetId"]
    print(f"[YT-Vault] Run ID: {run_id} — bekleniyor...")

    # Tamamlanana kadar bekle
    for attempt in range(60):
        time.sleep(5)
        with urllib.request.urlopen(
            f"{BASE}/actor-runs/{run_id}?token={TOKEN}"
        ) as r:
            status = json.load(r)["data"]["status"]

        if status == "SUCCEEDED":
            break
        elif status in ("FAILED", "ABORTED", "TIMED-OUT"):
            print(f"[YT-Vault] HATA: Run {status}")
            sys.exit(1)

        if attempt % 6 == 0:
            print(f"[YT-Vault] Devam ediyor... ({attempt*5}sn)")

    # Sonuçları çek
    with urllib.request.urlopen(
        f"{BASE}/datasets/{dataset_id}/items?token={TOKEN}&limit=10000"
    ) as r:
        items = json.load(r)

    return items if isinstance(items, list) else items.get("items", [])


def save_results(videos: list, channel: str, output_dir: str = "."):
    os.makedirs(output_dir, exist_ok=True)
    channel_slug = channel.lstrip("@").replace("/", "_")
    out_file = os.path.join(output_dir, f"{channel_slug}_videos.json")

    # Sadece gerekli alanları al
    clean = []
    for v in videos:
        clean.append({
            "title":       v.get("title", ""),
            "url":         v.get("url", ""),
            "id":          v.get("id", ""),
            "date":        v.get("date", ""),
            "duration":    v.get("duration", ""),
            "viewCount":   v.get("viewCount", 0),
            "likes":       v.get("likes", 0),
            "description": v.get("description", "")[:300],
            "channelName": v.get("channelName", ""),
            "channelTotalVideos": v.get("channelTotalVideos", 0),
        })

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(clean, f, ensure_ascii=False, indent=2)

    print(f"[YT-Vault] ✅ {len(clean)} video → {out_file}")
    return out_file, clean


def main():
    parser = argparse.ArgumentParser(description="YT-Vault: Kanal video listesi")
    parser.add_argument("channel", help="Kanal handle (@GrahamStephan) veya URL")
    parser.add_argument("--max", type=int, default=500, help="Max video sayısı (varsayılan: 500)")
    parser.add_argument("--output", default="output", help="Çıktı klasörü")
    args = parser.parse_args()

    videos = run_actor(args.channel, args.max)
    out_file, clean = save_results(videos, args.channel, args.output)

    # Özet
    if clean:
        print(f"\n--- ÖZET ---")
        print(f"Kanal: {clean[0].get('channelName', args.channel)}")
        print(f"Toplam video: {len(clean)}")
        print(f"İlk video: {clean[0].get('title','?')[:60]}")
        print(f"Son video:  {clean[-1].get('title','?')[:60]}")
        print(f"Dosya: {out_file}")


if __name__ == "__main__":
    main()
