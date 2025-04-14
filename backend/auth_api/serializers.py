from api.models import Member
from django.contrib.auth import authenticate
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Member
        fields = ("id", "username", "email", "phone", "password")

    def create(self, validated_data):
        user = Member.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            phone=validated_data.get("phone", ""),
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs["username"], password=attrs["password"])

        if not user:
            raise serializers.ValidationError(
                "Thông tin đăng nhập không chính xác. Vui lòng thử lại."
            )
        if not user.is_active:
            raise serializers.ValidationError("Tài khoản người dùng đã bị vô hiệu hóa.")

        return {"user": user}
