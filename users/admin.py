from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "is_host")
    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "avatar",
                    "username",
                    "password",
                    "name",
                    "email",
                    "language",
                    "currency",
                    "is_host",
                ),
                "classes": ("wide"),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            ("Important dates"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                ),
                "classes": ("collapse",),
            },
        ),
    )
