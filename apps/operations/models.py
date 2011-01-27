# -*- coding: utf-8 -*-

import datetime
from django.db import models
from classifiers.models import Service,Stock,Organization

INVOICE_TYPES = (
    (u'p',u'приход'),
    (u'r',u'расход'),
    (u'z',u'завяка'),
)
class Invoice(models.Model):
    create = models.DateTimeField(u'дата, время', default=datetime.datetime.now())
    organization = models.ForeignKey(Organization, verbose_name=u'организация')
#    invoicetype = models.CharField(u'тип', max_length=1, choices=INVOICE_TYPES)
    comment = models.TextField(u'коммент.', default='', blank=True)

    class Meta:
        verbose_name = u'документ'
        verbose_name_plural = u'документы'
        ordering = ('create',)    

    def __unicode__(self):
        return u'N %s от %s'  %(self.pk,self.create)

class Entry(models.Model):
    invoice = models.ForeignKey(Invoice, verbose_name=u'документ')
    service = models.ForeignKey(Service, verbose_name=u'товар/услуга')
    stock = models.ForeignKey(Stock, verbose_name=u'склад')
    count = models.FloatField(u'кол-во')
    cost = models.DecimalField(u'цена', max_digits=10, decimal_places=2,null=True)

    class Meta:
        verbose_name = u'проводка'
        verbose_name_plural = u'проводки'
        ordering = ('invoice',)    

    def __unicode__(self):
        return u'Entry N : %s по док-у %s'  %(self.pk,self.invoice)
    
    def unitmeas(self):
        return self.service.unitmeas
    unitmeas.short_description = u'ед.изм.'
