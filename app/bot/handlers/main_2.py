import logging
import re

from telebot import TeleBot, types

from django.conf import settings

from bot.models import Payment
from edu_docs.models import Word

logging.basicConfig(level=logging.INFO)

bot = TeleBot(settings.TELEGRAM_TOKEN)

admin_chat_id = int(settings.TG_ADMIN_CHAT_ID)

def create_markup(payment_id):
    """Создает разметку с кнопками для подтверждения и отклонения."""
    markup = types.InlineKeyboardMarkup()
    approve_button = types.InlineKeyboardButton("Подтвердить", callback_data=f'approve:{payment_id}')
    reject_button = types.InlineKeyboardButton("Отказать", callback_data=f'reject:{payment_id}')
    markup.add(approve_button, reject_button)
    return markup


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(admin_chat_id, 'Привет Админ!')


def send_receipt_to_admin(payment):
    """Send receipt to admin with inline keyboard buttons."""
    try:
        caption = (f"Имя клиента: {payment.author.full_name}\n"
                   f"Название заказа: {payment.word.work_theme}\n"
                   f"ID заказа: {payment.id}")
        markup = create_markup(payment.id)
        bot.send_message(admin_chat_id, caption)
        bot.send_message(admin_chat_id, 'Пожалуйста, выберите действие:', reply_markup=markup)
    except Exception as e:
        print(f'Error sending receipt: {e}')

@bot.message_handler(commands=['admin'])
def send_receipt_to_admin_2(message):
    """Send receipt to admin with inline keyboard buttons."""
    try:
        caption = f"Имя клиента: {admin.author.full_name}\nНазвание заказа: {payment.word.work_theme}"
        markup = create_markup(2)
        bot.send_message(admin_chat_id, text='123')
        bot.send_message(admin_chat_id, 'Пожалуйста, выберите действие:', reply_markup=markup)
    except Exception as e:
        print(f'Error sending receipt: {e}')

@bot.message_handler(commands=['approve'])
def approve_handler(message):
    if message.chat.id != admin_chat_id:
        return

    # Получение ID пользователя и подтверждение платежа
    command_parts = message.text.split()
    if len(command_parts) != 2:
        bot.send_message(admin_chat_id, 'Используйте команду в формате: /approve <id>')
        return

    payment_id = int(command_parts[1])
    try:
        payment = Payment.objects.get(id=payment_id)
        payment.status = Payment.StatusChoices.APPROVED
        payment.save()

        bot.send_message(admin_chat_id, f'Платеж пользователя {payment.author.full_name} подтвержден.')
    except Payment.DoesNotExist:
        bot.send_message(admin_chat_id, 'Платеж не найден или уже подтвержден.')


# def send_receipt_to_admin(payment):
#     logging.info(f'Attempting to send receipt for payment id: {payment.id}')
#     try:
#         photo_path = payment.photo.path
#         logging.info(f'Photo path: {photo_path}')
#
#         photo = open(photo_path, 'rb')
#
#         caption = f"Имя клиента: {payment.author.full_name}\nНазвание заказа: {payment.word.work_theme}"
#         logging.info(f'Caption: {caption}')
#
#         markup = create_markup(payment.id)
#
#         bot.send_photo(admin_chat_id, photo, caption=caption, reply_markup=markup)
#         logging.info(f'Receipt sent to admin with buttons for payment id: {payment.id}')
#
#         photo.close()
#     except Exception as e:
#         logging.error(f'Error sending receipt: {e}')


@bot.callback_query_handler(func=lambda call: True)
def handle_all_callbacks(call):
    logging.info(f'Callback received: {call.data}')
    bot.send_message(call.message.chat.id, f'Callback received: {call.data}')

# Handler for approving payment
@bot.callback_query_handler(func=lambda call: call.data.startswith('approve:'))
def approve_payment(call):
    logging.info(f'Approve callback received: {call.data}')
    payment_id = int(call.data.split(':')[1])
    try:
        payment = Payment.objects.get(id=payment_id)
        payment.status = Payment.StatusChoices.APPROVED
        payment.save()
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        bot.edit_message_text(f'Чек от {payment.author.full_name} для заказа {payment.word.work_theme}\n\nПлатеж подтвержден.', call.message.chat.id, call.message.message_id)
    except Payment.DoesNotExist:
        bot.send_message(call.message.chat.id, 'Платеж не найден.')

# Handler for rejecting payment
@bot.callback_query_handler(func=lambda call: call.data.startswith('reject:'))
def reject_payment(call):
    logging.info(f'Reject callback received: {call.data}')
    payment_id = int(call.data.split(':')[1])
    try:
        payment = Payment.objects.get(id=payment_id)
        payment.status = Payment.StatusChoices.REJECTED
        payment.save()
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        bot.edit_message_text(f'Чек от {payment.author.full_name} для заказа {payment.word.work_theme}\n\nПлатеж отклонен.', call.message.chat.id, call.message.message_id)
    except Payment.DoesNotExist:
        bot.send_message(call.message.chat.id, 'Платеж не найден.')


# Logging updates
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    logging.info(f'Received message: {message.text}')

def run_polling():
    print('start')
    bot.polling(none_stop=True)


if __name__ == '__main__':
    run_polling()
