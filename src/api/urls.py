from django.urls import path
from .views import CategoryListView, CategoryDetailView, MenuListView, MenuDetailView
from .views import OrderListCreateView, OrderRetrieveUpdateDestroyView
urlpatterns = [
    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    
    # Menu List Item URLs
    path('menu/', MenuListView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', MenuDetailView.as_view(), name='menu-detail'),


    path('orders/', OrderListCreateView.as_view(), name='orders-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='orders-detail'),
    # path('create-order/', create_order, name='create_order'),

]


