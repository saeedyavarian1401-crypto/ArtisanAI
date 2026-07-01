import logging
import os
from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
PORT = int(os.environ.get("PORT", 5000))

if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set.")

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# ========================= ربات =========================
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("🎨 باز کردن سازنده تصویر", web_app=WebAppInfo(url="https://perchance.org/imageconstructor"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("سلام! برای ساخت تصویر روی دکمه زیر کلیک کن:", reply_markup=reply_markup)

application.add_handler(CommandHandler("start", start))

# ========================= Flask =========================
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        update = Update.de_json(request.get_json(force=True), application.bot)
        application.process_update(update)
        return "ok", 200
    except Exception as e:
        logging.error(f"خطا در وب‌هوک: {e}")
        return "error", 500

@app.route("/health")
def health():
    return "ربات فعال است ✅", 200

@app.route("/")
def home():
    return "ربات در حال اجراست", 200

# ========================= اجرا =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
