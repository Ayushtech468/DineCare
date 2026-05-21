from django.contrib import admin
from apps.user.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('uid', 'email', 'phone_number', 'role', 'is_staff', 'is_active')
    search_fields = ('email', 'phone_number', 'full_name')
    list_filter = ('role', 'is_staff', 'is_active')
    ordering = ('uid',)
