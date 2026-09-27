from django.shortcuts import render
from .models import Category, MenuItem
from .serializers import CategorySerializer, MenuItemSerializer
from rest_framework import viewsets
from .permissions import MenuCategoryPermission


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True)
    permission_classes = [MenuCategoryPermission]


class MenuItemViewSet(viewsets.ModelViewSet):
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.filter(is_available=True)
    permission_classes = [MenuCategoryPermission]
