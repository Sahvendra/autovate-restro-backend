from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MenuListItem ,Category
from .serializers import MenuListItemSerializer ,CategorySerializer

class MenuListView(APIView):
    def get(self, request):
        menu_items = MenuListItem.objects.all()
        serializer = MenuListItemSerializer(menu_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Ensure the request contains a list
        if not isinstance(request.data, list):
            return Response({"error": "Expected a list of menu items"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = MenuListItemSerializer(data=request.data, many=True)  # Accepting a list
        if serializer.is_valid():
            serializer.save()  # Save all valid objects
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Ensure the request contains a list
        if not isinstance(request.data, list):
            return Response({"error": "Expected a list of categories"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CategorySerializer(data=request.data, many=True)  # Accepting a list of categories
        if serializer.is_valid():
            serializer.save()  # Save all valid objects
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)