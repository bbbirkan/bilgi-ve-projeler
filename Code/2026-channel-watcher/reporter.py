"""Sovereign Günlük Email — Gmail SMTP, tek mail, iki bölüm"""

import smtplib, html as _html
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ET_TZ      = ZoneInfo("America/New_York")
TO_EMAIL   = "8birkan@gmail.com"
FROM_EMAIL = "sovereignanvilon@gmail.com"
APP_PASS   = "xstlaliovxuvueeh"


# ── Yardımcılar ───────────────────────────────────────────────────────────────

def _read_yapilacaklar():
    try:
        return Path("/root/YAPILACAKLAR.md").read_text()
    except Exception:
        return ""

def _parse_tasks(content):
    pending, done = [], []
    for line in content.splitlines():
        s = line.strip()
        if "⬜" in s and "BEN YAPACAĞIM" not in s:
            t = s.lstrip("- ").replace("⬜","").strip()
            if t and len(t) > 3:
                pending.append(t)
        elif "✅" in s:
            t = s.lstrip("- ").replace("✅","").strip()
            if t and len(t) > 3:
                done.append(t)
    return pending, done[:6]

def _daemon_voice() -> str:
    today = datetime.now(ET_TZ).strftime("%Y-%m-%d")
    rpt   = Path(f"/root/2026-sovereign/reports/{today}_daemon_run.md")
    if rpt.exists():
        txt = rpt.read_text()
        if "[VOICE]" in txt:
            idx   = txt.rindex("[VOICE]")
            after = txt[idx + len("[VOICE]"):].strip()
            return after.split("\n\n")[0].strip()
    return ""


# ── HTML Builder ──────────────────────────────────────────────────────────────

def build_html(analyzed: list, date_str: str) -> str:
    pending, done = _parse_tasks(_read_yapilacaklar())
    ai_voice      = _daemon_voice()

    # ── AI Özeti bloğu
    ai_html = ""
    if ai_voice:
        ai_html = f"""
<div style="background:#0f172a;border-radius:12px;padding:22px 26px;margin-bottom:28px">
  <div style="color:#38bdf8;font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:10px">🤖 Sovereign AI — Bugünün Özeti</div>
  <p style="color:#e2e8f0;font-size:18px;line-height:1.75;margin:0">{ai_voice}</p>
</div>"""

    # ── Görev satırları
    task_rows = ""
    for i, t in enumerate(pending, 1):
        task_rows += f"""
<tr>
  <td style="padding:7px 10px 7px 0;vertical-align:top;width:28px">
    <div style="background:#f59e0b;color:#fff;width:22px;height:22px;border-radius:50%;font-weight:800;font-size:11px;text-align:center;line-height:22px">{i}</div>
  </td>
  <td style="padding:7px 0;font-size:14px;color:#111827;line-height:1.5;border-bottom:1px solid #f8fafc">{_html.escape(t)}</td>
</tr>"""

    done_rows = ""
    for t in done:
        done_rows += f"""
<tr>
  <td style="padding:8px 0;font-size:14px;color:#9ca3af;text-decoration:line-through" colspan="2">✅ {_html.escape(t)}</td>
</tr>"""

    # ── Video kartları — global numaralı liste, alt dallar a/b/c/d/e
    LETTERS = "abcdefghij"
    video_cards = ""
    global_n = 0  # tüm videolardaki toplam öğrenim sayısı

    if analyzed:
        for v in analyzed:
            a    = v.get("analysis", {})
            cat  = v.get("category", "")
            ch   = v.get("channel", "")
            ttl  = v.get("title", "")
            url  = v.get("url", "#")
            pub  = v.get("published_at", "")[:10]
            items = a.get("items", [])

            global_n += 1
            vid_n = global_n  # bu videonun numarası

            # Alt dallar: birden fazla item varsa a/b/c, tek item ise sadece numara
            items_html = ""
            if len(items) == 1:
                item = items[0]
                items_html = f"""
<div style="display:flex;gap:14px;margin-bottom:10px">
  <div>
    <div style="font-size:16px;font-weight:600;color:#111827;margin-bottom:4px">{_html.escape(item['insight'])}</div>
    <div style="font-size:14px;color:#4b5563;margin-bottom:6px">→ {_html.escape(item['action'])}</div>
    <code style="font-size:12px;background:#f0fdf4;border:1px solid #bbf7d0;border-radius:4px;padding:2px 8px;color:#059669">{_html.escape(item['destination'])}</code>
  </div>
</div>"""
            else:
                for j, item in enumerate(items):
                    lbl = LETTERS[j] if j < len(LETTERS) else str(j+1)
                    items_html += f"""
<div style="display:flex;gap:12px;margin-bottom:14px">
  <div style="flex-shrink:0;background:#e0e7ff;color:#3730a3;width:26px;height:26px;border-radius:50%;font-weight:800;font-size:13px;text-align:center;line-height:26px">{lbl}</div>
  <div>
    <div style="font-size:15px;font-weight:600;color:#111827;margin-bottom:3px">{_html.escape(item['insight'])}</div>
    <div style="font-size:13px;color:#4b5563;margin-bottom:5px">→ {_html.escape(item['action'])}</div>
    <code style="font-size:11px;background:#f0fdf4;border:1px solid #bbf7d0;border-radius:4px;padding:2px 7px;color:#059669">{_html.escape(item['destination'])}</code>
  </div>
</div>"""

            # Yanıt kodları — tek item ise "5", çoksa "5a 5b 5c"
            if len(items) <= 1:
                reply_codes = f'<code style="background:#e2e8f0;padding:2px 7px;border-radius:4px">{date_str}/{vid_n}</code>'
            else:
                reply_codes = " ".join(
                    f'<code style="background:#e2e8f0;padding:2px 7px;border-radius:4px">{date_str}/{vid_n}{LETTERS[j]}</code>'
                    for j in range(min(len(items), len(LETTERS)))
                )

            video_cards += f"""
<div style="border:1px solid #e5e7eb;border-radius:12px;overflow:hidden;margin-bottom:20px">
  <div style="background:#f8fafc;padding:14px 20px;border-bottom:1px solid #e5e7eb">
    <div style="font-size:12px;color:#6b7280;margin-bottom:5px">{_html.escape(cat)} · {_html.escape(ch)} · {pub}</div>
    <a href="{url}" style="font-size:18px;font-weight:700;color:#111827;text-decoration:none;line-height:1.4">{vid_n}. {_html.escape(ttl)}</a>
  </div>
  <div style="padding:18px 20px">
    <div style="background:#f8fafc;border-left:4px solid #2563eb;padding:12px 16px;border-radius:0 8px 8px 0;margin-bottom:18px">
      <p style="font-size:15px;color:#374151;line-height:1.7;margin:0">{_html.escape(a.get('summary','—'))}</p>
    </div>
    {items_html}
  </div>
  <div style="background:#f8fafc;padding:10px 20px;border-top:1px solid #e5e7eb;font-size:13px;color:#6b7280">
    Sisteme eklemek için yanıtla:&nbsp;{reply_codes}
  </div>
</div>"""

    no_video_msg = ""
    if not analyzed:
        no_video_msg = """<p style="color:#6b7280;font-size:15px;text-align:center;padding:24px 0">Bugün yeni video bulunamadı.</p>"""

    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>* {{box-sizing:border-box}} a {{color:inherit}}</style></head>
<body style="margin:0;padding:0;background:#f1f5f9;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,sans-serif">
<div style="max-width:640px;margin:0 auto;padding:24px 16px">

  <!-- HEADER -->
  <div style="background:linear-gradient(135deg,#0f172a 0%,#1e3a5f 100%);border-radius:16px;padding:28px 30px;margin-bottom:20px">
    <div style="color:#38bdf8;font-size:11px;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;margin-bottom:10px">SOVEREIGN AI · GÜNLÜK RAPOR</div>
    <div style="color:#fff;font-size:32px;font-weight:800;letter-spacing:-0.5px;margin-bottom:4px">☀️ {date_str}</div>
    <div style="display:flex;gap:16px;margin-top:10px">
      <span style="color:#64748b;font-size:12px">📺 {len(analyzed)} video</span>
      <span style="color:#64748b;font-size:12px">💡 {global_n} öğrenim</span>
      <span style="color:#64748b;font-size:12px">📋 {len(pending)} görev</span>
    </div>
  </div>

  <!-- AI ÖZETİ -->
  {ai_html}

  <!-- VİDEOLAR — önce gelir -->
  <div style="background:#fff;border-radius:16px;padding:24px 26px;margin-bottom:20px;border:1px solid #e5e7eb">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:18px">
      <div style="font-size:14px;font-weight:700;color:#2563eb;text-transform:uppercase;letter-spacing:1px">📺 Bugünün Videoları</div>
      {"<div style='font-size:12px;color:#6b7280'>Eklemek istediğini yanıtla → ben işlerim</div>" if analyzed else ""}
    </div>
    {video_cards}
    {no_video_msg}
  </div>

  <!-- GÖREVLER — ikinci sıra -->
  <div style="background:#fff;border-radius:16px;padding:24px 26px;margin-bottom:20px;border:1px solid #e5e7eb">
    <div style="font-size:14px;font-weight:700;color:#f59e0b;text-transform:uppercase;letter-spacing:1px;margin-bottom:16px">📋 Bekleyen Görevler — {len(pending)} adet</div>
    <table style="width:100%;border-collapse:collapse">{task_rows}</table>
    {('<div style="margin-top:16px;padding-top:14px;border-top:1px solid #f1f5f9"><div style="font-size:11px;color:#9ca3af;font-weight:600;text-transform:uppercase;letter-spacing:.5px;margin-bottom:8px">Son Tamamlananlar</div><table style="width:100%;border-collapse:collapse">' + done_rows + '</table></div>') if done_rows else ''}
  </div>

  <!-- FOOTER -->
  <div style="text-align:center;padding:6px 0">
    <p style="color:#94a3b8;font-size:11px;margin:0">202 kanal · Sovereign Channel Watcher · Her sabah 07:00 ET</p>
  </div>

</div>
</body></html>"""


# ── Gönder ────────────────────────────────────────────────────────────────────

def send_email(analyzed: list) -> bool:
    date_str = datetime.now(ET_TZ).strftime("%Y-%m-%d")
    html     = build_html(analyzed, date_str)

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"☀️ Sovereign Günlük Rapor — {date_str}"
    msg["From"]    = FROM_EMAIL
    msg["To"]      = TO_EMAIL
    msg.attach(MIMEText(html, "html", "utf-8"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(FROM_EMAIL, APP_PASS)
            smtp.send_message(msg)
        print(f"  ✅ Email gönderildi → {TO_EMAIL}")
        return True
    except Exception as e:
        print(f"  ❌ Email hata: {e}")
        return False
