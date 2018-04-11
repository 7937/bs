# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Question(models.Model):
    content = models.CharField(max_length=200)
    answer = models.CharField(max_length=200,default='0')
