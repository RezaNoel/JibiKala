from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from cart.models import Cart, CartItem
from .models import Product,ProductComment,ProductAttribute
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CommentForm

# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'products/index.html',{'products':products})

class single_product(View):
    def get(self, request, category=None, slug=None):
        form = CommentForm()
        if not category:
            product = get_object_or_404(Product, slug=slug)
            colors = product.colors.all()
            comments = ProductComment.objects.filter(product=product)
            attributes = ProductAttribute.objects.filter(product=product)
            context = {
                'product': product,
                'colors': colors,
                'comments': comments,
                'attributes': attributes,
                'slug': slug,
                'form': form,
            }
            return render(request, 'products/single-product.html', context)
        product = get_object_or_404(Product, slug=slug)
        colors = product.colors.all()
        comments = ProductComment.objects.filter(product=product)
        attributes = ProductAttribute.objects.filter(product=product)
        context = {
            'product': product,
            'colors': colors,
            'comments': comments,
            'attributes': attributes,
            'category': category,
            'slug': slug,
            'form': form,
        }
        return render(request, 'products/single-product.html', context)

    @method_decorator(login_required)
    def post(self, request,slug):
        product = get_object_or_404(Product, slug=slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.text = form.cleaned_data['text']
            comment.user = request.user
            comment.product_id = product.id
            comment.save()
            return redirect('single_product', slug=slug)

        quantity = 1
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product,quantity=1)
        # if not created:
        #     cart_item.quantity += quantity
        # else:
        #     cart_item.quantity = quantity
        cart_item.save()

        return redirect('cart')
