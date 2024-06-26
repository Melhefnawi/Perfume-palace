from django.contrib import admin

from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):

    list_display = ('brand', 'form', 'name', 'category',
                    'price', 'rating', 'image','reviews_count',)
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
