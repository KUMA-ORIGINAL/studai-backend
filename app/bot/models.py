from django.db import models

from account.models import User
from edu_docs.models import Word


class Payment(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'pending', 'Pending'
        APPROVED = 'approved', 'Approved'
        REJECTED = 'rejected', 'Rejected'
        READY = 'ready', 'Ready'

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.OneToOneField(Word, on_delete=models.CASCADE)

    photo = models.ImageField(upload_to='payment_photos/%Y/%m/%d')
    status = models.CharField(
        max_length = 20,
        choices = StatusChoices.choices,
        default = StatusChoices.PENDING,
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
