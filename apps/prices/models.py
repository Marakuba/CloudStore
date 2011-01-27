# -*- coding: utf-8 -*-

import datetime
from django.db import models
from classifiers.models import Service

class Currency(models.Model):    
    name = models.CharField(u'наименование', max_length=30)
   
    def __unicode__(self):
        return u"%s" % self.name
    
    class Meta:
        verbose_name = u"валюта"
        verbose_name_plural = u"валюты"

class CurrRate(models.Model):    
    create = models.DateTimeField(u'создано', default=datetime.datetime.now())
    rete = models.DecimalField(u'курс', max_digits=10, decimal_places=2,null=True)    
    currency = models.ForeignKey(Currency,verbose_name=u'валюта')

    def __unicode__(self):
        return u"%s %s %s" % (self.create, self.rete, self.currency)
    
    class Meta:
        verbose_name = u"курс валюты"
        verbose_name_plural = u"курсы валют"
        get_latest_by = "create"
            
class PriceType(models.Model):
    name = models.CharField(u'наименование', max_length=50)
    slug = models.SlugField(u'sku', default=u'')
    currency = models.ForeignKey(Currency,verbose_name=u'валюта')
    
    def __unicode__(self):
        return u"%s" % self.name
    
    class Meta:
        verbose_name = u"тип цены"
        verbose_name_plural = u"типы цены"
            
class PriceRete(models.Model):
    create = models.DateTimeField(u'создано', default=datetime.datetime.now())
    service = models.ForeignKey(Service,verbose_name=u'товар')
    price = models.DecimalField(u'цена', max_digits=10, decimal_places=2,null=True)
    pricetype = models.ForeignKey(PriceType, verbose_name=u'Тип цены')

    def __unicode__(self):
        return u"%s %s %s %s" % (self.create, self.service, self.price, self.pricetype )
    
    class Meta:
        verbose_name = u"курс цены"
        verbose_name_plural = u"курсы цен"
        get_latest_by = "create"
            
class ConvfactorRete(models.Model):
    create = models.DateTimeField(u'создано', default=datetime.datetime.now())
    service = models.ForeignKey(Service,verbose_name=u'товар')
    convfactor = models.DecimalField(u'значение', max_digits=10, decimal_places=2,null=True)
    
    def __unicode__(self):
        return u"%s %s %s" % (self.create, self.service,self.convfactor)
    
    class Meta:
        verbose_name = u'курс скидки/наценки'
        verbose_name_plural = u'курсы скидок/наценок'

