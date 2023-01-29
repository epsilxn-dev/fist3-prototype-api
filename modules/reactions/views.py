from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from core.exception import ServerException, ClientException
from modules.document.models import Document
from modules.reactions.models import Like, Dislike


class ToggleReaction(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        doc_id = request.data.get("doc_id")
        btn_clicked = request.data.get("btn_click")
        document = Document.objects.get(id=doc_id)
        liked_by_me = document.likes.filter(user_id=request.user.id).count() > 0
        disliked_by_me = document.dislikes.filter(user_id=request.user.id).count() > 0
        like = Like.objects.get_or_create(user_id=request.user.id)[0]
        dislike = Dislike.objects.get_or_create(user_id=request.user.id)[0]
        if btn_clicked == "like":
            if not liked_by_me and not disliked_by_me:
                document.likes.add(like)
            elif liked_by_me and not disliked_by_me:
                document.likes.remove(like)
            elif not liked_by_me and disliked_by_me:
                document.dislikes.remove(dislike)
                document.likes.add(like)
            else:
                raise ServerException(f"Одновременно не может стоять like и dislike. doc_id: {doc_id}")
        elif btn_clicked == "dislike":
            if not liked_by_me and not disliked_by_me:
                document.dislikes.add(dislike)
            elif liked_by_me and not disliked_by_me:
                document.likes.remove(like)
                document.dislikes.add(dislike)
            elif not liked_by_me and disliked_by_me:
                document.dislikes.remove(dislike)
            else:
                raise ServerException(f"Одновременно не может стоять like и dislike. doc_id: {doc_id}")
        else:
            raise ClientException(f"Неизвестный тип действия: {btn_clicked}")
        document.save()
        return Response()
