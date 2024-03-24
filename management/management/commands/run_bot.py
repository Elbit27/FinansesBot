from django.core.management.base import BaseCommand
import asyncio

from bot.main_bot import bot

from bot.main_bot import dp


class Command(BaseCommand):
    help = 'Запускаем бота!'

    def handle(self, *args, **options):
        asyncio.run(dp.start_polling(bot))
