from django.db import models

from prayer_garden_backend.common.models import AbstractBase
from prayer_garden_backend.prayer.models import Prayer
from prayer_garden_backend.timer.models import Timer


class Plant(AbstractBase):
    """Class to hold prayer plants."""

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)


class PrayerPlanting(AbstractBase):
    """Class to hold prayer plantings."""

    plant = models.ForeignKey(Plant, on_delete=models.PROTECT, related_name="plantings")
    prayer = models.ForeignKey(
        Prayer, on_delete=models.PROTECT, related_name="plantings"
    )
    timer = models.ForeignKey(Timer, on_delete=models.PROTECT, related_name="plantings")
