import logging
from telegram.ext import Updater, CommandHandler
from config import BOT_TOKEN

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = BOT_TOKEN


def help(update, context):
    update.message.reply_text(
        "Я бот справочник.")


def address(update, context):
    update.message.reply_text(
        "Адрес: г. Москва, ул. Льва Толстого, 16")


def phone(update, context):
    update.message.reply_text("Телефон: +7(495)776-3030")


def site(update, context):
    update.message.reply_text(
        "Сайт: http://www.yandex.ru/company")


def work_time(update, context):
    update.message.reply_text(
        "Время работы: круглосуточно.")


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("address", address))
    dp.add_handler(CommandHandler("phone", phone))
    dp.add_handler(CommandHandler("site", site))
    dp.add_handler(CommandHandler("work_time", work_time))
    dp.add_handler(CommandHandler("help", help))
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
