from django.contrib import admin
from . import models


@admin.register(models.Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country", "city", "host", "start", "end")


@admin.register(models.Perk)
class PerkAdmin(admin.ModelAdmin):
    list_display = ("id", "details", "explanation", "created")
    readonly_fields = ("created", "updated")
