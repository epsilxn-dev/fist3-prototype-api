from modules.reactions.serializers import DislikeSerializer, LikeSerializer
from ..models import Document, DocumentType
from rest_framework import serializers
from modules.reactions.serializers import LikeSerializer, DislikeSerializer
from modules.user.serializers import UserSerializer


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    doc_type = DocumentTypeSerializer(many=False, read_only=True)
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    dislikes = DislikeSerializer(many=True, read_only=True)
    liked_by_me = serializers.BooleanField(default=None)
    disliked_by_me = serializers.BooleanField(default=None)
    create_by = UserSerializer(many=False, read_only=True)
    update_by = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Document
        fields = "__all__"

