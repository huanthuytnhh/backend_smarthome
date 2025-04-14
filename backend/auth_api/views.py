from django.contrib.auth import login, logout
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer, RegisterSerializer


class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {"user": serializer.data, "token": token.key},
            status=status.HTTP_201_CREATED,
        )


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "token": token.key,
            },
            status=status.HTTP_200_OK,
        )


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except AttributeError:
            pass

        logout(request)
        return Response({"message": "Đăng xuất thành công"}, status=status.HTTP_200_OK)
        return Response({"message": "Đăng xuất thành công"}, status=status.HTTP_200_OK)
        return Response({"message": "Đăng xuất thành công"}, status=status.HTTP_200_OK)
