from datetime import datetime
from telegram.ext import Application, MessageHandler, filters, CommandHandler
import logging

TOKEN = 'BOT_TOKEN'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def echo(update, context):
    await update.message.reply_text(update.message.text)


async def start(update, context):
    await update.message.reply_text("Привет! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!")


async def help(update, context):
    await update.message.reply_text("Я пока не умею помогать... Я только ваше эхо.")


async def get_time(update, context):
    await update.message.reply_text(datetime.now().strftime("%H:%M:%S"))


async def get_date(update, context):
    await update.message.reply_text(datetime.now().strftime("%d/%m/%Y"))


def main():
    application = Application.builder().token(TOKEN).build()
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    application.add_handler(text_handler)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("time", get_time))
    application.add_handler(CommandHandler("date", get_date))

    logger.info('Bot started')
    application.run_polling()


if __name__ == '__main__':
    main()
