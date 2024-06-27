import logging

import telegram

from telegram.ext import (
    Updater, Dispatcher, CommandHandler, CallbackQueryHandler
)

# from celery.decorators import task  # event processing in async mode

from app.settings import TELEGRAM_TOKEN

from bot.handlers import handlers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def setup_dispatcher(dp):
    """
    Adding handlers for events from Telegram
    """

    start_handler = CommandHandler('start', handlers.start_handler)
    dp.add_handler(start_handler)
    admin_handler = CommandHandler('admin', handlers.send_receipt_to_admin_2)
    dp.add_handler(admin_handler)

    dp.add_handler(CallbackQueryHandler(handlers.handle_all_callbacks))
    dp.add_handler(CallbackQueryHandler(handlers.approve_payment, pattern=r'^approve:'))
    dp.add_handler(CallbackQueryHandler(handlers.reject_payment, pattern=r'^reject:'))

    return dp


def run_polling():
    """ Run bot in pooling mode """
    updater = Updater(TELEGRAM_TOKEN, use_context=True, workers=1)

    dp = updater.dispatcher
    dp = setup_dispatcher(dp)

    bot_info = telegram.Bot(TELEGRAM_TOKEN).get_me()
    bot_link = f"https://t.me/" + bot_info["username"]

    print(f"Polling of '{bot_link}' started")
    logger.info("Starting bot polling...")
    updater.start_polling(timeout=123)
    updater.idle()


# @task(ignore_result=True)
def process_telegram_event(update_json):
    update = telegram.Update.de_json(update_json, bot)
    dispatcher.process_update(update)


# Global variable - best way I found to init Telegram bot
bot = telegram.Bot(TELEGRAM_TOKEN)
dispatcher = setup_dispatcher(Dispatcher(bot=bot, update_queue=None))
TELEGRAM_BOT_USERNAME = bot.get_me()["username"]