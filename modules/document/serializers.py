from modules.reactions.serializers import DislikeSerializer, LikeSerializer
from modules.tags.models import Tag
from .models import Document, DocumentType
from rest_framework import serializers
from modules.tags.serializers import TagSerializer
from modules.reactions.serializers import LikeSerializer, DislikeSerializer
from modules.files.models import File
from modules.files.serializers import FileDocumentSerializer


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

    class Meta:
        model = Document
        fields = "__all__"


class NewsCreateSerializer(serializers.Serializer):
    preview_title = serializers.CharField()
    preview_image = serializers.ImageField()
    text = serializers.CharField()
    tags = serializers.ListField(child=serializers.CharField())

    def create(self, validated_data):
        tags = []
        for tag in validated_data["tags"]:
            tags.append(Tag.objects.get_or_create(name=tag)[0])
        file = File.objects.create(file=validated_data["preview_image"],
                                   filename=validated_data["preview_image"].name,
                                   file_type_id="news_preview_image")
        validated_data["preview_image"] = FileDocumentSerializer(file).data
        news = Document.objects.create(doc_type_id="news", json_data=validated_data)
        news.tags.set(tags)
        return validated_data
