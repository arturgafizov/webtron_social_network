from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe


from .managers import UserManager


def avatar_upload_patch(obj, filename: str):
    return f"avatar_images/{obj.email}/{filename}"


class User(AbstractUser):

    class GenderChoice(models.TextChoices):
        MALE = ('male', 'Male')
        FEMALE = ('female', 'Female')

    username = None
    email = models.EmailField(_('Email address'), unique=True)
    gender = models.CharField(max_length=6, choices=GenderChoice.choices)
    avatar = models.ImageField(upload_to=avatar_upload_patch, default='default_avatar.jpeg')
    like = models.ManyToManyField('self', related_name='subscribers', symmetrical=False, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.email

    def full_name(self):
        return super().get_full_name()
