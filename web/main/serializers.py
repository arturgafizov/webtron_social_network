from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'gender', 'avatar', 'email')
        extra_kwargs = {
            'avatar': {'read_only': False},
        }

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)
