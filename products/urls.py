from django.urls import path
from .views import home,single_product

urlpatterns = [
    path('', home,name='home'),
    path('product', single_product.as_view(),name='single_product'),
    # path('<slug:category>/<slug:slug>', home,name='single_product'),
]