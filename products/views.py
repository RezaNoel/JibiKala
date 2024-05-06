from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View

# Create your views here.

def home(request):
    return render(request, 'products/index.html')
class single_product(View):
    template_name=None
    def get(self,request):
        return render(request, self.template_name)
