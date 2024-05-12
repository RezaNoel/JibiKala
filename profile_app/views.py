from django.shortcuts import render
from django.views import View

# Create your views here.
class profileView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'profile_app/profile.html')

def get_cart_from_session(request):
    cart_id = request.session.get('cart_id')
    if cart_id:
        try:
            cart = Cart.objects.get(pk=cart_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=request.user, session=request.session.session_key)
    else:
        cart = Cart.objects.create(user=request.user, session=request.session.session_key)
    request.session['cart_id'] = cart.pk
    return cart


