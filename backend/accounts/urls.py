from django.urls import path
from .views import *


urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:pk>/', update_user, name='update_user'),
]