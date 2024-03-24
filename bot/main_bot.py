# from telebot.async_telebot import AsyncTeleBot, types
from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode

from Config import settings
from category.models import Category

# bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='HTML')
bot = Bot(token=settings.TOKEN_BOT)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.reply('''
Hi there, I am FinansesBot.
I am here to do something'''
                        )


# Handle '/start' and '/help'
# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     await message.reply("Привет! Я бот.")

# @bot.message_handler(commands=['help', 'start'])
# async def send_wellcome(message):
#     await bot.reply_to(message, '''\
# Hi there, I am FinansesBot.
# I am here to do something'''
#                        )


# # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# async def echo_message(message):
#     await bot.reply_to(message, message.text)


cats = []
for e in Category.objects.all():
    cats.append(e)


@dp.message()
async def plus_or_minus(message):
    if message.text == '+':
        await message.reply('you are rich now')
    elif message.text == '-':
        kb = []
        for i in range(len(cats)):
            kb.append([types.KeyboardButton(text=f'{cats[i]}')])

        keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
        await message.reply('Какую категорию расходов выберите?', reply_markup=keyboard)
