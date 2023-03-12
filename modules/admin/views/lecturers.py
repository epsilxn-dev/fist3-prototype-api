from rest_framework import views

from core.permissions import AdminAndHigher


class AddLecturerView(views.APIView):
    permission_classes = [AdminAndHigher]

    def post(self, request, *args, **kwargs):
        ...


class UpdateLecturerView(views.APIView):
    permission_classes = [AdminAndHigher]

    def patch(self, request, *args, **kwargs):
        ...
