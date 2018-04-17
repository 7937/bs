# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Question(models.Model):
    content = models.CharField(max_length=200)
    answer = models.CharField(max_length=200,default='0')

class AutoReply(models.Model):
    auto = models.ChoiceField(choices=(0,1),initial='0',help_text='是否自动回复，0为否，1为是，默认为否')