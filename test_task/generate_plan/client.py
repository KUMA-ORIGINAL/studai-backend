import httpx
from django.conf import settings
from openai import OpenAI

proxy = 'http://85.111.60.196:8080'

OPENAI_API_KEY = settings.OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY,
                http_client=httpx.Client(proxy=proxy))
