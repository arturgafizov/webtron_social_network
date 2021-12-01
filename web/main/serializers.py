from math import radians, asin, sqrt, sin, cos

import pytz
from rest_framework import serializers
from .models import User
from .services import CeleryService


class UserSerializer(serializers.ModelSerializer):
    # distance = serializers.SerializerMethodField(method_name='get_distance_between_users')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'gender', 'avatar', 'email') #, 'distance')
        extra_kwargs = {
            'avatar': {'read_only': False},
        }

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)

    # def get_distance_between_users(self, obj):
    #     lon1 = self.context['request'].user.longitude
    #     lat1 = self.context['request'].user.latitude
    #     lon2 = obj.longitude
    #     lat2 = obj.latitude
    #     lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    #     dlon = lon2 - lon1
    #     dlat = lat2 - lat1
    #     length = 2 * asin(sqrt(sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2))
    #     km = 6371 * length
    #     return round(km, 3)
