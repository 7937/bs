# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-19 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('replyMsg', '0007_autoreply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=200)),
                ('time', models.DateTimeField(verbose_name='\u5b9a\u65f6\u65f6\u95f4')),
                ('recycle', models.IntegerField(default=0)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
    ]
