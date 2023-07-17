from urllib import request
import django_filters
from django.core.exceptions import ObjectDoesNotExist
from django.forms import Select, TextInput
from django_filters import ChoiceFilter, CharFilter
from django import forms
from geopy.distance import geodesic
from .models import *

class FilterUser(django_filters.FilterSet):
    pol = ChoiceFilter(widget=Select(attrs={'class': 'form-control'}), choices=ImageUsers.choices_pol, label="Пол")
    last_name = CharFilter(field_name='user__last_name', widget=TextInput(attrs={'class': 'form-control'}), label="Фамилия")
    first_name = CharFilter(field_name='user__first_name', widget=TextInput(attrs={'class': 'form-control'}), label="Имя")
    # distance = CharFilter(method='filter_distance',widget=TextInput(attrs={'class': 'form-control'}), label="Дистанция")

    class Meta:
        model = ImageUsers
        fields = ['pol', 'last_name', 'first_name']#distance

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request', None)
    #     super(FilterUser, self).__init__(*args, **kwargs)

    # def filter_distance(self, queryset, name, value):
    #     if not value:
    #         return queryset
    #
    #     location1 = Location.objects.get(user=self.request.user)
    #     filtered_ids = []
    #     for obj in queryset:
    #         user_location = Location.objects.get(user=obj.user)
    #         if user_location:
    #             distance = geodesic(
    #                 (location1.latitude, location1.longitude),
    #                 (user_location.latitude, user_location.longitude)
    #             ).kilometers
    #             if distance <= float(value):
    #                 filtered_ids.append(obj.user.id)
    #     return queryset.filter(user__id__in=filtered_ids)







