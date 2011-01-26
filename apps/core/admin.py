# -*- coding: utf-8 -*-

from django.contrib import admin
#from mptt.admin import MPTTModelAdmin
from feincms.admin import editor
from models import *

class MKBAdmin(editor.TreeEditor):
    raw_id_fields = ('parent',)
    search_fields = ['code', 'name']

#class ICD10Admin(editor.TreeEditor):
#    pass

class RelformAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

class UnitmeasAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

class RoutadmAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    
admin.site.register(MKB,MKBAdmin)
#admin.site.register(ICD10,ICD10Admin)
admin.site.register(Relform,RelformAdmin)
admin.site.register(Routadm,RoutadmAdmin)
admin.site.register(Unitmeas,UnitmeasAdmin)
