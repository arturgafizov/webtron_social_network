from datetime import datetime
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'gender', 'email')
        extra_kwargs = {
            'avatar': {'read_only': False},
        }

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)
