from django.db import models
from common.models import CommonModel


class Category(CommonModel):
    """카테고리"""

    class CategoryKind(models.TextChoices):
        rooms = "Rooms", "rooms"
        experiences = "Experiences", "experiences"

    name = models.CharField(max_length=140)
    kind = models.CharField(max_length=140, choices=CategoryKind.choices)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
