import random
import string
from django.db import models

class Order(models.Model):
    code = models.CharField(max_length=16, unique=True,blank=True)
    product = models.ManyToManyField('products.Product')
    address = models.ForeignKey('accounts.Address', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.code:
            # Generate a random 16-character code
            self.code = self._generate_random_code()
        super().save(*args, **kwargs)

    def _generate_random_code(self):
        # Generate a random string of 16 characters
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
