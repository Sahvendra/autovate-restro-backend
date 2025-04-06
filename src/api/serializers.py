from rest_framework import serializers
from .models import MenuListItem, Category,Orders

class MemuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuListItem
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# class OrdersSerializer(serializers.ModelSerializer):
#     class Meta:

#         model= Orders
#         fields='__all__'




#         from rest_framework import serializers
# from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
     
        model= Orders
        fields='__all__'