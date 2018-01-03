from rest_framework import serializers

from .models import RegistrationKey


class RegistrationKeySerializer(serializers.ModelSerializer):

    class Meta:
        model = RegistrationKey
        fields = ('id', 'key', 'device', 'time_to_expiration', 'token')
        read_only_fields = ('id', 'key', 'device', 'time_to_expiration', 'token')
