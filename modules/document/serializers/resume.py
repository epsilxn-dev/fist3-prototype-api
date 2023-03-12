from rest_framework import serializers

from core.doc_action import register_document, update_document
from core.exception import ClientException
from modules.files.models import File
from modules.files.serializers import GetFileSerializer
from modules.document.serializers.document import DocumentSerializer
from modules.document.models import Document


class ResumeSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    first_name = serializers.CharField(max_length=70)
    last_name = serializers.CharField(max_length=70)
    middle_name = serializers.CharField(max_length=70, required=False)
    fork_start = serializers.IntegerField(required=False)
    fork_end = serializers.IntegerField(required=False)
    currency_type = serializers.CharField(default="руб.", required=False)
    image = serializers.IntegerField()
    experience = serializers.CharField(max_length=10)
    text = serializers.CharField()
    tags = serializers.ListSerializer(child=serializers.CharField(max_length=50))

    def create(self, validated_data):
        user_id = validated_data["user"]
        candidates = Document.objects.filter(create_by_id=user_id, doc_type_id="resume")
        if len(candidates) > 0:
            raise ClientException("У вас уже есть созданное резюме!")
        image = File.objects.get(id=validated_data["image"])
        resume_doc = register_document("resume", validated_data, validated_data["user"], validated_data["tags"])
        image.doc_id = resume_doc.id
        image.save()
        validated_data["image"] = GetFileSerializer(image).data
        resume_doc.json_data = validated_data
        resume_doc.save()
        return DocumentSerializer(resume_doc).data

    def update(self, instance: Document, validated_data):
        user_id = validated_data["user"]
        if instance.create_by_id != int(user_id):
            raise ClientException()
        if int(instance.json_data["image"]["id"]) == validated_data["image"]:
            image = File.objects.get(id=validated_data["image"])
        else:
            File.objects.filter(doc_id=instance.id).delete()
            image = File.objects.get(id=validated_data["image"])
        validated_data["image"] = GetFileSerializer(image).data
        resume_doc = update_document(instance, validated_data, user_id, validated_data["tags"])
        return DocumentSerializer(resume_doc).data
