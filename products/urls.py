from django.urls import path
from django.views.generic.base import RedirectView
from .views import home,single_product

urlpatterns = [
    # path('', home,name='home'),
    
    path('product', single_product.as_view(template_name='products/single-product.html'),name='single_product'),
    path('', single_product.as_view(template_name='products/index.html'),name='home'),
    # path('<slug:category>/<slug:slug>', home,name='single_product'),
]