from django.conf import settings
from openai import OpenAI

OPENAI_API_KEY = settings.OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)
