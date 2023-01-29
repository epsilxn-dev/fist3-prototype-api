import random

from django.conf import settings
import datetime

from django.contrib.auth.hashers import check_password
from rest_framework.request import Request


def get_refresh_dict(value: str = ""):
    return {
        "key": "refresh",
        "value": value,
        "httponly": True,
        "expires": settings.JWT_REFRESH_LIFETIME + datetime.datetime.now(),
        "samesite": "Lax"
    }


def check_password_by_request(request: Request) -> bool:
    password = request.data.get("checkPassword")
    return password and check_password(password, request.user.password)


def generate_code_confirmation() -> str:
    digit = str(random.randint(0, 999999))
    if len(digit) < 6:
        lead_zeros = (6 - len(digit)) * "0"
        digit = lead_zeros + digit
    return digit
