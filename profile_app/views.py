from django.shortcuts import render
from django.views import View

# Create your views here.
class profileView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'profile_app/profile.html')