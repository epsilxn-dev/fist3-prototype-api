from rest_framework import serializers


class VacancySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    text = serializers.CharField(max_length=300)
    text_markup = serializers.CharField()
    company = serializers.IntegerField()
