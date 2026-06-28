import asyncio
import logging
import os
from http import HTTPStatus
from flask import Flask, Response, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
PORT = int(os.environ.get("PORT", 5000))
URL = os.environ.get("RENDER_EXTERNAL_URL", "https://your-app.onrender.com")

if not all([TOKEN, URL]):
    raise ValueError("TELEGRAM_BOT_TOKEN and RENDER_EXTERNAL_URL must be set.")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

application = Application.builder().token(TOKEN).updater(None).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("سلام! ربات جدید فعال است.")

application.add_handler(CommandHandler("start", start))

flask_app = Flask(__name__)

@flask_app.post("/webhook")
async def webhook() -> Response:
    try:
        await application.update_queue.put(Update.de_json(data=request.json, bot=application.bot))
        return Response(status=HTTPStatus.OK)
    except Exception as e:
        logging.error(f"خطا در وب‌هوک: {e}")
        return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)

@flask_app.get("/health")
async def health() -> Response:
    return Response("ربات فعال است ✅", status=HTTPStatus.OK, mimetype="text/plain")

async def main() -> None:
    webhook_url = f"{URL}/webhook"
    await application.bot.set_webhook(url=webhook_url)
    await application.initialize()
    await application.start()

    import uvicorn
    config = uvicorn.Config(flask_app, host="0.0.0.0", port=PORT, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())
