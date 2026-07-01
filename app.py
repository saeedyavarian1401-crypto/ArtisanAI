from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

# ... بقیه کد ربات ...

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ساخت دکمه WebApp
    keyboard = [
        [InlineKeyboardButton(
            "🎨 باز کردن سازنده تصویر",
            web_app=WebAppInfo(url="https://perchance.org/imageconstructor")
        )]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "سلام! برای ساخت تصویر روی دکمه زیر کلیک کن:",
        reply_markup=reply_markup
    )

# این تابع را به جای تابع start قبلی خود قرار دهید.
