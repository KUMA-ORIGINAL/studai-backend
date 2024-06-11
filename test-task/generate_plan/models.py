from django.db import models


class Plan(models.Model):
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

    language_of_talk = models.CharField(max_length=255, choices=LANGUAGES)
    work_type = models.CharField(max_length=255, choices=WORK_TYPES_RU)
    language_of_work = models.CharField(max_length=255, choices=LANGUAGES)
    work_theme = models.CharField(max_length=255)
    discipline = models.CharField(max_length=255)
    page_count = models.CharField(max_length=255, choices=PAGE_COUNTS)
    wishes = models.CharField(max_length=255)

    cover_page_data = models.CharField(max_length=255)
    university = models.CharField(max_length=255, blank=True)
    author_name = models.CharField(max_length=255, blank=True)
    group_name = models.CharField(max_length=255, blank=True)
    teacher_name = models.CharField(max_length=255, blank=True)

    chatbot_response = models.TextField()
