from rest_framework import serializers

from .models import Company, Vacancy
from modules.document.serializers.document import DocumentSerializer


class WorkCompanySerializer(serializers.ModelSerializer):
    doc = DocumentSerializer(many=False, read_only=True)

    class Meta:
        model = Company
        fields = "__all__"


class WorkVacancySerializer(serializers.ModelSerializer):
    doc = DocumentSerializer(many=False, read_only=True)

    class Meta:
        model = Vacancy
        fields = "__all__"

