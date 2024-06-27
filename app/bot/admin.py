from django.contrib import admin

from bot.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "status", 'created', 'updated')
    list_display_links = ('id', 'author')
