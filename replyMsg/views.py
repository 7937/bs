# coding:utf-8
from .models import Question
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from wxpy import *
import time


def question(request):
    bot = Bot(cache_path=True,qr_path=/static/qr.png)
    time.sleep(3)
    
    questions = Question.objects.all()
    context = {}
    context['questions'] = questions
    return render_to_response('question.html',context)
