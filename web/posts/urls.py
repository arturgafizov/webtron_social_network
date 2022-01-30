from rest_framework.routers import DefaultRouter

from . import views

app_name = 'posts'

router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='post')

urlpatterns = [

]

urlpatterns += router.urls
