from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN  # импортируем токен
import logging

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

bot = Bot(token=BOT_TOKEN)  # Инициализируем бота здесь надо указать свой токен, полученный от @BotFather.
dp = Dispatcher(bot)  # Инициализируем диспечера сообщений


@dp.message_handler(commands=['start'])  # декоратор дли обработчика команды start
async def process_start_command(message: types.Message):
    """
    Создаем и регистрируем в диспечере асинхронный обработчик сообщений.
    В пераметре message создержится вся информация о сообщении - посмотрите в отладчике.
    """
    await message.reply("Привет!\nНапиши мне что-нибудь!")  # отправляет ответ на сообщение


@dp.message_handler(commands=['help'])  # декоратор дли обработчика команды help
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отправлю этот текст тебе в ответ!")


@dp.message_handler()  # декоратор дли обработчика прочих сообщений
async def echo_message(message: types.Message):
    await message.answer(message.text)  # отправляет обратно новое сообщение с тем же текстом


if __name__ == '__main__':
    executor.start_polling(dp)  # начинаем принимать сообщения
