import logging
import re

from telebot import TeleBot

from account.models import User
from app import settings
from bot.models import Payment
from edu_docs.models import Word

logging.basicConfig(level=logging.INFO)

token = settings.TELEGRAM_TOKEN
bot = TeleBot(token)

admin_chat_id = int(settings.TG_ADMIN_CHAT_ID)

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")



@bot.message_handler(commands=['start'])
def start_handler(message):
    if message.chat.id != admin_chat_id:
        bot.send_message(message.chat.id, 'Привет! Пожалуйста, отправьте почту, на которой вы регистрировались на платформе.')
    else:
        bot.send_message(admin_chat_id, 'Привет Админ!')


# Обработчик команды админа для подтверждения платежа
@bot.message_handler(commands=['approve'])
def approve_handler(message):
    if message.chat.id != admin_chat_id:
        return

    # Получение ID пользователя и подтверждение платежа
    command_parts = message.text.split()
    if len(command_parts) != 2:
        bot.send_message(admin_chat_id, 'Используйте команду в формате: /approve <email>')
        return

    email = command_parts[1]
    try:
        payment = Payment.objects.get(author__email=email, status=Payment.StatusChoices.PENDING)
        payment.status = Payment.StatusChoices.APPROVED
        payment.save()

        bot.send_message(payment.tg_user_id, 'Ваш платеж подтвержден!')
        bot.send_message(admin_chat_id, f'Платеж пользователя {payment.author.full_name} подтвержден.')
    except Payment.DoesNotExist:
        bot.send_message(admin_chat_id, 'Платеж не найден или уже подтвержден.')



@bot.message_handler(content_types=['text'])
def email_handler(message):
    email = message.text
    if EMAIL_REGEX.match(email):
        try:
            user = User.objects.get(email=email)
            bot.send_message(message.chat.id, f'Спасибо, {user.full_name}! Теперь отправьте скриншот '
                                              f'чека.')
            bot.register_next_step_handler(message, photo_handler, user)
        except User.DoesNotExist:
            bot.send_message(message.chat.id, 'Пользователь с такой почтой не найден. Пожалуйста, проверьте и попробуйте снова.')
    else:
        bot.send_message(message.chat.id,'Пожалуйста, отправьте действительный адрес электронной почты.')

# Обработчик для получения фото
def photo_handler(message, user):
    if message.content_type == 'photo':
        file_id = message.photo[-1].file_id
        payment = Payment.objects.create(author=user,
                                         tg_user_id=message.chat.id,
                                         tg_username=message.chat.username,
                                         receipt_image_id=file_id)

        # Уведомляем админа
        bot.send_message(admin_chat_id,
                         f'Новый чек от {user.full_name} ({user.email}). Пожалуйста, проверьте.')
        bot.send_photo(admin_chat_id, file_id, caption=f'Чек от {user.full_name}')
        bot.send_message(message.chat.id, 'Чек отправлен на проверку. Ожидайте подтверждения.')
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, отправьте скриншот чека.')
