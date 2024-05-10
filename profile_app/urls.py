from django.urls import path,re_path
from . import views

urlpatterns = [
    path('profile/',views.profileView.as_view() ,name='profile'),
]