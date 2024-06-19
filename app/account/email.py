from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from djoser import email, utils


class ActivationEmail(email.ActivationEmail):
    template_name = 'account/activation.html'


class ConfirmationEmail(email.ConfirmationEmail):
    template_name = 'account/confirmation.html'
