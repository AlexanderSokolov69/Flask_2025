from telegram.ext import CommandHandler, ConversationHandler, Application
import logging

BOT_TOKEN = "TOKEN"
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def start(update, context):
    await update.message.reply_text("Для входа в музей введите команду /enter.")


async def to_enter(update, context):
    await update.message.reply_text("Добро пожаловать! Не забудьте сдать вещи в гардероб.")
    await update.message.reply_text("Вы находитесь в зале №1. Здесь представлено чучело мамонта.")
    await update.message.reply_text("Отсюда можно выйти (/exit) или перейти в зал №2 (/to2).")
    return 1


async def to_1(update, context):
    await update.message.reply_text("Вы находитесь в зале №1. Здесь представлено чучело мамонта.")
    await update.message.reply_text("Отсюда можно выйти (/exit) или перейти в зал №2 (/to2).")
    return 1


async def to_2(update, context):
    await update.message.reply_text("Вы находитесь в зале №2. Здесь представлено жилище пещерного человека.")
    await update.message.reply_text("Отсюда можно перейти в зал №3 (/to3).")
    return 2


async def to_3(update, context):
    await update.message.reply_text("Вы находитесь в зале №3. Здесь представлены орудия труда каменного века.")
    await update.message.reply_text("Отсюда можно перейти в зал №4 (/to4) или в зал №1 (/to1).")
    return 3


async def to_4(update, context):
    await update.message.reply_text(
        "Вы находитесь в зале №4. Здесь представлена неведомая диковина, найденная археологами.")
    await update.message.reply_text("Отсюда можно перейти в зал №1 (/to1).")
    return 4


async def to_exit(update, context):
    await update.message.reply_text("Всего доброго! Не забудьте забрать вещи из гардероба.")
    return ConversationHandler.END


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    museum_handler = ConversationHandler(
        entry_points=[CommandHandler('enter', to_enter), CommandHandler('start', start)],

        states={
            1: [CommandHandler('to2', to_2), CommandHandler('exit', to_exit)],
            2: [CommandHandler('to3', to_3)],
            3: [CommandHandler('to1', to_1), CommandHandler('to4', to_4)],
            4: [CommandHandler('to1', to_1)]
        },
        fallbacks=[]
    )

    application.add_handler(museum_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
