from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DevicePermissionViewSet, DeviceViewSet, MemberViewSet

router = DefaultRouter()
router.register(r"members", MemberViewSet)
router.register(r"devices", DeviceViewSet)
router.register(r"permissions", DevicePermissionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
