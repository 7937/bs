# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Question
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id","content","answer")
    ordering = ("id",)
    
admin.site.register(Question,QuestionAdmin)


from .models import AutoReply
class AutoReplyAdmin(admin.ModelAdmin):
    list_display = ("auto",)

admin.site.register(AutoReply,AutoReplyAdmin)

from .models import Timer
class TimerAdmin(admin.ModelAdmin):
    list_display = ("id","receiver","time","content","recycle",)
    ordering = ("id",)    
    
admin.site.register(Timer,TimerAdmin)
