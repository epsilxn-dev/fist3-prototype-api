from django.contrib.auth.hashers import check_password
from rest_framework import permissions, status
from rest_framework.request import Request
from rest_framework.response import Response

from core.exception import ClientException, ServerException
from core.security.jwt import generate_jwt_pair, decode_jwt
from core.utils.esia import get_refresh_dict
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from ..models import User, AccessTokens, RefreshTokens
from ..serializers import RegistrationSerializer, AuthRespSerializer, \
    ConfirmRegistrationSerializer, ConfirmPasswordChangeSerializer, PasswordChangeSerializer


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
@authentication_classes([])
def register_step_1(request: Request):
    data = RegistrationSerializer(data=request.data)
    if not data.is_valid():
        raise ClientException(data.errors)
    data.save()
    return Response(data.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
@authentication_classes([])
def register_step_2(request: Request):
    code = request.data.get("code")
    id = request.data.get("id")
    candidates = User.objects.filter(code_email=code, id=id)
    if len(candidates) == 1:
        user = candidates[0]
        serializer = ConfirmRegistrationSerializer(
            user, data=request.data, partial=True)
        if not serializer.is_valid():
            raise ServerException()
        serializer.save()
        return Response(status=204)
    raise ClientException("Ошибка подтверждения регистрации. Пожалуйста, пройдите процедуру регистрации через 30 минут. "
                          "В случае возникновения повторной ошибки, пожалуйста, свяжитесь со службой поддержки!", status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
@authentication_classes([])
def authorize(request: Request):
    data = request.data
    try:
        candidate = User.objects.get(username=data.get(
            "username"), is_confirmed_email=True)
    except Exception as e:
        raise ClientException("Неверный логин или пароль",
                              status.HTTP_400_BAD_REQUEST)
    if check_password(data.get("password"), candidate.password):
        pair = generate_jwt_pair(candidate)
        response_data = {
            "access": pair.access.token,
            "user": candidate
        }
        response_cookie = get_refresh_dict(pair.refresh.token)
        response = Response(AuthRespSerializer(
            response_data).data, status=status.HTTP_200_OK)
        response.set_cookie(**response_cookie)
        return response
    raise ClientException("Неверный логин или пароль",
                          status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated])
def logout(request: Request):
    AccessTokens.objects.get(token=request.auth.token).delete()
    response = Response(status=status.HTTP_204_NO_CONTENT)
    response.set_cookie(**get_refresh_dict())
    return response


@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated])
def logout_all(request: Request):
    AccessTokens.objects.filter(user_id=request.user.id).delete()
    response = Response(status=status.HTTP_204_NO_CONTENT)
    response.set_cookie(**get_refresh_dict())
    return response


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
@authentication_classes([])
def get_new_token_pair(request: Request):
    token = request.COOKIES.get("refresh")
    if token is None or token == '':
        raise ClientException("Необходимо перезайти",
                              status.HTTP_400_BAD_REQUEST)
    decoded_token = decode_jwt(token)
    if not decoded_token.is_valid:
        raise ClientException("Необходимо перезайти",
                              status.HTTP_401_UNAUTHORIZED)
    refresh_model = RefreshTokens.objects.get(token=decoded_token.token)
    new_pair = generate_jwt_pair(refresh_model.user)
    AccessTokens.objects.get(token=refresh_model.access.token).delete()
    response = Response({"access": new_pair.access.token},
                        status=status.HTTP_200_OK)
    response.set_cookie(**get_refresh_dict(new_pair.refresh.token))
    return response


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
@authentication_classes([])
def restore_password_step1(request: Request):
    serializer = PasswordChangeSerializer(data=request.data)
    if not serializer.is_valid():
        raise ClientException(serializer.errors)
    candidates = User.objects.filter(
        email=serializer.validated_data.get("email"))
    if len(candidates) == 1:
        serializer.instance = candidates[0]
        serializer.save()
        return Response(status=200)
    raise ServerException()


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
@authentication_classes([])
def restore_password_step2(request: Request):
    serializer = ConfirmPasswordChangeSerializer(data=request.data)
    if not serializer.is_valid():
        raise ClientException(serializer.errors)
    candidates = User.objects.filter(
        token_password_change=serializer.validated_data.get("token"))
    if len(candidates) == 1:
        serializer.instance = candidates[0]
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    raise ServerException()
