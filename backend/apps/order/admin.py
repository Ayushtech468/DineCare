from django.contrib import admin
from apps.order.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "uid", "customer", "status", "total_amount"
    )

    search_fields = (
        "uid", "customer", "status", "total_amount"
    )

    list_filter = (
        "uid", "customer", "status", "total_amount"
    )

    ordering = ["uid"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        "uid", "order", "menu_item", "quantity", "price"
    )

    search_fields = (
        "uid", "order", "menu_item", "quantity"
    )

    list_filter = (
        "uid", "order", "menu_item", "quantity", "price"
    )

    ordering = ["uid"]
