# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _

from forms import CustomUserChangeForm
from models import User as CustomUser

class CustomUserAdmin(UserAdmin):
    #...
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email','icq')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Groups'), {'fields': ('groups',)}),
    )
    #...
    form = CustomUserChangeForm
    #....
    list_display = ('username', 'last_name', 'first_name','email','icq',
                    'is_staff', 'is_active','is_superuser')
    #....

admin.site.unregister(User)    
admin.site.register(CustomUser,CustomUserAdmin)
