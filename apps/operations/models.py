# -*- coding: utf-8 -*-
from django.db import models
from classifiers.models import Service,Stock,Organization

class InvoiceType(models.Model):
    name =  models.CharField(u'наименование', max_length=256,unique=True)

    class Meta:
        verbose_name = u'тип документа'
        verbose_name_plural = u'типы документоы'
        ordering = ('name',)

    def __unicode__(self):
        return '%s'  %(self.name)

class Invoice(models.Model):
    create = models.DateTimeField(u'дата, время', auto_now_add=True)
    organization = models.ForeignKey(Organization, verbose_name=u'организация')
    invoicetype = models.ForeignKey(InvoiceType, verbose_name=u'тип')

    class Meta:
        verbose_name = u'документ'
        verbose_name_plural = u'документы'
        ordering = ('create',)    

    def __unicode__(self):
        return '%s - %s'  %(self.create,self.pk)

class Entry(models.Model):
    invoice = models.ForeignKey(Invoice, verbose_name=u'документ')
    service = models.ForeignKey(Service, verbose_name=u'товар/услуга')
    stock = models.ForeignKey(Stock, verbose_name=u'склад')
    count = models.FloatField(u'кол-во')
    comment = models.TextField(u'коммент.', default='', blank=True)

    class Meta:
        verbose_name = u'проводка'
        verbose_name_plural = u'проводки'
        ordering = ('invoice',)    

    def __unicode__(self):
        return 'Entry: %s - %s'  %(self.invoice,self.pk)
