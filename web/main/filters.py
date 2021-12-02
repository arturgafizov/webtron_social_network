from django_filters import rest_framework as filters

from django.contrib.auth import get_user_model

from .services import get_user_distance

User = get_user_model()


class CharFilter(filters.BaseInFilter, filters.CharFilter, filters.NumberFilter):
    pass


class ListUserFilter(filters.FilterSet):
    gender = filters.ChoiceFilter(choices=User.GenderChoice.choices)
    first_name = filters.CharFilter('first_name', lookup_expr='icontains')
    last_name = filters.CharFilter('last_name', lookup_expr='icontains')
    distance = filters.NumberFilter(method='distance_filter')

    def distance_filter(self, queryset, name, value):
        current_user = self.request.user
        excluded_users: list[int] = []
        for user in queryset:
            distance = get_user_distance(current_user, user)
            if distance >= value:
                excluded_users.append(user.id)
        return queryset.exclude(id__in=excluded_users)
