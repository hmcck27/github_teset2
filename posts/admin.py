from django.contrib import admin
from .models import Review

# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['title','content','item','is_purchasable']
    list_display_links = ['title','item']
    search_fields = ['item']
    list_filter = ['created_at','is_purchasable']
    pass


# Register your models here.
