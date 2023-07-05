from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import status, viewsets
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .serializers import LoginSerializer, SignupSerializer


# Create your views here.
class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        django_login(request=request, user=user)
        token, created = Token.objects.get_or_create(user=user)
        json = {
            "token": token.key,
            "user_id": serializer.validated_data['user_id']
        }
        return Response(json, status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        json = {
            "token": token.key,
            "user_id": serializer.validated_data["user_id"]
        }
        return Response(json, status=status.HTTP_200_OK)


class LogoutView(APIView):
    authentication_classes = [
        TokenAuthentication,
        SessionAuthentication,
        BasicAuthentication
    ]

    def get(self, request):
        request.user.auth_token.delete()
        django_logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
