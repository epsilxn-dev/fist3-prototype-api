from rest_framework import serializers
from .models import Department, Direction, Lecturer
from modules.document.serializers.document import DocumentSerializer


class StructureDepartmentSerializer(serializers.ModelSerializer):
    doc = DocumentSerializer(many=False, read_only=True)

    class Meta:
        model = Department
        fields = "__all__"


class StructureDirectionSerializer(serializers.ModelSerializer):
    doc = DocumentSerializer(many=False, read_only=True)

    class Meta:
        model = Direction
        fields = "__all__"


class StructureLecturerSerializer(serializers.ModelSerializer):
    doc = DocumentSerializer(many=False, read_only=True)

    class Meta:
        model = Lecturer
        fields = "__all__"
