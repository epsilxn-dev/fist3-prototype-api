import datetime

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from core.email import send_email_template
from core.exception import ServerException

from core.utils.esia import generate_code_confirmation
from .models import Role, User


class UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "image", "role",
                  "phone", "middle_name", "is_stand", "is_graduate", "is_lecturer"]


class RegistrationSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        role = Role.objects.get(name="USER")
        user.role = role
        code = generate_code_confirmation()
        user.code_email = code
        user.code_email_dt = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
        user.save()
        send_email_template([user.email],
                            "Подтверждение адреса электронной почты",
                            "confirm-registration.html",
                            {"code": code})
        return user

    class Meta:
        model = User
        fields = ["username", "password", "email"]


class AuthorizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class ConfirmRegistrationSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.code_email = None
        instance.code_email_dt = None
        instance.is_active = True
        instance.is_confirmed_email = True
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ["code_email", "email"]


class PasswordChangeSerializer(serializers.Serializer):
    email = serializers.CharField()

    def create(self, validated_data):
        raise ServerException()

    def update(self, instance, validated_data):
        code = generate_code_confirmation()
        instance.code_password = code
        instance.code_password_dt = datetime.datetime.utcnow()
        instance.save()
        send_email_template(
            [validated_data.get("email")],
            "Восстановление пароля",
            "password_forgot.html",
            {"code": code}
        )
        return instance


class ConfirmPasswordChangeSerializer(serializers.Serializer):
    token = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        raise ServerException()

    def update(self, instance, validated_data):
        instance.code_password = None
        instance.code_password_dt = None
        instance.password = make_password(validated_data.get("password"))
        instance.save()
        return instance


class AuthRespSerializer(serializers.Serializer):
    access = serializers.CharField(max_length=2048)
    user = UserSerializer()
