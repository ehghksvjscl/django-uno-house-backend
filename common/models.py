from django.db import models


class CommonModel(models.Model):
    """공통 모델"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
