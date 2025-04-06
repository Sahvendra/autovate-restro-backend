from django.contrib import admin
from .models import Category, MenuListItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "likes", "rating", "views", "price")
    search_fields = ("name",)
    list_filter = ("rating", "views")
    ordering = ("-views",)  # Sort by most viewed
    readonly_fields = ("id",)  # ID should be read-only

@admin.register(MenuListItem)
class MenuListItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "likes", "views", "rating")
    search_fields = ("name", "category__name")  # Search by menu name and category
    list_filter = ("category", "rating", "views")
    ordering = ("-likes",)  # Sort by most liked items
    readonly_fields = ("id",)  # ID should be read-only
