from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'products/index.html')
def single_product(request):
    return render(request, 'products/single-product.html')