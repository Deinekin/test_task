from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админ-панель работника"""

    list_display = (
        "id",
        "name",
        "email",
        "company",
    )
