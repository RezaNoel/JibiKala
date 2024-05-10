from django.urls import path,re_path
from .views import home,single_product

urlpatterns = [
    path('', home,name='home'),
    
    re_path(r'^(?P<category>[\w-]*)/(?P<slug>[\w-]+)/$', single_product.as_view(),name='single_product'),
    re_path(r'(?P<slug>[\w-]+)/$', single_product.as_view(),name='single_product'),

]