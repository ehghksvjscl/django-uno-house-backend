from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ("__str__", "room", "experience")
    list_filter = ("rating",)
