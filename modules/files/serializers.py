import os
import uuid

from rest_framework import serializers
from pathlib import Path
from core.exception import ClientException
from django.conf import settings
import json

from .models import File, FileType


class GetFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


class UploadFileSerializer(serializers.Serializer):
    file = serializers.FileField()
    file_type = serializers.CharField(max_length=255)

    def create(self, validated_data):
        file_type = FileType.objects.get(file_type=validated_data['file_type'])
        file_path_dir = settings.BASE_DIR / settings.MEDIA_ROOT / file_type.save_path
        file_path_dir.mkdir(parents=True, exist_ok=True)
        file_name = validated_data["file"].name
        file_path = file_path_dir / file_name
        if os.path.exists(file_path):
            file_name = str(uuid.uuid4()) + file_name
            file_path = file_path_dir / file_name
        with open(file_path, "wb+") as file:
            for chunk in validated_data["file"].chunks():
                file.write(chunk)
        file = File.objects.create(file="/" + str(file_path.relative_to(settings.BASE_DIR)).replace("\\", "/"),
                                   filename=file_name,
                                   file_type_id=validated_data["file_type"],
                                   create_by_id=validated_data["user"])
        return GetFileSerializer(file).data

    def update(self, instance, validated_data):
        raise ClientException()
