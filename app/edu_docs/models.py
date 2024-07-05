from django.db import models

from account.models import User


class Word(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'pending', 'Pending'
        APPROVED = 'approved', 'Approved'
        REJECTED = 'rejected', 'Rejected'
        READY = 'ready', 'Ready'

    WORK_TYPES_RU = [
        ("1", "Реферат"),
        ("2", "Самостоятельная работа студента"),
        ("3", "Курсовая работа"),
        ("4", "Доклад")
    ]

    # Количества страниц
    PAGE_COUNTS = [
        ("1", "1-10"),
        ("2", "10-20"),
        ("3", "20-30"),
        ("4", "30-40")
    ]

    LANGUAGES = [
        ("1", "Кыргызча"),
        ("2", "Русский"),
        ("3", "English"),
    ]

    COVER_PAGE = [
        ("1", "Да"),
        ("2", "Нет"),
        ("3", "Пустой титульный лист"),
    ]

    work_type = models.CharField(max_length=255, choices=WORK_TYPES_RU)
    language_of_work = models.CharField(max_length=255, choices=LANGUAGES)
    work_theme = models.CharField(max_length=255)
    discipline = models.CharField(max_length=255, blank=True)
    page_count = models.CharField(max_length=255, choices=PAGE_COUNTS)
    wishes = models.CharField(max_length=255)

    cover_page_data = models.CharField(max_length=255, choices=COVER_PAGE)
    university = models.CharField(max_length=255, blank=True, null=True)
    author_name = models.CharField(max_length=255, blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    teacher_name = models.CharField(max_length=255, blank=True, null=True)

    subtopics = models.JSONField()
    context = models.JSONField()

    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING)

    file = models.FileField(upload_to='documents/')

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.work_theme

    @property
    def work_type_display(self):
        return dict(self.WORK_TYPES_RU).get(self.work_type, self.work_type)

    @property
    def language_of_work_display(self):
        return dict(self.LANGUAGES).get(self.language_of_work, self.language_of_work)

    @property
    def page_count_display(self):
        return dict(self.PAGE_COUNTS).get(self.page_count, self.page_count)

    @property
    def cover_page_data_display(self):
        return dict(self.COVER_PAGE).get(self.cover_page_data, self.cover_page_data)