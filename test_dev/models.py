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
    image = models.ImageField('Аватарка пользователя', null=True,blank=True)


