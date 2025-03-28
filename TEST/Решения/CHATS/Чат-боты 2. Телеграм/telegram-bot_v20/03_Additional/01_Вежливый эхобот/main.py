import logging
from telegram.ext import Application, MessageHandler, filters

TOKEN = 'BOT_TOKEN'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


# Определяем функцию-обработчик сообщений.
async def echo(update, context):
    await update.message.reply_text(f'Я получил сообщение "{update.message.text}".')


def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT, echo))

    logger.info('Bot started')
    application.run_polling()


if __name__ == '__main__':
    main()
