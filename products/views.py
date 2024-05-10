from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View

# Create your views here.

def home(request):
    return render(request, 'products/index.html')
class single_product(View):
    def get(self,request,category=None,slug=None):
        if not category:
            return render(request, 'products/single-product.html', {'slug': slug})

        return render(request, 'products/single-product.html', {'category': category, 'slug': slug})

