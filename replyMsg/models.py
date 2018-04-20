# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Question(models.Model):
    content = models.CharField(max_length=200)
    answer = models.CharField(max_length=200,default='0')

class AutoReply(models.Model):
    auto = models.BooleanField()

class Timer(models.Model):
    receiver = models.CharField(max_length=200)
    time = models.DateTimeField()
    recycle = models.IntegerField(default = 0)
    content = models.CharField(max_length=200)
