from rest_framework import serializers

from .models import Device


class DeviceSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super(DeviceSerializer, self).create(validated_data)

    class Meta:
        model = Device
        fields = ('id', 'owner', 'name', 'location', 'connected', 'current_module')
        read_only_fields = ('owner', )
