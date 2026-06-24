from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.constants import ParseMode

# ==========================
# НАСТРОЙКИ
# ==========================
BOT_TOKEN = "8406335141:AAG9LCls54PJmcZc-goxauzRvSzwQ42Q3d8"

PHOTO_URL = "https://iili.io/Cu5hlPR.png"  # ссылка на фото
MINI_APP_URL = "https://tstwbstrstnnl123.netlify.app"         # ссылка на мини-приложение

CAPTION = """
<b>🔥 Добро пожаловать в РосТуннель (a.k.a. РСТ)!</b>

<blockquote>
➡️ ТГК: <a href="https://t.me/rostunnel">тык</a>

➡️ ТГ-прокси: <a href="https://t.me/proxy?server=tourist.maxmir.ru&port=443&secret=ee270cc417222fb80a4b0e3483d7478a2a31632e7275">тык</a>
</blockquote>

Это наш официальный бот, который работает в режиме Telegram Mini App.

<i>Если вы используете нашего бота, сервис, подписки или другое, вы автоматически соглашаетесь с <a href="https://telegra.ph/YUridicheskoe-uvedomlenie-disklejmer-01-29">нашими правилами и условиями использования</a>.</i>

Нажмите на кнопку ниже, чтобы открыть мини-приложение ⬇️
"""

# ==========================
# КОМАНДА /start
# ==========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                text="Открыть приложение",
                web_app=WebAppInfo(url=MINI_APP_URL)
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo=PHOTO_URL,
        caption=CAPTION,
        parse_mode=ParseMode.HTML,
        reply_markup=reply_markup
    )

# ==========================
# ЗАПУСК БОТА
# ==========================
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
