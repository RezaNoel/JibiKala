from django.shortcuts import render
from django.views import View
# Create your views here.

class cartView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'cart/cart.html')