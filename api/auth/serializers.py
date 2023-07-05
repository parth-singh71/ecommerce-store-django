from rest_framework import serializers, exceptions
from django.contrib.auth import authenticate
from ..models import User


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def validate(self, data):
        username = data.get("username", "")
        email = data.get("email", "")
        password = data.get("password", "")

        if username and email and password:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()
            if user:
                if user.is_active:
                    data["user"] = user
                    data["user_id"] = user.id
                else:
                    msg = "This account has been deactivated"
                    raise exceptions.ValidationError(msg)
            else:
                msg = 'Unable to signup with given credentials.'
                raise exceptions.ValidationError(msg)
        else:
            msg = "Username, Email and Password are required fields and cannot be empty"
            raise exceptions.ValidationError(msg)
        return data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=100)

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                    data["user_id"] = user.id
                else:
                    msg = "This account has been deactivated"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Username or Password Incorrect, Please try again later"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Username and Password are required fields and cannot be empty"
            raise exceptions.ValidationError(msg)
        return data
