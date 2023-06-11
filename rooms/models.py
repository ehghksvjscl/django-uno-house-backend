from django.db import models
from common.models import CommonModel


class Room(CommonModel):
    """숙소"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE = "entire", "집 전체"
        PRIVATE = "private", "개인실"
        SHARED = "shared", "다인실"

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


class Amenity(CommonModel):
    """편의시설"""

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, default="")
