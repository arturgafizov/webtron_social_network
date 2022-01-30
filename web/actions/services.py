from main.decorators import except_shell

from .models import LikeDislike


class ActionsService:
    @staticmethod
    @except_shell((LikeDislike.DoesNotExist, ))
    def get_like_dislike_obj(user_id: int, post):
        return LikeDislike.objects.get(user_id=user_id, post=post)
