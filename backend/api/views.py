from rest_framework import viewsets

from .models import Device, DevicePermission, Member
from .serializers import DevicePermissionSerializer, DeviceSerializer, MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DevicePermissionViewSet(viewsets.ModelViewSet):
    queryset = DevicePermission.objects.all()
    serializer_class = DevicePermissionSerializer
    serializer_class = DevicePermissionSerializer
