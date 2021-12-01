from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import RedirectView
from .views import UserModelViewSet, UserListView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user', UserModelViewSet, basename='user')


urlpatterns = [
    path('', login_required(RedirectView.as_view(pattern_name='admin:index'))),
    path('api/list/', UserListView.as_view(), name='list_user'),

]


urlpatterns += router.urls
