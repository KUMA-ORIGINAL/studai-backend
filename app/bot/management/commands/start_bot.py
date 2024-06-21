import logging

from django.core.management.base import BaseCommand

from bot.views import bot

logging.basicConfig(level=logging.INFO)

class Command(BaseCommand):
    """Команда для запуска бота в режиме long polling."""

    help = 'command for start bot long polling mode'

    def handle(self, *args, **options):
        """Entrypoint."""
        logging.info('Start long polling...')
        try:
            bot.infinity_polling()
        except Exception as e:
            logging.error(f'Ошибка при запуске бота: {e}')

