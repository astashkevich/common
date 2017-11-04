# -*-coding: utf-8 -*-
import datetime

from django.db import models


class BaseContact(models.Model):

    name = models.CharField(u'Имя', max_length=250)
    email = models.EmailField('Email', max_length=50)
    phone = models.CharField(u'Телефон', max_length=15)
    date = models.DateTimeField(u'Дата', default=datetime.datetime.now)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Базовая форма регистрации"

    def __unicode__(self):
        return self.name