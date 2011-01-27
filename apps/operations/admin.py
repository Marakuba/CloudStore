# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *

   
class EntryInline(admin.TabularInline):
    raw_id_fields = ('service',)
    readonly_fields = ('unitmeas',)
    fields = ('service','count','cost')
    model = Entry
    extra = 0

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('pk','create','organization','stock','invoicetype')
    list_display_links = ('pk','create')
    search_fields = ['pk','organization']
    date_hierarchy = 'create'
    inlines = [EntryInline]
    list_filter = ('stock','invoicetype')

admin.site.register(Invoice,InvoiceAdmin)
