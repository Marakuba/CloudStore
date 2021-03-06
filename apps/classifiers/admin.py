# -*- coding: utf-8 -*-

from django.contrib import admin
#from mptt.admin import MPTTModelAdmin
from feincms.admin import editor
from models import *

class UnitmeasAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

class ServiceGeneralGroupAdmin(editor.TreeEditor):
    search_fields = ['name',]

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','unitmeas','servicegeneralgroup')
    list_display_links = ('name',)
    search_fields = ['name',]
    raw_id_fields = ('servicegeneralgroup',)

class StockAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ['name',]

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ['name',]
    
admin.site.register(ServiceGeneralGroup,ServiceGeneralGroupAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Stock,StockAdmin)
admin.site.register(Organization,OrganizationAdmin)
admin.site.register(Unitmeas,UnitmeasAdmin)
