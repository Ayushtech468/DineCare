from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.user.models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('uid', 'email', 'phone_number', 'role', 'is_staff', 'is_active')
    search_fields = ('email', 'phone_number', 'full_name')
    list_filter = ('role', 'is_staff', 'is_active')
    ordering = ('uid',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {
            'fields': ('full_name', 'phone_number', 'role')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'is_staff',
                'is_active',
            ),
        }),
    )
