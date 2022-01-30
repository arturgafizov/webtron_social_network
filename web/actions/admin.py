from django.contrib import admin

from actions.models import LikeDislike


@admin.register(LikeDislike)
class LikeDislikeAdmin(admin.ModelAdmin):
    list_display = ('vote', 'user', 'date')
