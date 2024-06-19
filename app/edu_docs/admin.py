from django.contrib import admin

from edu_docs.models import Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ("id", 'work_theme', "work_type", "author")
    list_display_links = ('id', 'work_theme')

