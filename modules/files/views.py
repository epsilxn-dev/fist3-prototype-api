from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from core.exception import ClientException
from .serializers import UploadFileSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_file(request: Request):
    serializer = UploadFileSerializer(data=request.data)
    if not serializer.is_valid():
        raise ClientException(serializer.errors)
    data = serializer.save(user=request.user.id)
    return Response(data, status=200)
