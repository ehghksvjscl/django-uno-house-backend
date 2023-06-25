from django.db import models
from common.models import CommonModel


class Experience(CommonModel):
    """체험"""

    name = models.CharField(max_length=140)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    host = models.ForeignKey("users.User", null=True, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()
    description = models.TextField()
    perks = models.ManyToManyField(
        "experiences.Perk",
        related_name="experiences",
    )
    category = models.ForeignKey(
        "categories.Category",
        related_name="experiences",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name


class Perk(CommonModel):

    name = models.CharField(max_length=140)
    details = models.CharField(max_length=140)
    explanation = models.TextField()

    def __str__(self) -> str:
        return self.name
