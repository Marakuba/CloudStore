# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *

class InvoiceTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ['name',]
    
class EntryInline(admin.TabularInline):
    model = Entry
    extra = 0

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('pk','create','organization','invoicetype')
    list_display_links = ('pk','create')
    search_fields = ['pk','organization']
    list_filter = ('invoicetype',)
    date_hierarchy = 'create'
    inlines = [EntryInline]

    

admin.site.register(InvoiceType,InvoiceTypeAdmin)
admin.site.register(Invoice,InvoiceAdmin)
