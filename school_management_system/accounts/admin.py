from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# CustomUser Admin Configuration
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

    list_display = ('username', 'email', 'role', 'is_staff') #

    list_filter = UserAdmin.list_filter + ('role',) # Adding role to filter options

    search_fields = UserAdmin.search_fields + ('role',) # Adding role to search fields

    ordering = UserAdmin.ordering # Ordering by username

# Registering CustomUser model with CustomUserAdmin configuration
admin.site.register(CustomUser, CustomUserAdmin) 
