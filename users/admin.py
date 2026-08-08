from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'username', 'phone', 'country', 'is_staff')
    search_fields = ('email', 'username')
    list_filter = ('is_staff', 'is_active', 'groups')

    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {
            'fields': ('avatar', 'phone', 'country'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Дополнительная информация', {
            'fields': ('avatar', 'phone', 'country'),
        }),
    )
