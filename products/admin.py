from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'frame', 
        'product_group',
        'name',
        'fork',
        'weight',
        'weight_alloy',
        'weight_carbon',
        'price',
        'price_alloy',
        'price_carbon',
    )

    ordering = ('product_group',)

# Register your models here.
admin.site.register(Product, ProductAdmin)
