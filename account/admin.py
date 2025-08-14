from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'user_type', 'is_staff')
    list_filter = ('user_type', 'is_staff', 'is_superuser')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('user_type', 'profile_picture', 'address_line1', 'city', 'state', 'pincode')
        }),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('user_type', 'first_name', 'last_name', 'email', 'profile_picture', 
                      'address_line1', 'city', 'state', 'pincode')
        }),
    )

admin.site.register(User, CustomUserAdmin)
