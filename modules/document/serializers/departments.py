from rest_framework import serializers
from core.doc_action import register_document, update_document
from modules.structure.models import Department
from modules.structure.serializers import StructureDepartmentSerializer


class DepartmentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=300)
    text = serializers.CharField()
    tags = serializers.ListField(child=serializers.CharField(max_length=50))

    def create(self, validated_data):
        department_doc = register_document("department",
                                           validated_data,
                                           validated_data["user"],
                                           validated_data["tags"])
        department = Department.objects.create(name=validated_data["name"],
                                               address=validated_data["address"],
                                               text=validated_data["text"],
                                               doc_id=department_doc.id)
        return StructureDepartmentSerializer(department).data

    def update(self, instance, validated_data):
        department_doc = update_document(instance, validated_data, validated_data["user"], validated_data["tags"])
        department = Department.objects.filter(doc_id=department_doc.id)[0]
        department.name = validated_data["name"]
        department.address = validated_data["address"]
        department.text = validated_data["text"]
        department.save()
        return StructureDepartmentSerializer(department).data
