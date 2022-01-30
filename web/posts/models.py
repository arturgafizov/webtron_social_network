from django.db import models
from django.contrib.auth import get_user_model

from actions.choices import LikeStatus
from .choices import PostStatus

User = get_user_model()


class Post(models.Model):
    user = models. ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='post_set')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    status = models.PositiveSmallIntegerField(choices=PostStatus.choices, default=PostStatus.INACTIVE)

    def likes(self) -> int:
        return self.post_likes.filter(vote=LikeStatus.LIKE).count()

    def dislikes(self) -> int:
        return self.post_likes.filter(vote=LikeStatus.DISLIKE).count()
