from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, MenuItemViewSet

router = DefaultRouter()

router.register('category', CategoryViewSet, basename='category')
router.register('menu_item', MenuItemViewSet, basename='menu_item')

urlpatterns = [
    path('', include(router.urls))
]
