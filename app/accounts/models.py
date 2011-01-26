# -*- coding: utf-8 -*-
from django.contrib.auth.models import UserManager, User as BaseUser
from django.db import models

class User(BaseUser):
    icq = models.DecimalField(('ICQ'),max_digits=9, decimal_places=0,blank=True, null=True)
    objects = UserManager()

    class Meta:
        verbose_name = u'Пользыватель'
        verbose_name_plural = u'Пользыватели'
        ordering = ('first_name',)

    def __unicode__(self):
        return u'%s "%s"' % (self.first_name, self.last_name)
