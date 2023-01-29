from django.urls import path
from rest_framework.routers import DefaultRouter
from .views.news import ReadNews
from .views.admin.news import ActionNews


router = DefaultRouter()
router.register("news", ReadNews)

urlpatterns = [
    path("admin/news/create/", ActionNews.as_view()),
]

urlpatterns += router.urls