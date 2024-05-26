from django.urls import path,re_path
from . import views

urlpatterns = [
    path('cart/',views.CartView.as_view() ,name='cart'),
    path('cart/shopping/',views.ShoppingView.as_view() ,name='shopping'),
    path('cart/shopping/payment',views.ShoppingPaymentView.as_view() ,name='payment'),
    path('cart/shopping/payment/complete',views.PaymentSuccessView.as_view() ,name='payment-success'),
    path('cart/shopping/payment/failed',views.PaymentFailedView.as_view() ,name='payment-failed'),
    path('cart/bank',views.BankView.as_view() ,name='bank'),
]