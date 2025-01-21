from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Automatically set when the object is created
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
