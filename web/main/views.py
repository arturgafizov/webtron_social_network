from math import cos, radians, sqrt
from django.db.models import F
from django.conf import settings
from django.db.models.functions import Sqrt, Abs
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.parsers import JSONParser, MultiPartParser

from . import serializers
from .serializers import UserSerializer
from .filters import ListUserFilter
User = get_user_model()


class TemplateAPIView(APIView):
    """ Help to build CMS System using DRF, JWT and Cookies
        path('some-path/', TemplateAPIView.as_view(template_name='template.html'))
    """
    permission_classes = (AllowAny,)
    template_name = ''

    @swagger_auto_schema(auto_schema=None)
    def get(self, request, *args, **kwargs):
        return Response()


class ViewSet(ModelViewSet):
    http_method_names = ('get', 'post', 'put', 'delete')


class UserModelViewSet(ViewSet):
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, JSONParser, )

    def get_queryset(self):
        return User.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserListView(ListAPIView):
    serializer_class = serializers.UserSerializer
    filterset_class = ListUserFilter

    def get_queryset(self):
        queryset = User.objects.filter(is_active=True).exclude(id=self.request.user.id)
        return queryset
