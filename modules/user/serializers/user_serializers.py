from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "image", "role", "phone", "middle_name",
                  "birth_date", "gender"]