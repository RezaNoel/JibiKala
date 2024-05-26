from django.urls import path,re_path
from .views import home,single_product,SearchResultsView,CategoryView,BrandView

urlpatterns = [
    path('', home,name='home'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('category/<str:category>', CategoryView.as_view(), name='category'),
    path('brand/<str:brand>', BrandView.as_view(), name='brand'),
    path('<slug:slug>/', single_product.as_view(),name='single_product'),
    # path('<str:category>/<slug:slug>/', single_product.as_view(),name='single_product'),

    # re_path(r'^(?P<category>[\w-]*)/(?P<slug:slug>[\w-]+)/$', single_product.as_view(),name='single_product'),
    # re_path(r'(?P<slug>[\w-]+)/$', single_product.as_view(),name='single_product'),

]