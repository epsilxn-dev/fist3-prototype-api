from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/v1/', include("modules.user.urls")),
    path('api/v1/', include("modules.document.urls")),
    path('api/v1/', include("modules.reactions.urls")),
    path('api/v1/', include("modules.admin.urls")),
    path('api/v1/', include("modules.files.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
