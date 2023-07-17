from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ImageUsers(models.Model):
    """
    Имя (first_name), фамилия (last_name) и почта уже есть в модели User
    """
    choices_pol = (
        ('мужской','мужской'),
        ('женский','женский'),
    )
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    pol = models.CharField('Пол',null=True,blank=True, max_length=10, choices=choices_pol,default='мужской')
    image = models.BinaryField('Аватарка пользователя', null=True,blank=True)

class LikeUsers(models.Model):
    id_user_1 = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nameuser1 = models.CharField('Пользователь который оценил', null=True, blank=True, max_length=255)
    id_user_2 = models.IntegerField('Айди пользователя которого оценили', null=True, blank=True)
    image_us = models.ForeignKey(ImageUsers, on_delete=models.CASCADE, null=True)#default=1
    is_mutual = models.BooleanField('Оценили пользователя2', null=True, blank=True, default=False)


class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    street = models.CharField('Улица', max_length=255,null=True,blank=True)
    longitude = models.DecimalField('Долгота', max_digits=9, decimal_places=6)
    latitude = models.DecimalField('Широта', max_digits=9, decimal_places=6)

