from django.contrib import admin
from apps.menu.models import MenuItem, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'uid', 'name', 'description',
        'display_order', 'is_active'
    )

    search_fields = ('uid', 'name', 'description')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = (
        'uid', 'category', 'name',
        'description', 'price', 'preparation_time',
        'image', 'is_available', 'is_vegetarian',
        'preparation_time'
    )

    search_fields = ('uid', 'category__name', 'name', 'description', 'price')

    list_filter = ('uid', 'name', 'is_vegetarian', 'is_available')

    ordering = ('uid',)

