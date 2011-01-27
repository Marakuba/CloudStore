# -*- coding: utf-8 -*-

from django.contrib import admin
from models import *

class CurrencyAdmin(admin.ModelAdmin):
    pass

class CurrRateAdmin(admin.ModelAdmin):
    list_display = ('create','rete','currency')
    list_display_links = ('create',)
    date_hierarchy = 'create'
    list_filter = ('currency',)

class PriceTypeAdmin(admin.ModelAdmin):
    list_display = ('name','slug','currency')
    list_display_links = ('name',)

class PriceReteAdmin(admin.ModelAdmin):
    list_display = ('create','service','price','pricetype')
    list_display_links = ('create',)
    date_hierarchy = 'create'    
    list_filter = ('pricetype',)

class ConvfactorReteAdmin(admin.ModelAdmin):
    list_display = ('create','service','convfactor')
    list_display_links = ('create',)
    date_hierarchy = 'create'        

admin.site.register(Currency,CurrencyAdmin)
admin.site.register(CurrRate,CurrRateAdmin)
admin.site.register(PriceType,PriceTypeAdmin)
admin.site.register(PriceRete,PriceReteAdmin)
admin.site.register(ConvfactorRete,ConvfactorReteAdmin)

