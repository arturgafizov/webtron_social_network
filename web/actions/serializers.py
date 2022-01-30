from rest_framework import serializers

from actions.choices import LikeStatus
from actions.services import ActionsService
from posts.choices import PostStatus
from posts.models import Post


class LikeDislikeSerializer(serializers.Serializer):
    vote = serializers.ChoiceField(choices=LikeStatus.choices)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.filter(status=PostStatus.ACTIVE))

    def save(self):
        user = self.context['request'].user
        post: Post = self.validated_data['post']
        vote: int = self.validated_data['vote']
        like_dislike = ActionsService.get_like_dislike_obj(user.id, post)
        if not like_dislike:
            post.post_likes.create(user=user, vote=vote)
        else:
            if like_dislike.vote == vote:
                like_dislike.delete()
            else:
                like_dislike.vote = vote
                like_dislike.save(update_fields=['vote'])

        return self.response_data(post)

    def response_data(self, post) -> dict:

        return {
            'like_count': post.likes(),
            'dislike_count': post.dislikes(),
            'status': self.validated_data['vote']
        }
