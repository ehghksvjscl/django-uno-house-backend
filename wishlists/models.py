from django.db import models
from common.models import CommonModel


class Wishlist(CommonModel):
    """위시리스트"""

    name = models.CharField(max_length=140)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)
    experiences = models.ManyToManyField("experiences.Experience", blank=True)

    def __str__(self) -> str:
        return self.name
