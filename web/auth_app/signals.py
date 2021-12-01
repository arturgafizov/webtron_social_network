from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .processors import add_watermark
from .tasks import get_user_coordinates

User = get_user_model()


@receiver(post_save, sender=User)
def add_user_watermark(sender, created, instance, **kwargs):
    ava = instance.avatar
    ava = ava.path
    if created:
        watermark = "static/watermark_normal.png"
        result_image = add_watermark(ava, watermark)
        print(result_image)
