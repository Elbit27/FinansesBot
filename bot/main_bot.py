
from telebot.async_telebot import AsyncTeleBot

from Config import settings

bot = AsyncTeleBot(settings.TOKEN_BOT, parse_mode='HTML')


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_wellcome(message):
    await bot.reply_to(message, '''\
Hi there, I am FinansesBot.
I am here to do something'''
                       )


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)
