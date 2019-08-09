from django.contrib import admin
from uploader.models import ProductDetails
# Register your models here.


class ProductDetailsAdmin(admin.ModelAdmin):
    fields = ('inventory_key', 'catalog_no', 'catalog_color', 'size', 'quantity', 'catalog_price', 'is_on_sale')
    list_display = ('inventory_key', 'catalog_no')
    search_fields = ('inventory_key', 'catalog_no')

admin.site.register(ProductDetails, ProductDetailsAdmin)