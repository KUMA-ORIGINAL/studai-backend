import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

# from bot.handlers.main import run_polling
from bot.handlers.main_2 import run_polling


if __name__ == "__main__":
    run_polling()
