from django.urls import path
from .views.news import create_news, update_news
from .views.departments import create_department, update_department
from .views.directions import create_direction, update_direction
from .views.companies import create_company, update_company


urlpatterns = [
    path("admin/news/", create_news),
    path("admin/news/<int:id>/", update_news),
    path("admin/departments/", create_department),
    path("admin/departments/<int:id>/", update_department),
    path("admin/directions/", create_direction),
    path("admin/directions/<int:id>/", update_direction),
    path("admin/companies/", create_company),
    path("admin/companies/<int:id>/", update_company),
]


