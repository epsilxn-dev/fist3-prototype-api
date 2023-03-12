from rest_framework import serializers

from core.doc_action import register_document, update_document
from modules.structure.models import Direction
from modules.structure.serializers import StructureDirectionSerializer


class DirectionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    text = serializers.CharField()
    department = serializers.IntegerField()
    tags = serializers.ListField(child=serializers.CharField(max_length=50))

    def create(self, validated_data):
        direction_doc = register_document("direction", validated_data, validated_data["user"], validated_data["tags"])
        direction = Direction.objects.create(name=validated_data["name"],
                                             text=validated_data["text"],
                                             department_id=validated_data["department"],
                                             doc_id=direction_doc.id)
        return StructureDirectionSerializer(direction).data

    def update(self, instance, validated_data):
        direction_doc = update_document(instance, validated_data, validated_data["user"], validated_data["tags"])
        direction = Direction.objects.filter(doc_id=direction_doc.id)[0]
        direction.name = validated_data["name"]
        direction.text = validated_data["text"]
        direction.department_id = validated_data["department"]
        direction.save()
        return StructureDirectionSerializer(direction).data
