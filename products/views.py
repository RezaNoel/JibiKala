from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from cart.models import Cart, CartItem
from .models import Product,ProductComment,ProductAttribute,ProductBrand
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CommentForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def home(request):
    products = Product.objects.all()
    offers = Product.objects.order_by('price')[:5]
    return render(request, 'products/index.html',{'products':products,'offers':offers})


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
        color_id = request.POST.get('radio1')
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product,quantity=1,color_id=color_id)
        cart_item.save()

        return redirect('cart')


class SearchResultsView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if query:
            results_list = Product.objects.filter(
                Q(model__icontains=query) |
                Q(brand__name__icontains=query) |
                Q(type__icontains=query) |
                Q(storage__value__icontains=query)
            ).distinct()

            # صفحه‌بندی نتایج
            paginator = Paginator(results_list, 2)  # تعداد محصولات در هر صفحه

            page = request.GET.get('page')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # اگر شماره صفحه عددی نیست، نمایش صفحه اول
                results = paginator.page(1)
            except EmptyPage:
                # اگر شماره صفحه بیشتر از تعداد صفحات است، نمایش صفحه آخر
                results = paginator.page(paginator.num_pages)
        else:
            results = Product.objects.none()

        return render(request, 'products/search.html', {'results': results, 'query': query})

class CategoryView(View):
    def get(self, request,category):
        results_list = Product.objects.filter(type__icontains=category)
        match category:
            case 'S':
                category_name = 'گوشی'
            case 'L':
                category_name = 'لپتاپ'
            case 'T':
                category_name = 'تبلت'
            case 'P':
                category_name = 'کامپیوتر'
        # صفحه‌بندی نتایج
        paginator = Paginator(results_list, 2)  # تعداد محصولات در هر صفحه

        page = request.GET.get('page')
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            # اگر شماره صفحه عددی نیست، نمایش صفحه اول
            results = paginator.page(1)
        except EmptyPage:
            # اگر شماره صفحه بیشتر از تعداد صفحات است، نمایش صفحه آخر
            results = paginator.page(paginator.num_pages)


        return render(request, 'products/category.html', {'results': results,'category_name':category_name})

class BrandView(View):
    def get(self, request,brand):
        results_list = Product.objects.filter(brand__name__icontains=brand)
        brand_name = ProductBrand.objects.get(name=brand).faname
        # صفحه‌بندی نتایج
        paginator = Paginator(results_list, 2)  # تعداد محصولات در هر صفحه

        page = request.GET.get('page')
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            # اگر شماره صفحه عددی نیست، نمایش صفحه اول
            results = paginator.page(1)
        except EmptyPage:
            # اگر شماره صفحه بیشتر از تعداد صفحات است، نمایش صفحه آخر
            results = paginator.page(paginator.num_pages)


        return render(request, 'products/brand.html', {'results': results,'brand_name':brand_name})