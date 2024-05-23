from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .models import Cart, CartItem

@method_decorator(login_required, name='dispatch')
class CartView(View):
    def get(self, request, *args, **kwargs):
        carts = Cart.objects.all()
        user_carts = CartItem.objects.filter(cart__user=request.user)
        total_amount =  "{:,}".format(sum(item.get_total_price() for item in user_carts))

        context = {
            'carts': carts,
            'user_carts': user_carts,
            'total_amount': total_amount,
        }
        return render(request, 'cart/cart.html', context)
