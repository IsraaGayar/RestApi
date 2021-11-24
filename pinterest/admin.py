from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rest_framework.authtoken.models import Token
from .models import Pin,User


class CustomUserAdmin(UserAdmin):
    readonly_fields = ['getPins','getfollowees']
    list_display = ('username', 'first_name', 'last_name','getPins')

    fieldsets = (
        ('General Info', {'fields': ('username', 'password') }),
        ('Personal info', {'fields': ('first_name', 'email','followers', 'getPins','getfollowees')}),

        (None, {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'), }),
        (None, {'fields': ('last_login', 'date_joined')}),
    )
    def getfollowees(self,obj):
        mypins=list(obj.followees.all())
        return mypins

    def getPins(self, obj):
        mypins = list(obj.pins.all())
        return mypins

class customPin(admin.ModelAdmin):

    list_display = ('title', 'owner')


# Register your models here.
admin.site.register(User,CustomUserAdmin)

# admin.site.register(User)

admin.site.register(Pin,customPin)
