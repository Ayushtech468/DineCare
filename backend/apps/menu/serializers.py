from apps.menu.models import MenuItem, Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['uid','name', 'description', 'display_order', 'is_active']


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            'uid', 'category', 'name',
            'description', 'price', 'image',
            'is_available', 'is_vegetarian', 'preparation_time'
        ]
