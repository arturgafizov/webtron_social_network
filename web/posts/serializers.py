from rest_framework import serializers

from main.serializers import UserSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'content', 'created', 'likes', 'dislikes')

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        if user.is_authenticated:
            validated_data['user'] = user
        return Post.objects.create(**validated_data)
