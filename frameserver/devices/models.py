from django.db import models

import uuid

from users.models import User


# Create your models here.

class Device(models.Model):
    GALLERY = 'GAL'
    WEATHER = 'WEA'
    CALENDAR = 'CAL'
    VIDEO = 'VID'
    MODULE_CHOICES = (
        (GALLERY, "Gallery"),
        (WEATHER, "Weather"),
        (CALENDAR, "Calendar"),
        (VIDEO, "Video")
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=32, blank=False, null=False)
    location = models.CharField(max_length=32, blank=False, null=False)
    connected = models.BooleanField(default=False)
    current_module = models.CharField(max_length=3, choices=MODULE_CHOICES, default=WEATHER)
