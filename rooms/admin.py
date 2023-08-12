from django.contrib import admin
from . import models


@admin.action(description="금액을 0으로 변경")
def set_zero(model_admin, request, rooms):
    for room in rooms:
        room.price = 0
        room.save()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    actions = [set_zero]
    list_display = (
        "id",
        "name",
        "price",
        "country",
        "city",
        "host",
        "total_amenities",
        "rating",
        "created",
        "updated",
    )


@admin.register(models.Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "created", "updated")
    readonly_fields = ("created", "updated")
