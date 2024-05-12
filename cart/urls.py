from django.urls import path,re_path
from . import views

urlpatterns = [
    path('cart/',views.cartView.as_view() ,name='cart'),
]