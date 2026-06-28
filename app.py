import asyncio
import html
import logging
import os
from http import HTTPStatus
from flask import Flask, Response, request
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes

# ========================= تنظیمات اولیه =========================
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
ADMIN_CHAT_ID = os.environ.get("ADMIN_CHAT_ID")
PORT = int(os.environ.get("PORT", 5000))
URL = os.environ.get("RENDER_EXTERNAL_URL", "https://your-app.onrender.com")

# اگر متغیرهای محیطی تنظیم نشده باشند، برنامه با خطا مواجه می‌شود.
if not all([TOKEN, ADMIN_CHAT_ID, URL]):
    raise ValueError("TELEGRAM_BOT_TOKEN, ADMIN_CHAT_ID, and RENDER_EXTERNAL_URL must be set.")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# ========================= تعریف ربات =========================
application = Application.builder().token(TOKEN).updater(None).build()

# ========================= تعریف هندلرها =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """پاسخ به دستور /start"""
    user = update.effective_user
    await update.message.reply_html(
        f"سلام {user.mention_html()}! من یک ربات نمونه هستم. برای شروع از دستورات استفاده کنید."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """پاسخ به دستور /help"""
    await update.message.reply_text("من یک ربات ساده هستم. هنوز کار خاصی بلد نیستم!")

# ثبت هندلرها در برنامه
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))

# ========================= راه‌اندازی وب‌هوک با Flask =========================
flask_app = Flask(__name__)

@flask_app.post("/webhook")
async def webhook() -> Response:
    """مسیر وب‌هوک برای دریافت آپدیت‌ها از تلگرام"""
    try:
        await application.update_queue.put(Update.de_json(data=request.json, bot=application.bot))
        return Response(status=HTTPStatus.OK)
    except Exception as e:
        logger.error(f"خطا در پردازش وب‌هوک: {e}")
        return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)

@flask_app.get("/health")
async def health() -> Response:
    """مسیر سلامت برای چک کردن وضعیت ربات توسط Render"""
    return Response("ربات فعال است ✅", status=HTTPStatus.OK, mimetype="text/plain")

# ========================= تابع اصلی برای اجرا =========================
async def main() -> None:
    """تنظیم وب‌هوک و شروع سرور Flask"""
    webhook_url = f"{URL}/webhook"
    await application.bot.set_webhook(url=webhook_url, allowed_updates=Update.ALL_TYPES)
    logger.info(f"Webhook set to {webhook_url}")

    await application.initialize()
    await application.start()

    import uvicorn
    config = uvicorn.Config(flask_app, host="0.0.0.0", port=PORT, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())
