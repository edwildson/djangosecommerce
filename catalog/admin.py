from django.contrib import admin
# Register your models here.
from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'category', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)