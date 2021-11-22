from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rest_framework.authtoken.models import Token
from .models import Pin,User


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name')

    fieldsets = (
        ('General Info', {'fields': ('username', 'password'), }),
        ('Personal info', {'fields': ('first_name', 'email','followers')}),

        (None, {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'), }),
        (None, {'fields': ('last_login', 'date_joined')}),
    )


# Register your models here.
admin.site.register(User,CustomUserAdmin)

# admin.site.register(User)

admin.site.register(Pin)
