from django.urls import path,re_path
from . import views

urlpatterns = [
    path('login/',views.loginView.as_view() ,name='login'),
    path('logout/',views.logoutView.as_view() ,name='logout'),
    path('register/',views.registerView.as_view() ,name='register'),
    path('password-change/',views.passwordChangeView.as_view() ,name='password_change'),
]