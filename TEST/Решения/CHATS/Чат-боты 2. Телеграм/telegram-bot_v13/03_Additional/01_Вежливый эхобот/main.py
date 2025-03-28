from telegram.ext import Updater, MessageHandler, Filters
import logging

TOKEN = 'BOT_TOKEN'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


# Определяем функцию-обработчик сообщений.
def echo(update, context):
    update.message.reply_text(f'Я получил сообщение "{update.message.text}".')


def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    print('Bot started')
    updater.idle()


if __name__ == '__main__':
    main()
