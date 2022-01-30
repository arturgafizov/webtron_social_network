from django.urls import path


from .views import LoginView, LogoutView, SignUpView

app_name = 'auth_app'

urlpatterns = [
    path('sign-in/', LoginView.as_view(), name='api_login'),
    path('sign_up/', SignUpView.as_view(), name='api_sign_up'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
