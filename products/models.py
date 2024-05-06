from django.db import models

# Create your models here.
class productBrands(models.Model):
    name = models.CharField(max_length=100)
    faname = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class productColors(models.Model):
    name = models.CharField(max_length=50)
    faname = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class productStorages(models.Model):
    value = models.IntegerField(default=128)

    def __str__(self):
        return str(self.value)


class phoneProducts(models.Model):
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
    phone_model = models.CharField(max_length=100)
    price = models.IntegerField()
    brand = models.ForeignKey(productBrands,on_delete=models.CASCADE)
    color = models.ForeignKey(productColors, on_delete=models.CASCADE)
    storage = models.ForeignKey(productStorages, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    part = models.CharField(max_length=5,choices=product_parts,blank=True)

    def __str__(self):
        return self.phone_model

class productOptions(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class productAttributs(models.Model):
    product = models.ForeignKey(phoneProducts,on_delete=models.CASCADE)
    options = models.ForeignKey(productOptions, on_delete=models.CASCADE)
    value = models.CharField(max_length=250)

    def __str__(self):
        return self.product + ' ' + self.options + ' ' + self.value