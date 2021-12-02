from math import radians, asin, sqrt, sin, cos

import pytz
from rest_framework import serializers
from .models import User
from .services import get_user_distance


class UserSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField(method_name='get_distance_between_users')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'gender', 'avatar', 'email', 'distance')
        extra_kwargs = {
            'avatar': {'read_only': False},
        }

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)

    def get_distance_between_users(self, obj):
        return get_user_distance(self.context['request'].user, obj)
