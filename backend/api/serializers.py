from rest_framework import serializers

from .models import Device, DevicePermission, Member


class MemberSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Member
        fields = (
            "id",
            "username",
            "email",
            "phone",
            "avatar",
            "is_active",
            "is_staff",
            "is_superuser",
            "password",
        )
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ("id", "name", "device_type", "room", "status", "last_updated")


class DevicePermissionSerializer(serializers.ModelSerializer):
    user = MemberSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=Member.objects.all(), source="user", write_only=True
    )
    device = DeviceSerializer(read_only=True)
    device_id = serializers.PrimaryKeyRelatedField(
        queryset=Device.objects.all(), source="device", write_only=True
    )

    class Meta:
        model = DevicePermission
        fields = ("id", "user", "user_id", "device", "device_id", "can_control")
        model = DevicePermission
        fields = ("id", "user", "user_id", "device", "device_id", "can_control")
        model = DevicePermission
        fields = ("id", "user", "user_id", "device", "device_id", "can_control")
