# coding:utf-8
from .models import Question,AutoReply
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from wxpy import *
import time

def question(request):
    try:
        bot = Bot(cache_path=True,qr_path="../static/img/qr.png")
    except Exception,e:
        print e

    time.sleep(2)

    questions = Question.objects.all()
    auto = AutoReply.objects.all()
    
    context = {}
    context['questions'] = questions
    context['auto'] = auto
    return render_to_response('question.html',context)

    if auto:   
        @bot.register()
        def reply_my_friend(msg):
            tuling.do_reply(msg)

    @bot.register()
    def auto_reply(msg):
        for question in questions:
            if isinstance(msg.chat, Friend) & question.content==msg.text:
                return ' {} '.format(msg.text)


