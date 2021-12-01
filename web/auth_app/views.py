from django.contrib.auth import get_user_model
from django.contrib.auth import logout as django_logout
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, JSONParser
from dj_rest_auth import views as auth_views

from .serializers import LoginSerializer, UserSignUpSerializer
from .services import full_logout

User = get_user_model()


class LoginView(auth_views.LoginView):
    serializer_class = LoginSerializer


class SignUpView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSignUpSerializer


class LogoutView(auth_views.LogoutView):
    allowed_methods = ('POST', 'OPTIONS')

    def session_logout(self):
        django_logout(self.request)

    def logout(self, request):
        self.session_logout()
        response = full_logout(request)
        return response
