from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
import json
from .models import Category, MenuListItem

@method_decorator(csrf_exempt, name='dispatch')
class CategoryListView(View):
    def get(self, request):
        categories = list(Category.objects.values())
        return JsonResponse({"categories": categories}, safe=False)
    
    def post(self, request):
        data = json.loads(request.body)
        category = Category.objects.create(**data)
        return JsonResponse({"message": "Category created", "id": category.id})

@method_decorator(csrf_exempt, name='dispatch')
class CategoryDetailView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        return JsonResponse({"category": model_to_dict(category)})
    
    def put(self, request, pk):
        data = json.loads(request.body)
        Category.objects.filter(pk=pk).update(**data)
        return JsonResponse({"message": "Category updated"})
    
    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return JsonResponse({"message": "Category deleted"})

@method_decorator(csrf_exempt, name='dispatch')
class MenuListView(View):
    def get(self, request):
        menu_items = list(MenuListItem.objects.values())
        return JsonResponse({"menu": menu_items}, safe=False)
    
    def post(self, request):
        data = json.loads(request.body)
        menu_item = MenuListItem.objects.create(**data)
        return JsonResponse({"message": "Menu item created", "id": menu_item.id})

@method_decorator(csrf_exempt, name='dispatch')
class MenuDetailView(View):
    def get(self, request, pk):
        menu_item = get_object_or_404(MenuListItem, pk=pk)
        return JsonResponse({"menu_item": model_to_dict(menu_item)})
    
    def put(self, request, pk):
        data = json.loads(request.body)
        MenuListItem.objects.filter(pk=pk).update(**data)
        return JsonResponse({"message": "Menu item updated"})
    
    def delete(self, request, pk):
        menu_item = get_object_or_404(MenuListItem, pk=pk)
        menu_item.delete()
        return JsonResponse({"message": "Menu item deleted"})
    


# from rest_framework import generics
# from .models import Orders
# from .serializers import OrdersSerializer

# # ✅ Create & List Orders
# class OrdersListCreateView(generics.ListCreateAPIView):
#     queryset = Orders.objects.all()
#     serializer_class = OrdersSerializer

# # ✅ Retrieve, Update, Delete a Single Order
# class OrdersDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Orders.objects.all()
#     serializer_class = OrdersSerializer
  


from rest_framework import generics, status
from rest_framework.response import Response
from .models import Orders
from .serializers import OrderSerializer
from rest_framework import status as drf_status

from django.http import JsonResponse
import json

# @csrf_exempt  # only if you're testing without CSRF token
# def create_order(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)

#             # Print or extract values from JSON
#             user_name = data.get('user_name')
#             dish = data.get('dish')
#             quantity = data.get('quantity')
#             table_number = data.get('table_number')
#             total_amount = data.get('total_amount')
#             delivery_address = data.get('delivery_address')
#             image = data.get('image')

#             print("User:", user_name)
#             print("Dish:", dish)
#             print("Quantity:", quantity)

#             # Save to DB if needed
#             order = Orders.objects.create(
#                 user_name=user_name,
#                 dish=dish,
#                 quantity=quantity,
#                 table_number=table_number,
#                 total_amount=total_amount,
#                 delivery_address=delivery_address,
#                 image=image
#             )

#             return JsonResponse({'message': 'Order created successfully'}, status=201)

#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON'}, status=400)

#     return JsonResponse({'error': 'Only POST method allowed'}, status=405)





class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        # Don't allow updating ordered_at timestamp
        if 'ordered_at' in serializer.validated_data:
            del serializer.validated_data['ordered_at']
        serializer.save()




