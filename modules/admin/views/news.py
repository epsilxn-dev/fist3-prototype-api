from rest_framework.decorators import api_view, permission_classes
from core.permissions import AdminAndHigher, ModeratorAndHigher
from rest_framework.request import Request
from rest_framework.response import Response
from modules.document.serializers.news import NewsSerializer
from core.exception import ClientException
from core.doc_action import get_document


@api_view(["POST"])
@permission_classes([ModeratorAndHigher])
def create_news(request: Request):
    serializer = NewsSerializer(data=request.data)
    if not serializer.is_valid():
        raise ClientException(serializer.errors)
    data = serializer.save(user=request.user.id)
    return Response(data, status=201)


@api_view(["PUT"])
@permission_classes([ModeratorAndHigher])
def update_news(request: Request, **kwargs):
    news = get_document(kwargs["id"])
    serializer = NewsSerializer(news, data=request.data)
    if not serializer.is_valid():
        raise ClientException(serializer.errors)
    data = serializer.save(user=request.user.id)
    return Response(data, status=200)
