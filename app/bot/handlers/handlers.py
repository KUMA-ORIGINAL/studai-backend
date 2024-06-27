import logging

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from app.settings import TELEGRAM_TOKEN, TG_ADMIN_CHAT_ID


TG_ADMIN_CHAT_ID = int(TG_ADMIN_CHAT_ID)


def create_markup(payment_id):
    """Создает разметку с кнопками для подтверждения и отклонения."""
    keyboard = [
        [
            InlineKeyboardButton("Подтвердить", callback_data=f'approve:{payment_id}'),
            InlineKeyboardButton("Отказать", callback_data=f'reject:{payment_id}')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def start_handler(update, context):
    context.bot.send_message(chat_id=TG_ADMIN_CHAT_ID, text='Привет Админ!')

def send_receipt_to_admin_2(update, context):
    """Send receipt to admin with inline keyboard buttons."""
    try:
        # caption = f"Имя клиента: {payment.author.full_name}\nНазвание заказа: {payment.word.work_theme}"
        markup = create_markup(2)
        context.bot.send_message(chat_id=TG_ADMIN_CHAT_ID, text='sssssss', reply_markup=markup)
    except Exception as e:
        logging.error(f'Error sending receipt: {e}')

def send_receipt_to_admin(bot, payment):
    """Send receipt to admin with inline keyboard buttons."""
    try:
        caption = f"Имя клиента: {payment.author.full_name}\nНазвание заказа: {payment.word.work_theme}"
        markup = create_markup(payment.id)
        bot.send_message(chat_id=TG_ADMIN_CHAT_ID, text=caption, reply_markup=markup)
    except Exception as e:
        logging.error(f'Error sending receipt: {e}')


def handle_all_callbacks(update, context):
    query = update.callback_query
    context.bot.send_message(chat_id=TG_ADMIN_CHAT_ID, text=f'Callback received: {query.data}')

def approve_payment(update, context):
    query = update.callback_query
    # payment_id = int(query.data.split(':')[1])
    try:
        # Здесь должна быть логика обновления статуса платежа в вашей модели Payment
        context.bot.edit_message_text(text=f'Платеж подтвержден.', chat_id=TG_ADMIN_CHAT_ID, message_id=query.message.message_id)
    except Exception as e:
        logging.error(f'Error approving payment: {e}')

def reject_payment(update, context):
    query = update.callback_query
    # payment_id = int(query.data.split(':')[1])
    try:
        # Здесь должна быть логика обновления статуса платежа в вашей модели Payment
        context.bot.edit_message_text(text=f'Платеж отклонен.', chat_id=TG_ADMIN_CHAT_ID, message_id=query.message.message_id)
    except Exception as e:
        logging.error(f'Error rejecting payment: {e}')
