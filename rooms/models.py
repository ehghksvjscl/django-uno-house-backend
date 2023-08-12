from django.db import models
from common.models import CommonModel


class Room(CommonModel):
    """숙소"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE = "entire", "집 전체"
        PRIVATE = "private", "개인실"
        SHARED = "shared", "다인실"

    name = models.CharField(max_length=140)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=255)
    is_pet_allowed = models.BooleanField(default=False)
    kind = models.CharField(max_length=50, choices=RoomKindChoices.choices)
    host = models.ForeignKey("users.User", null=True, on_delete=models.SET_NULL)
    amenities = models.ManyToManyField("rooms.Amenity", related_name="rooms")
    category = models.ForeignKey(
        "categories.Category",
        related_name="rooms",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def total_amenities(room):
        return room.amenities.count()

    def rating(room):
        reviews = room.reviews.all().values_list("rating", flat=True)
        count = 0
        total = 0
        for review in reviews:
            total += review
            count += 1

        if count == 0:
            return "리뷰 없음"

        return round(total / count, 2)

    def __str__(self) -> str:
        return self.name


class Amenity(CommonModel):
    """편의시설"""

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, default="")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
