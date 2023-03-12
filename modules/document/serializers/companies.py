from rest_framework import serializers

from core.constants import DocTypes
from core.doc_action import register_document, update_document
from modules.work.models import Company
from modules.work.serializers import WorkCompanySerializer
from modules.files.models import File
from modules.files.serializers import GetFileSerializer


class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    address = serializers.CharField(max_length=200)
    description = serializers.CharField()
    email = serializers.CharField(max_length=320, required=False)
    phone = serializers.CharField(max_length=16, required=False)
    image = serializers.IntegerField()

    def create(self, validated_data):
        company_doc = register_document(DocTypes.COMPANY, validated_data, validated_data["user"])
        img = File.objects.get(id=validated_data["image"])
        img.doc_id = company_doc.id
        img.save()
        validated_data["image"] = GetFileSerializer(img).data
        company_doc.json_data = validated_data
        company_doc.save()
        company = Company.objects.create(name=validated_data["name"],
                                         address=validated_data["address"],
                                         description=validated_data["description"],
                                         email=validated_data["email"],
                                         phone=validated_data["phone"],
                                         doc_id=company_doc.id)
        return WorkCompanySerializer(company).data

    def update(self, instance, validated_data):
        image = File.objects.get(id=validated_data["image"])
        if instance.json_data["image"]["id"] != validated_data["image"]:
            File.objects.filter(id=instance.json_data["image"]["id"]).delete()
            image.doc_id = instance.id
            image.save()
        validated_data["image"] = GetFileSerializer(image).data
        company_doc = update_document(instance, validated_data, validated_data["user"])
        company = Company.objects.filter(doc_id=company_doc.id)[0]
        company.name = validated_data["name"]
        company.address = validated_data["address"]
        company.description = validated_data["description"]
        company.email = validated_data["email"]
        company.phone = validated_data["phone"]
        company.save()
        return WorkCompanySerializer(company).data


