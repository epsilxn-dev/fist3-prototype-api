from core.exception import ClientException
from core.permissions import AdminAndHigher
from ...serializers import NewsCreateSerializer
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class ActionNews(APIView):
    permission_classes = [AdminAndHigher]

    def post(self, request: Request, *args, **kwargs):
        serializer = NewsCreateSerializer(data=request.data)
        if not serializer.is_valid():
            raise ClientException(serializer.errors)
        serializer.save()
        return Response(serializer.data, status=201)

    def patch(self, request: Request, *args, **kwargs):
        ...

    def delete(self, request: Request, *args, **kwargs):
        ...
