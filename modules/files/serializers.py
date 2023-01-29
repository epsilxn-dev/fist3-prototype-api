from rest_framework import serializers

from .models import File, FileType, UserFile

class FileDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"