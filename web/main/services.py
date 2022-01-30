from django.contrib.auth import get_user_model

from main.tasks import send_information_email
from main.decorators import except_shell

User = get_user_model()


class CeleryService:

    @staticmethod
    def send_email_like(user, user2,):
        subject = 'User like'
        html_email_template_name = 'emails/email_user_like.html'
        context = {
            'user': user.get_full_name(),
            'email': user.email,
        }
        to_email = user2.email,
        send_information_email.delay(subject, html_email_template_name, context, to_email)
        context = {
            'user': user2.get_full_name(),
            'email': user2.email,
        }
        to_email = user.email,
        send_information_email.delay(subject, html_email_template_name, context, to_email)


class UserService:

    @staticmethod
    @except_shell((User.DoesNotExist,))
    def get_user(email):
        return User.objects.get(email=email)
