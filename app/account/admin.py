from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.forms import CustomUserChangeForm, CustomUserCreationForm
from account.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Dates", {"fields": ("last_login", "date_joined")}),
        ('required', {'fields': ('first_name', 'last_name')}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = User

    ordering = ['-date_joined']

    list_display = ('id', 'email', 'first_name', 'last_name')
    list_display_links = ('id', 'email')
