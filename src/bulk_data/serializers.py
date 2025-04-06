
from rest_framework import serializers
from .models import Category, MenuListItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"  # Includes all fields of the Category model

class MenuListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuListItem
        fields = '__all__'






