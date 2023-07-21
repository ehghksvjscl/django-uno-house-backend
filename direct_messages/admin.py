from django.contrib import admin
from . import models


@admin.register(models.ChattingRoom)
class ChattingRoomAdmin(admin.ModelAdmin):
    list_display = ("__str__", "created", "updated")


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("user", "message", "created", "updated")
