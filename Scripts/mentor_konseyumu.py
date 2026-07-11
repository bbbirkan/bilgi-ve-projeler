#!/usr/bin/env python3
"""
Mentörler Konseyumu — Sol + Fable tartışma modu
Kullanım: python3 mentor_konseyumu.py "konu veya soru"

Sol   = gpt-5.6-sol   (DevPass, $5/$30 per M)
Fable = claude-fable-5 (13 Temmuz'dan API'de, şimdilik claude-opus-4-8 yedek)
Sentez = GLM-5.2      (DevPass, $1.26/$3.96 per M — ucuz)
"""

import os, sys, requests, subprocess

# Env parse
with open("/root/.sovereign_env") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"): continue
        if "=" in line:
            k, v = line.split("=", 1)
            os.environ[k.strip()] = v.strip()

KEY = os.environ.get("LLMGATEWAY_KEY", "")
if not KEY:
    print("HATA: LLMGATEWAY_KEY bulunamadı")
    sys.exit(1)

URL = "https://api.llmgateway.io/v1/chat/completions"


def devpass(model, system, user, max_tokens=1200, provider=None):
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ],
        "temperature": 0.3,
        "max_tokens": max_tokens,
    }
    if provider:
        payload["provider"] = {"order": provider}
    headers = {"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"}
    r = requests.post(URL, headers=headers, json=payload, timeout=180)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]


def fable(konu):
    """Fable 5 (claude-fable-5) — 13 Temmuz'dan itibaren API'de aktif."""
    try:
        result = subprocess.run(
            ["claude", "-p", "--model", "claude-fable-5", konu],
            capture_output=True, text=True, timeout=180
        )
        out = result.stdout.strip()
        if not out:
            err = result.stderr.strip()
            print(f"[UYARI] Fable 5 yanıt vermedi. stderr: {err[:200]}")
            return f"[Fable 5 henüz erişilemez — 13 Temmuz'dan sonra dene]"
        return out
    except Exception as e:
        return f"[Fable 5 erişilemedi: {e}]"


def konseyum(konu):
    print(f"\n{'='*60}")
    print(f"MENTÖRLER KONSEYUMU")
    print(f"Konu: {konu}")
    print(f"{'='*60}\n")

    # TUR 1 — Sol ilk görüş
    print(">>> GÜNEŞ SOL — İlk Görüş...", flush=True)
    sol_1 = devpass(
        model="gpt-5.6-sol",
        system="Sen Güneş Sol, sovereign AI ekosistemi teknik ve strateji danışmanısın. Derinlikli, vizyoner, somut konuş. Türkçe.",
        user=f"Konu: {konu}\n\nGörüşünü ver. Max 300 kelime.",
        max_tokens=1000
    )
    print(f"SOL:\n{sol_1}\n")

    # TUR 1 — Fable ilk görüş
    print(">>> MENTOR FABLE — İlk Görüş...", flush=True)
    fable_1 = fable(
        f"Sen Mentor Fable, sovereign AI ekosistemi vizyoner danışmanısın. "
        f"Büyük resim, uzun vadeli bakış açısı. Türkçe.\n\n"
        f"Konu: {konu}\n\nGörüşünü ver. Max 300 kelime."
    )
    print(f"FABLE:\n{fable_1}\n")

    # TUR 2 — Sol Fable'a yanıt verir
    print(">>> GÜNEŞ SOL — Fable'a Yanıt...", flush=True)
    sol_2 = devpass(
        model="gpt-5.6-sol",
        system="Sen Güneş Sol. Fable'ın görüşünü oku, katıldıkların ve itiraz ettiğin noktaları belirt. Türkçe.",
        user=f"Konu: {konu}\n\nFable şunu dedi:\n{fable_1}\n\nYanıtın (max 200 kelime):",
        max_tokens=700
    )
    print(f"SOL (Tur 2):\n{sol_2}\n")

    # SENTEZ — GLM-5.2 (ucuz)
    print(">>> SENTEZ (GLM-5.2)...", flush=True)
    sentez = devpass(
        model="glm-5.2",
        system="Sen bir sentez yapıcısın. İki danışmanın görüşlerinden konsensüs ve eylem planı çıkar. Türkçe, madde madde.",
        user=f"Konu: {konu}\n\nSol (Tur1):\n{sol_1}\n\nFable:\n{fable_1}\n\nSol (Tur2):\n{sol_2}\n\nKonsensüs ve bu haftaki eylem planı (max 250 kelime):",
        max_tokens=1000,
        provider=["embercloud", "zai"]
    )

    print(f"{'='*60}")
    print(f"SENTEZ:\n{sentez}")
    print(f"{'='*60}\n")

    # Dosyaya kaydet
    import datetime
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    out = f"/root/sovereign-brain/decisions/konseyum_{ts}.md"
    os.makedirs("/root/sovereign-brain/decisions", exist_ok=True)
    with open(out, "w") as fp:
        fp.write(f"# Mentörler Konseyumu — {ts}\n\n")
        fp.write(f"**Konu:** {konu}\n\n")
        fp.write(f"## Sol (Tur 1)\n{sol_1}\n\n")
        fp.write(f"## Fable\n{fable_1}\n\n")
        fp.write(f"## Sol (Tur 2)\n{sol_2}\n\n")
        fp.write(f"## Sentez\n{sentez}\n")
    print(f"Kayıt: {out}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python3 mentor_konseyumu.py 'konu veya soru'")
        sys.exit(1)
    konu = " ".join(sys.argv[1:])
    konseyum(konu)
