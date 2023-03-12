import datetime

from rest_framework import serializers

from core.doc_action import register_tags, register_document, update_document
from modules.files.models import File
from modules.files.serializers import GetFileSerializer
from modules.document.models import Document
from modules.document.serializers.document import DocumentSerializer


class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    image = serializers.IntegerField(required=True)
    text = serializers.CharField(required=True)
    tags = serializers.ListField(child=serializers.CharField())

    def create(self, validated_data):
        create_by = validated_data["user"]
        news = register_document("news", validated_data, create_by, validated_data["tags"])
        image = File.objects.get(id=validated_data["image"], doc_id=None)
        image.doc_id = news.id
        image.save()
        validated_data["image"] = GetFileSerializer(image).data
        news.json_data = validated_data
        news.save()
        return DocumentSerializer(news).data

    def update(self, instance: Document, validated_data):
        update_by = validated_data["user"]
        image_id = validated_data["image"]
        if image_id == instance.json_data["image"]["id"]:
            image = File.objects.get(id=validated_data["image"], doc_id=instance.id)
        else:
            File.objects.filter(id=instance.json_data["image"]["id"]).delete()
            image = File.objects.get(id=validated_data["image"], doc_id=None)
            image.doc_id = instance.id
        validated_data["image"] = GetFileSerializer(image).data
        doc = update_document(instance, validated_data, update_by, validated_data["tags"])
        image.save()
        return DocumentSerializer(doc).data
