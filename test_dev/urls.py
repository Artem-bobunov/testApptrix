from . import views
from django.urls import path

urlpatterns = [
    path('', views.list_user, name='list_user'),
    path('register/', views.register, name='register'),
    path('detail_user/<int:id>', views.detail_user, name='detail_user'),
    path('like_for_users/<int:id>', views.like_for_users, name='like_for_users'),
    path('list_likes/<int:id>', views.list_likes, name='list_likes'),
    path('likes_is_mutual/<int:id>/<str:nameuser1>/', views.likes_is_mutual, name='likes_is_mutual')
]
