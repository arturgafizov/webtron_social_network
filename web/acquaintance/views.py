import logging
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from acquaintance.serializers import AcquaintanceSerializer

User = get_user_model()

logger = logging.getLogger(__name__)


class LikesView(GenericAPIView):
    serializer_class = AcquaintanceSerializer

    def get_queryset(self):
        return User.objects.filter(is_active=True)

    def post(self, request, pk):
        like_user = self.get_object()
        request.user.like.add(like_user)
        return Response({'detail': True})
