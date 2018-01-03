from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import Device
# from .permissions import IsUserOrReadOnly
from .serializers import DeviceSerializer


class DeviceViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Creates, Updates, and retrives User accounts
    """
    serializer_class = DeviceSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        user = self.request.user
        if(user.is_superuser):
            queryset = Device.objects.all()
        else:
            queryset = Device.objects.filter(owner=user)

        return queryset
