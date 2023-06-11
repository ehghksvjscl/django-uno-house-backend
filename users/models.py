from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        male = ("male", "Male")
        female = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        kr = ("kr", "Korean")
        en = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        krw = ("krw", "KRW")
        usd = ("usd", "USD")

    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150)
    avatar = models.ImageField(blank=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices)
    currency = models.CharField(max_length=3, choices=CurrencyChoices.choices)
    is_host = models.BooleanField(default=False)
