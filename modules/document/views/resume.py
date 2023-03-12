from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from modules.document.serializers.resume import ResumeSerializer
from core.exception import ClientException
from core.doc_action import get_document


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_resume(request: Request):
    serializer = ResumeSerializer(data=request.data)
    if not serializer.is_valid():
        raise ClientException(serializer.errors)
    data = serializer.save(user=request.user.id)
    return Response(data, status=201)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_resume(request: Request, **kwargs):
    doc = get_document(kwargs["id"])
    serializer = ResumeSerializer(doc, data=request.data)
    if not serializer.is_valid():
        raise ClientException(serializer.errors)
    data = serializer.save(user=request.user.id)
    return Response(data, status=200)
