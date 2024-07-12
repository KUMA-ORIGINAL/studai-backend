import logging
import time

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

# List of admin chat IDs
admin_chat_ids = [int(chat_id) for chat_id in settings.TG_ADMIN_CHAT_IDS.split(",")]


@bot.message_handler(commands=['start'])
def start_handler(message):
    for admin_chat_id in admin_chat_ids:
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

            for admin_chat_id in admin_chat_ids:
                bot.send_photo(admin_chat_id, photo, caption=caption)
                logger.info(f'Receipt sent to admin with buttons for payment id: {payment.id}')
    except FileNotFoundError:
        logger.error(f'Photo file not found at path: {photo_path}')
    except Exception as e:
        logger.error(f'Error sending receipt: {e}')


@bot.message_handler(commands=['approve'])
def approve_handler(message):
    if message.chat.id not in admin_chat_ids:
        return

    command_parts = message.text.split()
    if len(command_parts) != 2:
        for admin_chat_id in admin_chat_ids:
            bot.send_message(admin_chat_id, 'Используйте команду в формате: /approve <id>')
        return

    try:
        payment_id = int(command_parts[1])
    except ValueError:
        for admin_chat_id in admin_chat_ids:
            bot.send_message(admin_chat_id, 'ID должен быть числом.')
        return

    try:
        payment = Payment.objects.get(id=payment_id)
    except Payment.DoesNotExist:
        for admin_chat_id in admin_chat_ids:
            bot.send_message(admin_chat_id, 'Платеж не найден.')
        return

    if payment.status == Payment.StatusChoices.APPROVED:
        for admin_chat_id in admin_chat_ids:
            bot.send_message(admin_chat_id, 'Платеж уже подтвержден.')
        return
    elif payment.status == Payment.StatusChoices.REJECTED:
        for admin_chat_id in admin_chat_ids:
            bot.send_message(admin_chat_id, 'Платеж уже отклонен.')
        return

    payment.status = Payment.StatusChoices.APPROVED
    payment.save()

    for admin_chat_id in admin_chat_ids:
        bot.send_message(admin_chat_id,
                         f'Платеж пользователя {payment.author.full_name} подтвержден.\n'
                         f'Началось создание работы ...')

    word = payment.word

    logger.info('generate_texts generate_texts')
    subtopic_texts, context = generate_texts(
        client=client,
        language_of_work=word.language_of_work,
        subtopics=word.subtopics,
        context=word.context,
        page_count=word.page_count
    )
    logger.info('texts_editor texts_editor')
    edited_subtopic_texts = texts_editor(
        subtopic_texts,
        word.subtopics
    )
    logger.info('create_word create_word')
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
        word.file.save(sanitized_theme, ContentFile(file_content))
        word.status = word.StatusChoices.APPROVED
        word.save()

    for admin_chat_id in admin_chat_ids:
        bot.send_message(admin_chat_id, f'Работа пользователя {payment.author.full_name} создан')


@bot.message_handler(commands=['reject'])
def reject_handler(message):
    if message.chat.id not in admin_chat_ids:
        return

    command_parts = message.text.split()
    if len(command_parts) != 2:
        for admin_chat_id in admin_chat_ids:
            bot.send_message(admin_chat_id, 'Используйте команду в формате: /reject <id>')
        return

    try:
        payment_id = int(command_parts[1])
    except ValueError:
        for admin_chat_id in admin_chat_ids:
            bot.send_message(admin_chat_id, 'ID должен быть числом.')
        return

    try:
        payment = Payment.objects.get(id=payment_id)
    except Payment.DoesNotExist:
        for admin_chat_id in admin_chat_ids:
            bot.send_message(admin_chat_id, 'Платеж не найден.')
        return

    if payment.status == Payment.StatusChoices.REJECTED:
        for admin_chat_id in admin_chat_ids:
            bot.send_message(admin_chat_id, 'Платеж уже отклонен.')
        return
    elif payment.status == Payment.StatusChoices.APPROVED:
        for admin_chat_id in admin_chat_ids:
            bot.send_message(admin_chat_id, 'Платеж уже подтвержден.')
        return

    word = payment.word
    payment.status = Payment.StatusChoices.REJECTED
    word.status = Word.StatusChoices.REJECTED
    payment.save()
    word.save()

    for admin_chat_id in admin_chat_ids:
        bot.send_message(admin_chat_id, f'Платеж пользователя {payment.author.full_name} отклонен.')


def run_polling():
    logger.info('start bot')
    while True:
        try:
            bot.polling(non_stop=True, interval=0)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue


if __name__ == '__main__':
    run_polling()