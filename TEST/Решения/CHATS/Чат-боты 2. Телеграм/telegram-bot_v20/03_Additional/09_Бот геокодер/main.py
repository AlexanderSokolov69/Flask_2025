import logging

from geocoder import get_ll_span
from telegram.ext import Application, CommandHandler, MessageHandler, filters

BOT_TOKEN = "TOKEN"
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def start(update, context):
    await update.message.reply_text("Я бот-геокодер. Ищу объекты на карте.")


async def geocoder(update, context):
    try:
        ll, spn = await get_ll_span(update.message.text)
        if ll and spn:
            point = "{ll},pm2vvl".format(ll=ll)
            static_api_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&spn={spn}&l=map&pt={point}"
            await context.bot.sendPhoto(update.message.chat.id, static_api_request, caption=update.message.text)
        else:
            await update.message.reply_text("По запросу ничего не найдено.")
    except RuntimeError as ex:
        await update.message.reply_text(str(ex))


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, geocoder))
    application.run_polling()


if __name__ == '__main__':
    main()
