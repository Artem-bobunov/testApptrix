import base64
import random
from django.contrib import messages
from geopy.distance import geodesic
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserRegistrationForm,UserRegisterFields
from .models import ImageUsers,LikeUsers,Location
from .filters import FilterUser
from . location import location_data
from django.core.exceptions import ObjectDoesNotExist
from itertools import zip_longest


PATH_TO_IMAGE = r'C:\Users\btema\PycharmProjects\TestAppTrix\test_set\media\pupsen.jpg'

# Create your views here.
def notifications(request):
    obj = 0
    if request.user.is_authenticated:
        obj = LikeUsers.objects.filter(id_user_2__icontains=request.user.id, is_mutual=False).count()
    return obj

def list_user(request):
    # users = ImageUsers.objects.exclude(user__username__exact=request.user.username)
    users = ImageUsers.objects.exclude(user__is_superuser=True).order_by('-pk')
    myFilter = FilterUser(request.GET, queryset=users)
    objects = myFilter.qs
    obj = {}
    distances = []
    location = None

    if request.user.is_authenticated:
        try:
            location = Location.objects.get(user=request.user)
        except ObjectDoesNotExist:
            location = None
    else:
        pass

    for user in objects:
        try:
            user_location = Location.objects.get(user=user.user)
            if location is not None:
                distance = geodesic((location.latitude, location.longitude),
                                    (user_location.latitude, user_location.longitude)).kilometers
                distances.append(distance)
        except ObjectDoesNotExist:
            distances.append(None)

    zipped_data = zip_longest(objects, distances)

    return render(request, 'list.html', {'zipped_data': zipped_data, 'obj': notifications(request), 'myFilter': myFilter})

def list_likes(request, id):
    obj = LikeUsers.objects.filter(id_user_2__icontains=id, is_mutual__icontains=False)
    # location = Location.objects.get(user=request.user)

    return render(request, 'likes.html', {'obj': obj})


def likes_is_mutual(request, id, nameuser1):
    print(id)
    print(nameuser1)
    print(request.user.id)
    try:
        like = LikeUsers.objects.get(id_user_1=id,id_user_2=request.user.id,nameuser1__icontains=nameuser1,is_mutual=False)
        like.is_mutual = True
        print('ВЗАИМНЫЙ ЛАЙК')

        # # Отправка письма клиенту
        # subject = 'Вас оценили взаимно'
        # message = f'Вы понравились {nameuser1}! Почта участника: {request.user.email}'
        # from_email = request.user.email
        # recipient_list = [request.user.email]
        # send_mail(subject, message, from_email, recipient_list)
        #
        # # Отправка писем на почты участников
        # subject = 'Вам понравился пользователь'
        # message = f'Вы понравились {nameuser1}! Почта участника: {request.user.email}'
        # from_email = request.user.email
        # recipient_list = [like.id_user_1.email]  # Список почт участников, которым нужно отправить письма
        # send_mail(subject, message, from_email, recipient_list)

        like.save()
    except LikeUsers.DoesNotExist:
        print('Запись не найдена')
    return redirect('/')

def like_for_users(request, id):
    print('Поставил Лайк')
    like = LikeUsers(
        id_user_1=request.user,
        nameuser1=request.user.username,
        id_user_2=id,
        image_us=ImageUsers.objects.get(user=request.user)
    )
    like.save()
    return redirect('/')

def detail_user(request,id):
    user = ImageUsers.objects.get(pk=id)
    image = base64.b64encode(user.image).decode()
    return render(request, 'detail.html', {'us': user, 'image': image})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        user_field = UserRegisterFields(request.POST)
        if user_form.is_valid() and user_field.is_valid():
            try:
                new_user = user_form.save(commit=False)
                new_user.set_password(user_form.cleaned_data['password'])
                new_field = user_field.save(commit=False)
                new_field.user = new_user

                with open(PATH_TO_IMAGE, 'rb') as image_file:
                    new_field.image = image_file.read()
                print('СОХРАНИЛ БИНАРНИК')

                random_city = random.choice(list(location_data.keys()))
                coordinates = location_data[random_city]
                geo_ct = Location(user=new_user, street=random_city,
                                  longitude=coordinates['долгота'],
                                  latitude=coordinates['широта'])
                new_user.save()
                geo_ct.save()
                new_field.save()
                return redirect('login')
            except Exception as e:
                print(f'Не доглядел, ошибка: {e}')
    else:
        user_form = UserRegistrationForm()
        user_field = UserRegisterFields()

    return render(request, 'registration/register.html', {'user_form': user_form, 'user_field': user_field})



