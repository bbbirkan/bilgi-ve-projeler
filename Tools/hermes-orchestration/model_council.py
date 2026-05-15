#!/usr/bin/env python3
"""
Birkan Hermes Model Council

Purpose:
- Call selected OpenRouter models as text-only advisors.
- Do NOT rely on tool calling from advisor models.
- Send compact problem packets only.
- Return short Turkish advisory summaries for Hermes main model to synthesize.

Usage:
  python3 ~/.hermes/scripts/model_council.py --mode upper --question "..."
  python3 ~/.hermes/scripts/model_council.py --mode huge-file --question "..."

🤖 *Bu doküman Hermes Agent tarafından oluşturuldu*
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

ENV_PATH = os.path.expanduser("~/.hermes/.env")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

UPPER_MODELS = [
    ("GPT-5.5", "openai/gpt-5.5"),
    ("Claude Opus 4.6", "anthropic/claude-opus-4.6"),
    ("DeepSeek V4 Pro", "deepseek/deepseek-v4-pro"),
    ("Claude Opus 4.7", "anthropic/claude-opus-4.7"),
]

ALT_MODELS = [
    ("GLM-4.7", "z-ai/glm-4.7"),
    ("Gemini 3 Flash", "google/gemini-3-flash-preview"),
    ("MiniMax M2.5", "minimax/minimax-m2.5"),
    ("DeepSeek V4 Flash", "deepseek/deepseek-v4-flash"),
]

HUGE_FILE_MODELS = [
    ("DeepSeek V4 Flash", "deepseek/deepseek-v4-flash"),
    ("GLM-4.7", "z-ai/glm-4.7"),
    ("Gemini 3 Flash", "google/gemini-3-flash-preview"),
]


def load_env():
    if not os.path.exists(ENV_PATH):
        return
    with open(ENV_PATH, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k, v.strip().strip('"').strip("'"))


def call_model(model_id: str, question: str, timeout: int = 90, retry: int = 1) -> dict:
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        return {"ok": False, "error": "OPENROUTER_API_KEY yok"}

    prompts = [
        (
            "Sen Birkan'ın Hermes orkestrasyon sisteminde kısa danışman modelsin. "
            "Tool kullanma. Türkçe yaz. En fazla 5 madde ver. "
            "Belirsizlik varsa açıkça söyle. Uydurma veri yazma."
        ),
        (
            "Kısa Türkçe danışman cevabı ver. Tool kullanma. "
            "En fazla 5 madde. Boş cevap verme."
        ),
    ]

    last_error = None
    attempts = max(1, retry + 1)
    for attempt in range(attempts):
        system = prompts[min(attempt, len(prompts) - 1)]
        payload = {
            "model": model_id,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": question},
            ],
            "temperature": 0.2,
            "max_tokens": 1200 if "glm-4.7" in model_id else (900 if attempt else 700),
        }
        # GLM-4.7 çok reasoning token üretebiliyor; low reasoning content'in boş kalmasını engelliyor.
        if "glm-4.7" in model_id:
            payload["reasoning"] = {"effort": "low"}
        req = urllib.request.Request(
            OPENROUTER_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://hermes-agent.local",
                "X-Title": "Birkan Hermes Model Council",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                body = json.loads(r.read().decode("utf-8", "ignore"))
            msg = (body.get("choices") or [{}])[0].get("message") or {}
            text = (msg.get("content") or "").strip()
            if text:
                return {"ok": True, "text": text, "attempt": attempt + 1}
            last_error = {"error": "Boş cevap", "raw": str(body)[:500]}
        except urllib.error.HTTPError as e:
            err = e.read().decode("utf-8", "ignore")[:800]
            last_error = {"http": e.code, "error": err}
        except Exception as e:
            last_error = {"error": repr(e)}
        time.sleep(0.5)

    out = {"ok": False}
    out.update(last_error or {"error": "Bilinmeyen hata"})
    return out


def select_models(mode: str):
    if mode == "upper":
        return UPPER_MODELS
    if mode == "alt":
        return ALT_MODELS
    if mode == "huge-file":
        return HUGE_FILE_MODELS
    raise SystemExit(f"Unknown mode: {mode}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["upper", "alt", "huge-file"], default="upper")
    parser.add_argument("--question", required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    load_env()
    models = select_models(args.mode)
    results = []
    for name, model_id in models:
        started = time.time()
        res = call_model(model_id, args.question)
        res.update({"name": name, "model_id": model_id, "seconds": round(time.time() - started, 2)})
        results.append(res)
        time.sleep(0.4)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    print(f"# Model Council — mode={args.mode}\n")
    for r in results:
        status = "OK" if r.get("ok") else "FAIL"
        print(f"## {r['name']} — `{r['model_id']}` — {status} — {r['seconds']}s")
        if r.get("ok"):
            print(r["text"].strip())
        else:
            print(str(r.get("error") or r)[:1000])
        print()


if __name__ == "__main__":
    main()
