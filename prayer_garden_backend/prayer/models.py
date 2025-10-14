from django.db import models

from prayer_garden_backend.common.models import AbstractBase


class PrayerClassification(models.TextChoices):
    """Attributes that define the classification of a prayer."""

    GRATITUDE = "GRATITUDE", "Prayer of gratitude"
    HEALING = "HEALING", "Prayer of healing"
    PROTECTION = "PROTECTION", "Prayer for protection"
    CUSTOM = "CUSTOM", "Custom user-generated prayer"


class Prayer(AbstractBase):
    """Class to hold prayer items."""

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    classification = models.CharField(
        max_length=64,
        choices=PrayerClassification.choices,
    )
