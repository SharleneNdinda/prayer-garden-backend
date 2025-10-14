import uuid
from typing import Any, Sequence

from django.db import models


# Create your models here.
class AbstractBase(models.Model):
    """Base class for models."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.UUIDField(editable=False, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.UUIDField(blank=True, null=True)

    class Meta:
        """Define a sensible default ordering."""

        abstract = True
        ordering: tuple[str, ...] = ("-updated", "-created")
