from django.urls import path
from .views import ToggleReaction


urlpatterns = [
    path("toggle-reaction/", ToggleReaction.as_view()),
]
