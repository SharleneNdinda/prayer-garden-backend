from django.db import models
from prayer_garden_backend.common.models import AbstractBase


class TimerType(models.TextChoices):
    """Attributes that define the types of a timers."""

    WORK = "WORK", "Work timer"
    BREAK = "BREAK", "Break timer"


class Timer(AbstractBase):
    """Class to hold timer sessions."""

    duration = models.IntegerField()
    start_time = models.DateField(auto_now=True)
    end_time = models.DateField(blank=True, null=True)
    timer_type = models.CharField(max_length=64, choices=TimerType.choices)
    completed = models.BooleanField(default=False)
