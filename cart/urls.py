from django.urls import path,re_path
from . import views

urlpatterns = [
    path('cart/',views.CartView.as_view() ,name='cart'),
]