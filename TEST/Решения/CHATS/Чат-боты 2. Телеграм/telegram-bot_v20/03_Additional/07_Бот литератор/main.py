from telegram.ext import CommandHandler, MessageHandler, filters, ConversationHandler, Application

import logging

BOT_TOKEN = "TOKEN"
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

poem = """
Белеет парус одинокий
В тумане моря голубом.
Что ищет он в стране далекой?
Что кинул он в краю родном?
""".strip().split("\n")

LAST_READ = "last_read"

WAIT_FOR_NEXT_STRING, WAIT_REPEAT_ALL, ENABLE_SUPHLER = 1, 2, 3


async def start(update, context):
    await update.message.reply_text("Давайте почитаем стихотворение по строчке по очереди.")
    await update.message.reply_text("Я начну.")
    await update.message.reply_text(poem[0])
    context.user_data[LAST_READ] = 0
    return WAIT_FOR_NEXT_STRING


async def continue_or_repeat(update, user_data, next_string_index):
    if next_string_index + 1 < len(poem):  # Есть, что прочитать дальше.
        next_string_index += 1
        await update.message.reply_text(poem[next_string_index])
        user_data[LAST_READ] = next_string_index

    if next_string_index + 1 < len(poem):  # Есть, что ждать дальше.
        return WAIT_FOR_NEXT_STRING
    else:  # Закончили.
        await update.message.reply_text("Стихотворение закончилось. Хотите еще раз? (/yes /no)")
        return WAIT_REPEAT_ALL


def normalize(string):
    return string.lower().replace(".", "").replace(",", "").replace("-", "").replace("?", "").replace("!", "").replace(
        ":", "")


async def get_next_string(update, context):
    next_string_index = context.user_data[LAST_READ] + 1
    if normalize(poem[next_string_index]) == normalize(update.message.text):  # Правильная строчка.
        return await continue_or_repeat(update, context.user_data, next_string_index)
    else:  # Неправильная строчка.
        await update.message.reply_text("Нет, не так. Попробуйте еще раз или позовите суфлера (/suphler).")
        return ENABLE_SUPHLER


async def suphler(update, context):
    next_string_index = context.user_data[LAST_READ] + 1
    await update.message.reply_text(poem[next_string_index])
    return await continue_or_repeat(update, context.user_data, next_string_index)


async def stop(update, context):
    await update.message.reply_text("До новых встреч!")
    context.user_data[LAST_READ] = 0
    return ConversationHandler.END


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    museum_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            WAIT_FOR_NEXT_STRING: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, get_next_string)
            ],
            ENABLE_SUPHLER: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, get_next_string),
                CommandHandler('suphler', suphler)
            ],
            WAIT_REPEAT_ALL: [
                CommandHandler('yes', start),
                CommandHandler('no', stop)
            ]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    application.add_handler(museum_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
