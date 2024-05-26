from django.urls import path,re_path
from . import views

urlpatterns = [
    path('profile/',views.profileView.as_view() ,name='profile'),
    path('profile/edit',views.profileEditView.as_view() ,name='profile-edit'),
    path('profile/edit/address',views.addressEditView.as_view() ,name='address-edit'),
]