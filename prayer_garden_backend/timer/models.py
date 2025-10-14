from django.db import models

from prayer_garden_backend.common.models import AbstractBase


class Timer(AbstractBase):
    """Class to hold timer sessions."""

    duration = models.IntegerField()
    start_time = models.DateField(auto_now=True)
    end_time = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
