from django.urls import path
from rest_framework.routers import DefaultRouter
from .views.news import ReadNews
from .views.resume import create_resume, update_resume


router = DefaultRouter()
router.register("news", ReadNews)

urlpatterns = [
    path("resumes/", create_resume),
    path("resumes/<int:id>/", update_resume),
]

urlpatterns += router.urls

