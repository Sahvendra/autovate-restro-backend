from django.contrib import admin
from django.utils.html import format_html
from .models import Category, MenuListItem,Orders
import json


#  Django Admin Registration
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "likes", "rating", "views", "price")

@admin.register(MenuListItem)
class MenuListItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "likes", "views", "rating")



@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'dish', 'quantity', 'total_amount', 'status', 'payment_status', 'table_number', 'ordered_at']
    list_filter = ['status', 'payment_status', 'ordered_at']
    search_fields = ['user_name', 'dish', 'delivery_address']
    ordering = ['-ordered_at']