from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'acquaintance'

router = DefaultRouter()

urlpatterns = [
    path('clients/<pk>/match/', views.LikesView.as_view(), name='like')
]

urlpatterns += router.urls
