from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from core.exception import ClientException
from modules.document.serializers.directions import DirectionSerializer
from rest_framework.request import Request
from core.permissions import AdminAndHigher
from core.doc_action import get_document


@api_view(["POST"])
@permission_classes([AdminAndHigher])
def create_direction(request: Request):
    serializer = DirectionSerializer(data=request.data)
    if not serializer.is_valid():
        raise ClientException(serializer.errors)
    data = serializer.save(user=request.user.id)
    return Response(data, status=201)


@api_view(["PUT"])
@permission_classes([AdminAndHigher])
def update_direction(request: Request, **kwargs):
    direction = get_document(kwargs["id"])
    serializer = DirectionSerializer(direction, data=request.data)
    if not serializer.is_valid():
        raise ClientException(serializer.errors)
    data = serializer.save(user=request.user.id)
    return Response(data, status=201)
