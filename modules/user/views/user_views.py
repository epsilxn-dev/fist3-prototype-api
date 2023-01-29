from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..serializers import UserSerializer
from core.utils.esia import check_password_by_request

User = get_user_model()


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    search_fields = ["^username"]
    http_method_names = ["get"]


class UserPasswordChange(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request: Request, *args, **kwargs):
        if not check_password_by_request(request):
            return Response("Пароли не совпадают", status=403)
        password = request.data.get("password")
        if password:
            user = User.objects.get(id=request.user.id)
            user.password = make_password(password)
            user.save()
            return Response(status=200)
        else:
            return Response("Не был предоставлен новый пароль", status=400)


class UserAvatarChange(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request: Request, *args, **kwargs):
        avatar = request.data.get("avatar")
        if avatar:
            request.user.avatar = avatar
            request.user.save()
            return Response({"avatar": request.user.avatar.url}, status=200)
        else:
            return Response("Поле avatar не было предоставлено", status=400)


class UserPrivateDataChange(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request: Request, *args, **kwargs):
        fields = ["first_name", "last_name", "skype", "discord", "phone", "patronymic"]
        try:
            changed_data = {}
            for item in fields:
                if item in request.data:
                    value = request.data.get(item)
                    setattr(request.user, item, value)
                    changed_data[item] = value
            request.user.save()
            return Response(changed_data, status=200)
        except Exception as e:
            print(f"{request.method} {request.path}:", str(self), str(e))
            return Response(str(e), status=400)


class UserEmailChange(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request: Request, *args, **kwargs):
        if not check_password_by_request(request):
            return Response("Пароли не совпадают", status=403)
        email = request.data.get("email")
        if email:
            #request_email_confirmation(request.user, email)
            return Response(status=200)
        else:
            return Response("Поле email не было предоставлено", status=400)

