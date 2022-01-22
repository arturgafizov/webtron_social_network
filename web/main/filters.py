from django_filters import rest_framework as filters

from django.contrib.auth import get_user_model

User = get_user_model()


class CharFilter(filters.BaseInFilter, filters.CharFilter, filters.NumberFilter):
    pass


class ListUserFilter(filters.FilterSet):
    gender = filters.ChoiceFilter(choices=User.GenderChoice.choices)
    first_name = filters.CharFilter('first_name', lookup_expr='icontains')
    last_name = filters.CharFilter('last_name', lookup_expr='icontains')
