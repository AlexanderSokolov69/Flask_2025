import logging

import translators.server as ts #pip install translate-api
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import ReplyKeyboardMarkup

BOT_TOKEN = "TOKEN"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)
reply_keyboard = [['/ru_en', '/en_ru', '/ru_tr', '/tr_ru']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

TRANS_DIRECTION_KEY = "trans-direction"


async def start(update, context):
    await update.message.reply_text("Я бот-переводчик. Перевожу слова.", reply_markup=markup)


async def translater(updater, context):
    langs = context.user_data.get(TRANS_DIRECTION_KEY, "ru-en").split("-")
    logger.info(f"received '{updater.message.text}' for translate")
    res = ts.google(updater.message.text, from_language=langs[0], to_language=langs[1])
    logger.info(f"translation result '{res}'")
    await updater.message.reply_text(res)


async def ru_en(update, context):
    context.user_data[TRANS_DIRECTION_KEY] = "ru-en"
    await update.message.reply_text("Используем направление перевода: " + context.user_data[TRANS_DIRECTION_KEY])


async def en_ru(update, context):
    context.user_data[TRANS_DIRECTION_KEY] = "en-ru"
    await update.message.reply_text("Используем направление перевода: " + context.user_data[TRANS_DIRECTION_KEY])


async def ru_tr(update, context):
    context.user_data[TRANS_DIRECTION_KEY] = "ru-tr"
    await update.message.reply_text("Используем направление перевода: " + context.user_data[TRANS_DIRECTION_KEY])


async def tr_ru(update, context):
    context.user_data[TRANS_DIRECTION_KEY] = "tr-ru"
    await update.message.reply_text("Используем направление перевода: " + context.user_data[TRANS_DIRECTION_KEY])


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ru_en", ru_en))
    application.add_handler(CommandHandler("en_ru", en_ru))
    application.add_handler(CommandHandler("ru_tr", ru_tr))
    application.add_handler(CommandHandler("tr_ru", tr_ru))
    application.add_handler(MessageHandler(filters.TEXT, translater))

    application.run_polling()


if __name__ == '__main__':
    main()
