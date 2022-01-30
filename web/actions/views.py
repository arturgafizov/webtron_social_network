from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from .models import LikeDislike


class LikeDislikeView(GenericAPIView):
    serializer_class = serializers.LikeDislikeSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return LikeDislike.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data, status=status.HTTP_201_CREATED)
