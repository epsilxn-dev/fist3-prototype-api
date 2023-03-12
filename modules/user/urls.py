from django.urls import path
from rest_framework import routers
from .views.user_views import (UserViewSet, UserPasswordChange, UserAvatarChange, UserPrivateDataChange,
                               UserEmailChange)
from .views.auth_views import (register_step_1, register_step_2, authorize, logout, get_new_token_pair, restore_password_step1, restore_password_step2,
                               logout_all)

router = routers.DefaultRouter()
router.register("users", UserViewSet)
urlpatterns = [
    path("users/change/password/", UserPasswordChange.as_view()),
    path("users/change/avatar/", UserAvatarChange.as_view()),
    path("users/change/private_data/", UserPrivateDataChange.as_view()),
    path("users/change/email/", UserEmailChange.as_view()),
    path("auth/register/step1/", register_step_1),
    path("auth/register/step2/", register_step_2),
    path("auth/authorize/", authorize),
    path("auth/logout/", logout),
    path("auth/full-logout/", logout_all),
    path("auth/token-pair/", get_new_token_pair),
    path("auth/recover-password/", restore_password_step1),
    path("auth/confirm-password/", restore_password_step2)
] + router.urls
