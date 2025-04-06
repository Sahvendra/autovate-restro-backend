from django.urls import path
from .views import MenuListView,CategoryView

urlpatterns = [
    path("categories/", CategoryView.as_view(), name="category-list"),
    path("menu-items/", MenuListView.as_view(), name="menu-list"),
]
