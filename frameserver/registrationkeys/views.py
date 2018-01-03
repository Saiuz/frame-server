from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import detail_route

from .models import RegistrationKey
from .serializers import RegistrationKeySerializer


class RegistrationKeyViewSet(viewsets.ViewSet):
    queryset = RegistrationKey.objects.filter(used=False)
    permission_classes = (AllowAny,)
    """
    Creates, and retrives Registration Keys
    """
    def list(self, request):
        content = {'status': 'running'}
        return Response(content)

    def retrieve(self, request, pk=None):
        rk = get_object_or_404(self.queryset, pk=pk)
        serializer = RegistrationKeySerializer(rk)
        return Response(serializer.data)

    @detail_route(methods=['post'])
    def regen_key(self, request, pk=None):
        rk = get_object_or_404(self.queryset, pk=pk)
        rk.regen_key()
        serializer = RegistrationKeySerializer(rk)
        return Response(serializer.data)

    def create(self, request):
        rk = RegistrationKey.objects.create_registration_key()
        serializer = RegistrationKeySerializer(rk)
        return Response(serializer.data)

    @detail_route(methods=['post'], permission_classes=[IsAuthenticated])
    def assign_owner(self, request, pk=None):
        rk = get_object_or_404(self.queryset, key=pk.upper())
        if rk.expired:
            return Response({'result': 'unsuccessful', 'reason': 'expired'})
        rk.owner = request.user
        rk.save()
        return Response({'result': 'successful'})
