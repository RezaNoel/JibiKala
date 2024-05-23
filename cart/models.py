# models.py
from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_price(self):
        return "{:,}".format(self.price*self.quantity)
    def get_total_price(self):
        return int(self.price *self.quantity)

    def save(self, *args, **kwargs):
        self.price = self.product.price
        super(CartItem, self).save(*args, **kwargs)
    def __str__(self):
        return self.product.model +" -> "+ "Q:" + str(self.quantity) +" -> " + self.cart.user.username
