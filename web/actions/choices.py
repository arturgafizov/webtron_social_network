from django.db.models import IntegerChoices


class LikeStatus(IntegerChoices):
    LIKE = (1, 'like')
    DISLIKE = (-1, 'dislike')
