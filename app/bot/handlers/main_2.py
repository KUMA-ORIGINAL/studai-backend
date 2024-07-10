import logging
import time

from django.core.files import File
from django.core.files.base import ContentFile
from telebot import TeleBot

from django.conf import settings

from bot.models import Payment
from edu_docs.models import Word
from edu_docs.services.client import client
from edu_docs.services.create_word_2 import create_word
from edu_docs.services.generate_texts_2 import generate_texts
from edu_docs.services.texts_editor import texts_editor

logger = logging.getLogger(__name__)

telebot_logger = logging.getLogger('telebot')
telebot_logger.setLevel(logging.DEBUG)

bot = TeleBot(settings.TELEGRAM_TOKEN)

admin_chat_id = int(settings.TG_ADMIN_CHAT_ID)


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(admin_chat_id, 'Привет Админ!')


def send_receipt_to_admin(payment):
    logging.info(f'Attempting to send receipt for payment id: {payment.id}')
    try:
        photo_path = payment.photo.path
        logger.info(f'Photo path: {photo_path}')

        with open(photo_path, 'rb') as photo:
            caption = (f"Имя клиента: {payment.author.full_name}\n"
                       f"Название заказа: {payment.word.work_theme}\n"
                       f"Тип работы: {payment.word.work_type_display}\n"
                       f"Количество страниц: {payment.word.page_count_display}\n"
                       f"Цена: {payment.price}\n"
                       f"Номер заказа: {payment.id}")
            logger.info(f'Caption: {caption}')

            bot.send_photo(admin_chat_id, photo, caption=caption)
            logger.info(f'Receipt sent to admin with buttons for payment id: {payment.id}')
    except FileNotFoundError:
        logger.error(f'Photo file not found at path: {photo_path}')
    except Exception as e:
        logger.error(f'Error sending receipt: {e}')

@bot.message_handler(commands=['approve'])
def approve_handler(message):
    if message.chat.id != admin_chat_id:
        return

    # Получение ID пользователя и подтверждение платежа
    command_parts = message.text.split()
    if len(command_parts) != 2:
        bot.send_message(admin_chat_id, 'Используйте команду в формате: /approve <id>')
        return

    try:
        payment_id = int(command_parts[1])
    except ValueError:
        bot.send_message(admin_chat_id, 'ID должен быть числом.')
        return

    try:
        payment = Payment.objects.get(id=payment_id)
    except Payment.DoesNotExist:
        bot.send_message(admin_chat_id, 'Платеж не найден.')
        return

    if payment.status == Payment.StatusChoices.APPROVED:
        bot.send_message(admin_chat_id, 'Платеж уже подтвержден.')
        return
    elif payment.status == Payment.StatusChoices.REJECTED:
        bot.send_message(admin_chat_id, 'Платеж уже отклонен.')
        return

    payment.status = Payment.StatusChoices.APPROVED
    payment.save()

    bot.send_message(admin_chat_id,
                     f'Платеж пользователя {payment.author.full_name} подтвержден.\n'
                     f'Началось создание работы ...')


    word = payment.word

    subtopic_texts, context = generate_texts(
        client=client,
        language_of_work=word.language_of_work,
        subtopics=word.subtopics,
        context=word.context,
        page_count=word.page_count
    )
    edited_subtopic_texts = texts_editor(
        subtopic_texts,
        word.subtopics
    )
    full_path, sanitized_theme = create_word(
        work_theme=word.work_theme,
        subtopics=word.subtopics,
        texts=edited_subtopic_texts,
        university=word.university,
        work_type=word.work_type_display,
        author_name=word.author_name,
        group_name=word.group_name,
        teacher_name=word.teacher_name,
        language_of_work=word.language_of_work,
        cover_page_data=word.cover_page_data
    )

    with open(full_path, 'rb') as f:
        file_content = f.read()

        # Сохраняем содержимое файла в поле FileField модели
        word.file.save(sanitized_theme, ContentFile(file_content))
        word.status = word.StatusChoices.APPROVED
        word.save()

    bot.send_message(admin_chat_id, f'Работа пользователя {payment.author.full_name} создан')

# Обработчик команды /reject
@bot.message_handler(commands=['reject'])
def reject_handler(message):
    if message.chat.id != admin_chat_id:
        return

    # Получение ID пользователя и отклонение платежа
    command_parts = message.text.split()
    if len(command_parts) != 2:
        bot.send_message(admin_chat_id, 'Используйте команду в формате: /reject <id>')
        return

    try:
        payment_id = int(command_parts[1])
    except ValueError:
        bot.send_message(admin_chat_id, 'ID должен быть числом.')
        return

    try:
        payment = Payment.objects.get(id=payment_id)
    except Payment.DoesNotExist:
        bot.send_message(admin_chat_id, 'Платеж не найден.')
        return

    if payment.status == Payment.StatusChoices.REJECTED:
        bot.send_message(admin_chat_id, 'Платеж уже отклонен.')
        return
    elif payment.status == Payment.StatusChoices.APPROVED:
        bot.send_message(admin_chat_id, 'Платеж уже подтвержден.')
        return

    word = payment.word
    payment.status = Payment.StatusChoices.REJECTED
    word.status = Word.StatusChoices.REJECTED
    payment.save()
    word.save()

    bot.send_message(admin_chat_id, f'Платеж пользователя {payment.author.full_name} отклонен.')


# # Handler for approving payment
# @bot.callback_query_handler(func=lambda call: call.data.startswith('approve:'))
# def approve_payment(call):
#     logging.info(f'Approve callback received: {call.data}')
#     payment_id = int(call.data.split(':')[1])
#     try:
#         payment = Payment.objects.get(id=payment_id)
#         payment.status = Payment.StatusChoices.APPROVED
#         payment.save()
#         bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
#         bot.edit_message_text(f'Чек от {payment.author.full_name} для заказа {payment.word.work_theme}\n\nПлатеж подтвержден.', call.message.chat.id, call.message.message_id)
#     except Payment.DoesNotExist:
#         bot.send_message(call.message.chat.id, 'Платеж не найден.')
#
# # Handler for rejecting payment
# @bot.callback_query_handler(func=lambda call: call.data.startswith('reject:'))
# def reject_payment(call):
#     logging.info(f'Reject callback received: {call.data}')
#     payment_id = int(call.data.split(':')[1])
#     try:
#         payment = Payment.objects.get(id=payment_id)
#         payment.status = Payment.StatusChoices.REJECTED
#         payment.save()
#         bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
#         bot.edit_message_text(f'Чек от {payment.author.full_name} для заказа {payment.word.work_theme}\n\nПлатеж отклонен.', call.message.chat.id, call.message.message_id)
#     except Payment.DoesNotExist:
#         bot.send_message(call.message.chat.id, 'Платеж не найден.')


# Logging updates
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     logger.info(f'Received message: {message.text}')


def run_polling():
    logger.info(f'start bot')
    while True:
        try:
            bot.polling(non_stop=True, interval=0)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue


if __name__ == '__main__':
    run_polling()
