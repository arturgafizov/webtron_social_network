from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse_lazy
from math import radians, asin, sqrt, sin, cos
from main.tasks import send_information_email
from django.core.cache import cache

from django.conf import settings

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

