from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from accounts.models import Address
from .models import Cart, CartItem
from profile_app.models import Order
@method_decorator(login_required,name='dispatch')
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

    def post(self, request, *args, **kwargs):
        cart_item_id = request.POST.get('cart_item_id')
        cart_item = get_object_or_404(CartItem, id=cart_item_id)
        cart_item.delete()
        return redirect('cart')

@method_decorator(login_required,name="dispatch")
class ShoppingView(View):
    def get(self, request, *args, **kwargs):
        carts = Cart.objects.all()
        user_carts = CartItem.objects.filter(cart__user=request.user)
        total_amount =  "{:,}".format(sum(item.get_total_price() for item in user_carts))
        address = Address.objects.get(user=request.user)
        context = {
            'carts': carts,
            'user_carts': user_carts,
            'total_amount': total_amount,
            'address': address,
        }
        return render(request, 'cart/shopping.html', context)

@method_decorator(login_required,name="dispatch")
class ShoppingPaymentView(View):
    def get(self, request, *args, **kwargs):
        carts = Cart.objects.all()
        user_carts = CartItem.objects.filter(cart__user=request.user)
        total_amount =  "{:,}".format(sum(item.get_total_price() for item in user_carts))
        address = Address.objects.get(user=request.user)
        context = {
            'carts': carts,
            'user_carts': user_carts,
            'total_amount': total_amount,
            'address': address,
        }
        return render(request, 'cart/shopping-payment.html', context)

@method_decorator(login_required,name="dispatch")
class PaymentSuccessView(View):
    def get(self, request, *args, **kwargs):
        carts = Cart.objects.all()
        user_carts = CartItem.objects.filter(cart__user=request.user)
        total_amount =  "{:,}".format(sum(item.get_total_price() for item in user_carts))
        address = Address.objects.get(user=request.user)
        # order = Order.objects.get(user=request.user)
        context = {
            'carts': carts,
            'user_carts': user_carts,
            'total_amount': total_amount,
            'address': address,
        }
        return render(request, 'cart/shopping-complete-buy.html', context)


@method_decorator(login_required,name="dispatch")
class PaymentFailedView(View):
    def get(self, request, *args, **kwargs):
        carts = Cart.objects.all()
        user_carts = CartItem.objects.filter(cart__user=request.user)
        total_amount =  "{:,}".format(sum(item.get_total_price() for item in user_carts))
        address = Address.objects.get(user=request.user)
        context = {
            'carts': carts,
            'user_carts': user_carts,
            'total_amount': total_amount,
            'address': address,
        }
        return render(request, 'cart/shopping-no-complete-buy.html', context)

@method_decorator(login_required,name="dispatch")
class BankView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cart/bank.html')

    def post(self, request, *args, **kwargs):
        user_carts = CartItem.objects.filter(cart__user=request.user)

        # Get the user's address (assuming you have the 'Address' object)
        try:
            address = Address.objects.get(user=request.user)
        except Address.DoesNotExist:
            # Handle the case where the address does not exist
            address = None

        # Create an order for the user
        order = Order.objects.create(address=address)

        for item in user_carts:
            order.product.add(item.product)  # Use .add() to add products to the order

        # Remove all items from the user's cart
        # user_carts.delete()

        # Redirect to a success page or perform any other necessary actions
        return redirect('payment-success')
