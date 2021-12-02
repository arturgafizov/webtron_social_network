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


def get_user_distance(user1, user2):
    cache_key: str = cache.make_key('distance', f'{user1.id}:{user2.id}')
    print(cache_key)
    if cache_key in cache:
        print('in cache', )
        return cache.get(cache_key)
    lon1 = user1.longitude
    lat1 = user1.latitude
    lon2 = user2.longitude
    lat2 = user2.latitude
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    length = 2 * asin(sqrt(sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2))
    km = round(6371 * length, 3)
    cache.set(cache_key, km, timeout=settings.CACHE_DISTANCE_TIMEOUT)
    return km
