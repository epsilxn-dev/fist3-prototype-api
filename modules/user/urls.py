from django.urls import path
from rest_framework import routers
from .views.user_views import (UserViewSet, UserPasswordChange, UserAvatarChange, UserPrivateDataChange,
                    UserEmailChange)
from .views.auth_views import (Registration, Authorization, Logout, NewTokenPair, ConfirmEmail, ForgotPassword,
                                ForgotPasswordConfirm)

router = routers.DefaultRouter()
router.register("users", UserViewSet)
urlpatterns = [
    path("users/change/password/", UserPasswordChange.as_view()),
    path("users/change/avatar/", UserAvatarChange.as_view()),
    path("users/change/private_data/", UserPrivateDataChange.as_view()),
    path("users/change/email/", UserEmailChange.as_view()),
    path("auth/register/", Registration.as_view()),
    path("auth/authorize/", Authorization.as_view()),
    path("auth/logout/", Logout.as_view()),
    path("auth/token-pair/", NewTokenPair.as_view()),
    path("auth/confirm-registration/", ConfirmEmail.as_view()),
    path("auth/recover-password/", ForgotPassword.as_view()),
    path("auth/confirm-password/", ForgotPasswordConfirm.as_view())
] + router.urls
