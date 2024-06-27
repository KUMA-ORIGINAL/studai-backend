import logging

import telebot
from django.core.management.base import BaseCommand

from bot.views_bot import bot

logging.basicConfig(level=logging.INFO)

class Command(BaseCommand):
    """Команда для запуска бота в режиме long polling."""

    help = 'command for start bot long polling mode'

    def handle(self, *args, **options):
        """Entrypoint."""
        try:
            logging.info('Start long polling...')
            bot.polling(none_stop=True)
        except Exception as e:
            logging.error(f'Ошибка при запуске бота: {e}')

