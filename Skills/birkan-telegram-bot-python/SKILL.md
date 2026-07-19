---
name: telegram-bot-python
description: |
  python-telegram-bot v21.x production mimarileri. Async ApplicationBuilder,
  ContextTypes, webhook vs polling, birden fazla botu tek sunucuda paralel çalıştırma
  (BotManager class), PTB v21.4+ sigstore imzalı güvenlik.

  TRIGGER: telegram bot, python-telegram-bot, ptb, telegram python, telegram webhook,
           multi-bot, telegram asyncio
---

# Telegram Bot — Python PTB v21.x Production Rehberi

## Ne Zaman Kullan
- python-telegram-bot v20+ ile bot geliştirirken
- Eski `Updater` tabanlı kodu v21.x'e taşırken
- Tek sunucuda birden fazla bot çalıştırırken
- Webhook vs polling kararı verirken

---

## v21.x Temel Mimari

```python
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    filters, ContextTypes
)

# ContextTypes ile özel context tanımla
class BotData:
    user_sessions: dict = {}

class CustomContext(ContextTypes.DEFAULT_TYPE):
    pass

async def start(update: Update, context: CustomContext) -> None:
    await update.message.reply_text("Merhaba!")

async def echo(update: Update, context: CustomContext) -> None:
    await update.message.reply_text(update.message.text)

def build_app(token: str):
    return (
        ApplicationBuilder()
        .token(token)
        .context_types(ContextTypes(context=CustomContext))
        .build()
    )

async def main():
    app = build_app("YOUR_BOT_TOKEN")
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Polling modu (development)
    await app.run_polling(allowed_updates=Update.ALL_TYPES)
```

---

## Webhook (Production)

```python
from telegram.ext import ApplicationBuilder

async def main():
    app = (
        ApplicationBuilder()
        .token("TOKEN")
        .build()
    )
    
    app.add_handler(CommandHandler("start", start))
    
    # Webhook kurulumu
    await app.bot.set_webhook(
        url="https://yourdomain.com/webhook/TOKEN",
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True,
    )
    
    # FastAPI ile entegre:
    # app.update_queue → FastAPI endpoint'ten update besle
    async with app:
        await app.start()
        # FastAPI çalıştır, webhook gelince app.update_queue.put() çağır
        await app.stop()
```

### FastAPI + Webhook Entegrasyonu

```python
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import ApplicationBuilder
import asyncio

TOKEN = "YOUR_TOKEN"

bot_app = (
    ApplicationBuilder()
    .token(TOKEN)
    .build()
)

fastapi_app = FastAPI()

@fastapi_app.on_event("startup")
async def startup():
    await bot_app.initialize()
    await bot_app.start()

@fastapi_app.on_event("shutdown")  
async def shutdown():
    await bot_app.stop()
    await bot_app.shutdown()

@fastapi_app.post(f"/webhook/{TOKEN}")
async def webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, bot_app.bot)
    await bot_app.update_queue.put(update)
    return {"ok": True}
```

---

## Multi-Bot — Tek Sunucuda Paralel Bot

```python
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

class BotManager:
    """Birden fazla botu asyncio'da paralel çalıştır."""
    
    def __init__(self):
        self.bots: list = []
    
    def add_bot(self, token: str, handlers: list):
        app = (
            ApplicationBuilder()
            .token(token)
            .build()
        )
        for handler in handlers:
            app.add_handler(handler)
        self.bots.append(app)
        return app
    
    async def run_all(self):
        """Tüm botları aynı anda başlat, birbirini bloklamaz."""
        async with asyncio.TaskGroup() as tg:
            for app in self.bots:
                tg.create_task(self._run_bot(app))
    
    async def _run_bot(self, app):
        async with app:
            await app.run_polling(
                allowed_updates=Update.ALL_TYPES,
                close_loop=False,  # tek event loop'ta çalış
            )

# Kullanım
async def cmd_start_a(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot A burada!")

async def cmd_start_b(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot B burada!")

async def main():
    manager = BotManager()
    manager.add_bot("TOKEN_A", [CommandHandler("start", cmd_start_a)])
    manager.add_bot("TOKEN_B", [CommandHandler("start", cmd_start_b)])
    await manager.run_all()

if __name__ == "__main__":
    asyncio.run(main())
```

---

## Yaygın v20→v21 Göç Hataları

| Eski (v13/v20) | Yeni (v21.x) |
|----------------|--------------|
| `Updater(token).start_polling()` | `ApplicationBuilder().token().build()` |
| `CallbackContext` | `ContextTypes.DEFAULT_TYPE` |
| `dispatcher.add_handler()` | `app.add_handler()` |
| `updater.idle()` | `await app.run_polling()` |
| Sync handler | `async def handler(update, context)` |

---

## Güvenlik: Sigstore İmzası (v21.4+)

PTB v21.4'ten itibaren release'ler GitHub üzerinde sigstore ile kriptografik imzalanıyor:

```bash
# İmzayı doğrula
pip install sigstore
sigstore verify python-telegram-bot==21.x
```

---

## Kurulum

```bash
pip install "python-telegram-bot[webhooks,rate-limiter]"
# Rate limiter: otomatik Telegram API limit yönetimi
# Webhooks: FastAPI/aiohttp entegrasyonu için
```

---

## Kaynaklar
- PTB Docs: python-telegram-bot.readthedocs.io
- GitHub: github.com/python-telegram-bot/python-telegram-bot
- Examples: github.com/python-telegram-bot/python-telegram-bot/tree/master/examples
