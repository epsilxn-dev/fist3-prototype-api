from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import AccessTokens, RefreshTokens, User


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ("id", "username", "is_superuser", "is_staff", "is_stand", "is_graduate", "is_lecturer")
    ordering = ("-is_superuser", "id")


@admin.register(AccessTokens)
class AccessTokens(admin.ModelAdmin):
    list_display = ("token", "user", "valid_to")


@admin.register(RefreshTokens)
class AccessTokens(admin.ModelAdmin):
    list_display = ("token", "user", "valid_to", "access")
