from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(detail=False, methods=['get'], url_path='member/(?P<pk>[^/.]+)')
    def by_member(self, request, pk=None):
        permissions = DevicePermission.objects.filter(user_id=pk)
        serializer = self.get_serializer(permissions, many=True)
        return Response(serializer.data)
