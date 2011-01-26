# -*- coding: utf-8 -*-

from django.db import models
from mptt.models import MPTTModel
import mptt

class ServiceGeneralGroup(MPTTModel):
    name =  models.CharField(u'наименование', max_length=512,unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = u'группа товаров и услуг'
        verbose_name_plural = u'группы товаров и услуг'
        ordering = ('name',)

    def __unicode__(self):
        return '%s'  %(self.name)
    
mptt.register(ServiceGeneralGroup)

class Unitmeas(models.Model):
    name =  models.CharField(u'Наименование', max_length=500, unique=True)
    
    class Meta:
        verbose_name = u'единицы измерения'
        verbose_name_plural = u'единицы измерения'
        ordering = ('name',)

    def __unicode__(self):
        return '%s'  %(self.name)   
        
class Service(models.Model):
    name =  models.CharField(u'наименование', max_length=512,unique=True)
    servicegeneralgroup = models.ForeignKey(ServiceGeneralGroup
        ,related_name='services', verbose_name=u'общ. группа',null=True)
    unitmeas = models.ForeignKey(Unitmeas,verbose_name=u'удиницы измерения',null=True)

    class Meta:
        verbose_name = u'товар и услуга'
        verbose_name_plural = u'товары и услугаи'
        ordering = ('name',)

    def __unicode__(self):
        return '%s '  %(self.name)

class Stock(models.Model):
    name =  models.CharField(u'наименование', max_length=256,unique=True)

    class Meta:
        verbose_name = u'склад'
        verbose_name_plural = u'склады'
        ordering = ('name',)

    def __unicode__(self):
        return '%s'  %(self.name)

class Organization(models.Model):
    name =  models.CharField(u'наименование', max_length=512,unique=True)

    class Meta:
        verbose_name = u'организация'
        verbose_name_plural = u'организации'
        ordering = ('name',)

    def __unicode__(self):
        return '%s'  %(self.name)


