from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('<str:slug>/', post_detail, name='post_detail'),
]