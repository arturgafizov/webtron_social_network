from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .services import CeleryService

User = get_user_model()


@receiver(m2m_changed, sender=User.like.through)
def send_user_email(sender, **kwargs):
    if kwargs.get('action') != 'post_add':
        return
    instance = kwargs.get('instance')
    user_ids: list = list(kwargs.get('pk_set'))
    is_liked: bool = instance.subscribers.filter(id__in=user_ids).exists()
    # print(is_liked)
    if is_liked:
        liked_user = instance.subscribers.get(id=user_ids[0])
        CeleryService.send_email_like(instance, liked_user)
