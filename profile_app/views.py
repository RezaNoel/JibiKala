from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from accounts.models import User,Address
from cart.models import CartItem, Cart
from .forms import UserUpdateForm,AddressUpdateForm
# Create your views here.
class profileView(View):
    def get(self, request, *args, **kwargs):
        carts = CartItem.objects.filter(cart__user=request.user)
        return render(request,'profile_app/profile.html',{'carts':carts})
    def post(self, request, *args, **kwargs):
        cart_item_id = request.POST.get('cart_item_id')
        cart_item = get_object_or_404(CartItem, id=cart_item_id)
        cart_item.delete()
        return redirect('profile')

class profileEditView(View):
    def get(self, request, *args, **kwargs):
        form = UserUpdateForm(instance=request.user)
        return render(request,'profile_app/profile-edit.html',{'form': form})
    def post(self, request, *args, **kwargs):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return redirect('profile')

class addressEditView(View):
    def get(self, request, *args, **kwargs):
        form = AddressUpdateForm(instance=request.user)
        return render(request,'profile_app/address-edit.html',{'form': form})
    def post(self, request, *args, **kwargs):
        form = AddressUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            # form.user = request.user
            form.save()
            return redirect('profile')
        return redirect('profile')

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


