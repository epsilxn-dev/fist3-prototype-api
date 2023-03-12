from modules.document.models import Document
from ..serializers.document import DocumentSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
import json


class ReadNews(ReadOnlyModelViewSet):
    queryset = Document.objects.filter(doc_type="news", is_moderated=True, is_ready_for_publish=True, doc_type__is_active_type=True)
    permission_classes = [AllowAny]
    serializer_class = DocumentSerializer

    def list(self, request: Request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        for item in response.data["results"]:
            likes = json.loads(json.dumps(item["likes"]))
            for like in likes:
                if like["user"] == self.request.user.id:
                    item["liked_by_me"] = True
            item["likes"] = len(likes)
            dislikes = json.loads(json.dumps(item["dislikes"]))
            for dislike in dislikes:
                if dislike["user"] == self.request.user.id:
                    item["disliked_by_me"] = True
            item["dislikes"] = len(item["dislikes"])
        return response

