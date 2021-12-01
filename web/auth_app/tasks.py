import random

from src.celery import app
from django.contrib.auth import get_user_model
# from django.contrib.gis.geoip2 import GeoIP2


User = get_user_model()


@app.task()
def get_user_coordinates(user_ip: str, user_id: int):
    user = User.objects.get(id=user_id)
    longitude, latitude = (random.random() * 2.0, random.random() * 2.0)
    user.longitude = longitude
    user.latitude = latitude
    user.save(update_fields=['latitude', 'longitude'])
