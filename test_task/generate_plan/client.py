import httpx
from django.conf import settings
from django.contrib.sites import requests
from openai import OpenAI

proxy = '152.26.229.86:9443'

OPENAI_API_KEY = settings.OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY,
                http_client=httpx.Client(proxy=proxy))
