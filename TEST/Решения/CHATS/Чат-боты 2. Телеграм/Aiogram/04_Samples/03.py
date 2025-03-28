import logging
from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = [[KeyboardButton('/address'), KeyboardButton('/phone')],
                  [KeyboardButton('/site'), KeyboardButton('/work_time')], [KeyboardButton("/stop")]]
kb = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

bot = Bot(token=BOT_TOKEN)  # Инициализируем бота здесь надо указать свой токен, полученный от @BotFather.
dp = Dispatcher(bot)  # Инициализируем диспечера сообщений


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет.", reply_markup=kb)


@dp.message_handler(commands=['stop'])
async def stop(message: types.Message):
    await message.reply("Пока.", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Я бот справочник.")


@dp.message_handler(commands=['address'])
async def address(message: types.Message):
    await message.reply("Адрес: г. Москва, ул. Льва Толстого, 16")


@dp.message_handler(commands=['phone'])
async def phone(message: types.Message):
    await message.reply("Телефон: +7(495)776-3030")


@dp.message_handler(commands=['site'])
async def site(message: types.Message):
    await message.reply("Сайт: http://www.yandex.ru/company")


@dp.message_handler(commands=['work_time'])
async def work_time(message: types.Message):
    await message.reply("Время работы: круглосуточно.")


if __name__ == '__main__':
    executor.start_polling(dp)
