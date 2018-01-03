from django.db import models, IntegrityError
from django.utils import timezone

from .utils import generateKey
from users.models import User
from devices.models import Device

import uuid
from datetime import timedelta


class RegistrationKeyManager(models.Manager):
    def create_registration_key(self):
        while(True):
            try:
                key = generateKey()
                exp_time = timezone.now() + timedelta(seconds=30)
                registration_key = self.create(key=key, expires=exp_time)
                break
            except IntegrityError:
                pass
        return registration_key

class RegistrationKey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    key = models.CharField(unique=True, max_length=6)
    used = models.BooleanField(default=False)
    owner = models.ForeignKey(User, null=True, blank=True)
    device = models.ForeignKey(Device, null=True, blank=True)
    expires = models.DateTimeField()

    objects = RegistrationKeyManager()

    @property
    def status(self):
        if self.used:
            return "USED"
        elif self.owner is not None:
            return "ASSIGNED"
        elif self.expired:
            return "EXPIRED"
        return "UNASSIGNED"

    @property
    def expired(self):
        return timezone.now() > self.expires

    def regen_key(self):
        self.key = generateKey()
        self.expires = timezone.now() + timedelta(seconds=30)
        self.save()

    @property
    def time_to_expiration(self):
        return max(0, (self.expires-timezone.now()).total_seconds())

    @property
    def token(self):
        if self.owner is not None:
            return self.owner.auth_token.key
        else:
            return None
