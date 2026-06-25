"""opencode-go/minimax-m3 ile video analizi — özet + nereye gider"""
import subprocess, json
from db import get_conn

# Nereye gider haritası — kategori bazlı
DESTINATION_MAP = {
    1:  ("STRATEJI.md",                    "/root/trading-system/STRATEJI.md"),
    2:  ("STRATEJI.md + sovereign-brain",  "/root/trading-system/STRATEJI.md"),
    3:  ("STRATEJI.md kripto",             "/root/trading-system/STRATEJI.md"),
    4:  ("sovereign-brain/techniques/",    "/root/sovereign-brain/techniques/"),
    5:  ("sovereign-brain/techniques/",    "/root/sovereign-brain/techniques/"),
    12: ("sovereign-brain/research/",      "/root/sovereign-brain/research/"),
}

PROMPT_TEMPLATE = """Sen bir bilgi yönetim asistanısın.

Video başlığı: {title}
Kanal: {channel}
Kategori: {category}

Transkript (ilk 4000 karakter):
{transcript}

Görev: Bu videodan SİSTEME KATILABİLECEK öğrenimleri çıkar.
- Gerçekten değerli olan kadar çıkar: az ise 1, zengin içerikse 5'e kadar
- Her item: ne öğrendik + sisteme nasıl katabiliriz
- Zorunlu 3 değil — kaliteye göre karar ver

SADECE JSON döndür:
{{
  "summary": "2-3 cümle genel özet",
  "items": [
    {{
      "insight": "ne öğrendik (1 cümle)",
      "action": "sisteme nasıl katabiliriz (1 cümle)",
      "destination": "dosya yolu veya kategori"
    }}
  ]
}}"""


def analyze_video(video: dict) -> dict | None:
    transcript = video.get("transcript", "")[:4000]
    if len(transcript) < 200:
        return None

    prompt = PROMPT_TEMPLATE.format(
        title=video.get("title", ""),
        channel=video.get("channel", ""),
        category=video.get("category", ""),
        transcript=transcript
    )

    try:
        result = subprocess.run(
            ["opencode", "run", "-m", "opencode-go/minimax-m3", prompt],
            capture_output=True, text=True, timeout=90
        )
        raw = result.stdout.strip()
        start, end = raw.find("{"), raw.rfind("}") + 1
        if start >= 0 and end > start:
            return json.loads(raw[start:end])
    except Exception as e:
        print(f"  Analiz hata ({video.get('video_id')}): {e}")
    return None


def run_analyze(transcribed: list[dict]) -> list[dict]:
    print(f"  Analiz edilecek: {len(transcribed)} video")
    analyzed = []

    with get_conn() as conn:
        for v in transcribed:
            # Kanal kategorisini bul
            row = conn.execute(
                """SELECT c.cat_num, c.category FROM channels c
                   JOIN videos vi ON vi.channel_id=c.id
                   WHERE vi.video_id=?""",
                (v["video_id"],)
            ).fetchone()
            if row:
                v["cat_num"]  = row["cat_num"]
                v["category"] = row["category"]

            print(f"  Analiz: {v['title'][:50]}...")
            result = analyze_video(v)
            if result:
                conn.execute(
                    """INSERT OR REPLACE INTO analyses
                       (video_id, summary, destination, insight, analyzed_at)
                       VALUES (?,?,?,?, datetime('now'))""",
                    (
                        v["video_id"],
                        result.get("summary", ""),
                        DESTINATION_MAP.get(v.get("cat_num", 0), ("", ""))[0],
                        json.dumps(result.get("items", []), ensure_ascii=False),
                    )
                )
                v["analysis"] = result
                analyzed.append(v)
                print(f"  ✓ {len(result.get('items', []))} şık")
            else:
                print(f"  ✗ Analiz alınamadı")
        conn.commit()

    print(f"  Analiz tamamlanan: {len(analyzed)}/{len(transcribed)}")
    return analyzed
