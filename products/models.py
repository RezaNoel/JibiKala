from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.
class ProductBrand(models.Model):
    name = models.CharField(max_length=100)
    faname = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class ProductColor(models.Model):
    name = models.CharField(max_length=50)
    faname = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductStorage(models.Model):
    value = models.IntegerField(default=128)

    def __str__(self):
        return str(self.value)


class Product(models.Model):
    product_types = (
        ('S', 'Smart Phone'),
        ('T', 'Tablet'),
        ('L', 'Laptop'),
        ('P', 'PC'),
    )
    product_parts = (
        ('M','Monitor'),
        ('K','Keyboard'),
        ('MS','Mouse'),
    )
    type = models.CharField(max_length=5,choices=product_types)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    brand = models.ForeignKey(ProductBrand,on_delete=models.CASCADE)
    colors = models.ManyToManyField(ProductColor)
    storage = models.ForeignKey(ProductStorage, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True,blank=True)
    description = models.TextField(blank=True)
    part = models.CharField(max_length=5,choices=product_parts,blank=True)

    def get_comments_count(self):
        return self.comments.count()

    def get_price(self):
        return "{:,}".format(self.price)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.model)
        super(Product, self).save(*args, **kwargs)
    def __str__(self):
        return self.model


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.model}"


class ProductOption(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class ProductAttribute(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    options = models.ForeignKey(ProductOption, on_delete=models.CASCADE)
    value = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.product} {self.options} {self.value}"


class ProductComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
