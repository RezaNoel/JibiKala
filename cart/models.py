from django.db import models

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    session = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_and_add_time=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_and_add_time=True)
    updated_at = models.DateTimeField(auto_now=True)
