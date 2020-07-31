from django.contrib import admin
from .models import Brand,Item

# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','is_partner']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['created_at','is_partner']
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','brand','is_soldout','original_price','sale_price']
    list_display_links = ['name']
    search_fields = ['name','brand']
    list_filter = ['created_at']
    pass