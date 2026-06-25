#!/usr/bin/env python3
"""
Sovereign Channel Watcher — Ana akış
Günlük 07:00 ET:
  1. Apify → 202 kanalın yeni videolarını çek
  2. Apify pintostudio → transkript çek (sadece yeniler)
  3. MiniMax M3 → analiz (özet + A/B/C şıklar + nereye gider)
  4. Email → 8birkan@gmail.com akşam raporu
"""

from datetime import datetime
from zoneinfo import ZoneInfo
from db import init_db
from fetcher import run_fetch
from transcriber import run_transcribe
from analyzer import run_analyze
from reporter import send_email

ET_TZ = ZoneInfo("America/New_York")


def main():
    now = datetime.now(ET_TZ).strftime("%Y-%m-%d %H:%M ET")
    print(f"\n[{now}] Channel Watcher başladı")
    print("=" * 50)

    init_db()

    # 1. Yeni videoları çek
    print("\n[1/4] Video listesi çekiliyor...")
    new_videos = run_fetch()

    if not new_videos:
        print("  Yeni video yok. Çıkılıyor.")
        return

    # 2. Transkript çek
    print(f"\n[2/4] Transkript çekiliyor ({len(new_videos)} video)...")
    transcribed = run_transcribe(new_videos)

    if not transcribed:
        print("  Transkript alınamadı. Çıkılıyor.")
        return

    # 3. Analiz et
    print(f"\n[3/4] Analiz ediliyor ({len(transcribed)} video)...")
    analyzed = run_analyze(transcribed)

    # 4. Email raporu
    print(f"\n[4/4] Email raporu gönderiliyor...")
    if analyzed:
        send_email(analyzed)
    else:
        print("  Analiz sonucu yok, email atlanıyor.")

    done = datetime.now(ET_TZ).strftime("%H:%M ET")
    print(f"\n[{done}] Tamamlandı. {len(analyzed)} video analiz edildi.")
    print("=" * 50)


if __name__ == "__main__":
    main()
