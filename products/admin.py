from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'slug',
        'category',
        'price',
        'rating',
        'image',
        'created'
    )

    ordering = ('slug',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
