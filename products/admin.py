from django.contrib import admin
from .models import phoneProducts,productAttributs,productBrands,productColors,productOptions,productStorages
# Register your models here.
admin.site.register(phoneProducts)
admin.site.register(productStorages)
admin.site.register(productOptions)
admin.site.register(productColors)
admin.site.register(productBrands)
admin.site.register(productAttributs)