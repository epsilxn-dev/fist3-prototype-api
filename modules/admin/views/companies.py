from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response

from core.exception import ClientException
from modules.document.serializers.companies import CompanySerializer

from core.permissions import AdminAndHigher
from core.doc_action import get_document


@api_view(["POST"])
@permission_classes([AdminAndHigher])
def create_company(request: Request):
    serializer = CompanySerializer(data=request.data)
    if not serializer.is_valid():
        raise ClientException(serializer.errors)
    data = serializer.save(user=request.user.id)
    return Response(data, status=201)


@api_view(["PUT"])
@permission_classes([AdminAndHigher])
def update_company(request: Request, **kwargs):
    doc = get_document(kwargs["id"])
    serializer = CompanySerializer(doc, data=request.data)
    if not serializer.is_valid():
        raise ClientException(serializer.errors)
    data = serializer.save(user=request.user.id)
    return Response(data, status=200)
