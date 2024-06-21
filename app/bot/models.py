from django.db import models

from account.models import User


class Payment(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'pending', 'Pending'
        APPROVED = 'approved', 'Approved'
        REJECTED = 'rejected', 'Rejected'

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tg_user_id = models.BigIntegerField()
    tg_username = models.CharField(max_length=255, blank=True, null=True)
    receipt_image_id = models.TextField()
    status = models.CharField(
        max_length = 50,
        choices = StatusChoices.choices,
        default = StatusChoices.PENDING,
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
