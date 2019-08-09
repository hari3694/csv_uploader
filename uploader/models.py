from django.db import models

# Create your models here.

class ProductDetails(models.Model):
    inventory_key = models.IntegerField(null=True, blank=True)
    catalog_no = models.CharField(max_length=100, null=True, blank=True)
    catalog_color = models.CharField(max_length=100, null=True, blank=True)
    size = models.CharField(max_length=10, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    catalog_price = models.FloatField(null=True, blank=True)
    is_on_sale = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Product Details"
        verbose_name_plural = "Product Details"
