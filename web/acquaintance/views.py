import logging
from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from . import services
from . import serializers


User = get_user_model()

logger = logging.getLogger(__name__)

# Create your views here.


class LikesView(GenericAPIView):
    serializer_class = serializers.LikeSerializers

    def get_queryset(self):
        return User.objects.filter(is_active=True)

    def post(self, request, pk):
        like_user = self.get_object()
        request.user.like.add(like_user)
        return Response({'detail': True})
