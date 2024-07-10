from django.db import models

from account.models import User
from edu_docs.models import Word

prices = {
    "1": {
        "1": 250,
        "2": 450,
        "3": 700,
        "4": 1000,
    },
    "2": {
        "1": 250,
        "2": 1000,
        "3": 700,
        "4": 1000,
    },
    "3": {
        "1": 400,
        "2": 700,
        "3": 1000,
        "4": 1300,
    },
    "4": {
        "1": 300,
        "2": 500,
        "3": 750,
        "4": 1100,
    },
}


class Payment(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'pending', 'Pending'
        APPROVED = 'approved', 'Approved'
        REJECTED = 'rejected', 'Rejected'
        READY = 'ready', 'Ready'

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.OneToOneField(Word, on_delete=models.CASCADE)

    photo = models.ImageField(upload_to='payment_photos/%Y/%m/%d')
    price = models.PositiveIntegerField(blank=True)
    status = models.CharField(
        max_length = 20,
        choices = StatusChoices.choices,
        default = StatusChoices.PENDING,
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Only calculate price if creating a new instance
            self.price = prices[self.word.work_type][self.word.page_count]
        super().save(*args, **kwargs)
