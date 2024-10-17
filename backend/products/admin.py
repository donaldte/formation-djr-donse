from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'description', 'created_at', 'updated_at']
    search_fields = ['name', 'price', 'description']
    list_filter = ['price', 'created_at', 'updated_at']
    list_per_page = 10
    
admin.site.register(Product, ProductAdmin)    