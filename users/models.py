from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Модель пользователя"""

    name = models.CharField()
    email = models.EmailField()
    company = models.CharField()

    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
