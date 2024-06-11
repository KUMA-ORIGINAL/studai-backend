from django.contrib import admin


class PlanAdmin(admin.ModelAdmin):
    list_display = ("id", "work_type", "work_theme")
