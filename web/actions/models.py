from django.db import models
from django.contrib.auth import get_user_model

from actions.choices import LikeStatus
from posts.models import Post

User = get_user_model()


class LikeDislike(models.Model):
    vote = models.IntegerField(choices=LikeStatus.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')
    objects = models.Manager()
