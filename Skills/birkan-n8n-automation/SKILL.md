---
name: n8n-automation
description: |
  n8n iş akışı otomasyonu rehberi. v2.x Native Python Runner yapılandırması,
  N8N_PYTHON_BINARY ayarı, Pyodide → Native geçiş, webhook entegrasyonu,
  FastAPI/Prefect orkestrasyon desenleri.

  TRIGGER: n8n, workflow automation, n8n python, n8n code node, webhook, n8n docker
---

# n8n Automation — Python + Orkestrasyon Rehberi

## Ne Zaman Kullan
- n8n Code Node'da Python kodu çalıştırırken
- "Python runner unavailable" hatası alındığında
- n8n → FastAPI veya Prefect entegrasyonu kurarken
- Webhook tabanlı iş akışı tasarlarken

---

## Kritik: v2.x Native Python Runner

n8n v2.x'te Python çalıştırma mimarisi değişti:

| | Eski (Pyodide) | Yeni (Native Runner) |
|--|----------------|---------------------|
| Ortam | Tarayıcı/WebAssembly | Sunucu process |
| Kurulum | Otomatik | Python binary gerekli |
| Kütüphaneler | Pyodide uyumlu | pip install gerekli |
| Windows | Çalışıyordu | N8N_PYTHON_BINARY şart |

### "Python runner unavailable" Hatasını Çöz

```bash
# 1. Python binary yolunu bul
which python3   # Linux/Mac
where python    # Windows

# 2. n8n ortam değişkenini ayarla
# .env dosyasına veya systemd service'e ekle:
N8N_PYTHON_BINARY=/usr/bin/python3

# Windows örneği:
# N8N_PYTHON_BINARY=C:\Python311\python.exe

# 3. n8n'i yeniden başlat
systemctl restart n8n
```

### Harici Kütüphane Kurma (External Mode)

```bash
# n8n process'inin gördüğü Python environment'a kur
/usr/bin/python3 -m pip install requests pandas numpy

# Veya venv kullanıyorsan:
/root/n8n-venv/bin/pip install requests pandas
N8N_PYTHON_BINARY=/root/n8n-venv/bin/python
```

---

## Docker Ortamında n8n Python

```yaml
# docker-compose.yml
services:
  n8n:
    image: n8nio/n8n
    environment:
      - N8N_PYTHON_BINARY=/usr/bin/python3
    volumes:
      - n8n_data:/home/node/.n8n
```

Docker içinde Python yoksa:
```dockerfile
# Özel n8n image
FROM n8nio/n8n
USER root
RUN apk add --no-cache python3 py3-pip
RUN pip3 install requests pandas numpy
USER node
```

---

## Webhook Entegrasyon Desenleri

### n8n → FastAPI (Async)

```python
# FastAPI tarafı — n8n'den webhook al
from fastapi import FastAPI, BackgroundTasks
import httpx

app = FastAPI()

@app.post("/n8n-trigger")
async def handle_n8n_webhook(payload: dict, background: BackgroundTasks):
    background.add_task(process_task, payload)
    return {"status": "accepted"}

async def process_task(payload: dict):
    # İşlemi yap, sonucu n8n'e geri bildir
    async with httpx.AsyncClient() as client:
        await client.post(
            payload["callback_url"],
            json={"result": "done", "data": ...}
        )
```

```javascript
// n8n Code Node — FastAPI'ye istek gönder
const response = await $http.post('http://localhost:8000/n8n-trigger', {
  data: $input.item.json,
  callback_url: $execution.resumeUrl  // n8n resume webhook
});
return [{ json: response.data }];
```

### Prefect ile Orkestrasyon

```python
# Prefect flow — n8n'den tetiklenen kompleks pipeline
from prefect import flow, task
import httpx

@task
def fetch_data(source_url: str):
    with httpx.Client() as client:
        return client.get(source_url).json()

@task
def process(data: dict):
    # AI işlemi, dönüşüm vb.
    return transformed_data

@flow
def n8n_triggered_pipeline(webhook_payload: dict):
    data = fetch_data(webhook_payload["source"])
    result = process(data)
    return result

# FastAPI endpoint üzerinden n8n tetikler:
# POST /run-flow → Prefect flow başlar
```

---

## Yaygın Hatalar

| Hata | Neden | Çözüm |
|------|-------|-------|
| `Python runner unavailable` | N8N_PYTHON_BINARY ayarsız | Binary yolunu env var'a ekle |
| `ModuleNotFoundError` | Kütüphane n8n'in Python'ına kurulu değil | N8N_PYTHON_BINARY'nin işaret ettiği Python'a pip install et |
| `Timeout` | Uzun süreli Python işlemi | BackgroundTasks veya Prefect kullan, n8n'e hemen 200 dön |
| Pyodide kodu çalışmıyor | v2.x Native'e geçince eski API yok | `import asyncio` yerine sync kod yaz |

---

## Kaynaklar
- n8n Native Python Runner: community.n8n.io
- Prefect Docs: docs.prefect.io
- n8n + FastAPI pattern: reddit.com/r/n8n
