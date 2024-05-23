from django.contrib import admin
from .models import Product,ProductAttribute,ProductBrand,ProductColor,ProductOption,ProductStorage,ProductComment,ProductImage
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    filter_horizontal = ['colors']

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductStorage)
admin.site.register(ProductOption)
admin.site.register(ProductColor)
admin.site.register(ProductBrand)
admin.site.register(ProductAttribute)
admin.site.register(ProductImage)
admin.site.register(ProductComment)