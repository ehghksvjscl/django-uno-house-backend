from django.contrib import admin
from . import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country", "city", "host", "created", "updated")


@admin.register(models.Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "created", "updated")
    readonly_fields = ("created", "updated")
