# coding:utf-8
from .models import Question
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from wxpy import *
import time


def question(request):
    try:
        bot = Bot(cache_path=True,qr_path="../static/img/qr.png")
    except Exception,e:
        print e

    time.sleep(3)

    questions = Question.objects.all()
    context = {}
    context['questions'] = questions
    return render_to_response('question.html',context)

@bot.register()
def auto_reply(msg):
    questions = Question.objects.all()
    for question in questions:
        if isinstance(msg.chat, Friend) & question.content==msg.text:
            return ' {} '.format(msg.text)
