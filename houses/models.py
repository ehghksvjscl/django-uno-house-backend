from django.db import models


class House(models.Model):
    owner = models.ForeignKey("users.User", null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=140)
    price = models.PositiveBigIntegerField(help_text="KRW")
    description = models.TextField()
    address = models.CharField(max_length=140)
    is_pet_allowed = models.BooleanField(default=False)
