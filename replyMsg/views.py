# coding:utf-8
from .models import Question,AutoReply
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from wxpy import *
import time
import itchat
import logging
import threading

def login_c():
    print "login in"

def question(request):
    #bot = Bot(cache_path=True,qr_path="../static/img/qr.png",login_callback=login_c)
    bot = Bot(cache_path=True,console_qr=True)
    tuling = Tuling(api_key='884ea5d4a41d48f583649eb8ea443669')
    
    logging.debug("A log message")	

    time.sleep(2)

    questions = Question.objects.all()
    auto = AutoReply.objects.all()

    context = {}
    context['questions'] = questions
    context['auto'] = auto
  
    for a in auto:
        if a.auto == True:
            @bot.register()
            def reply_my_friend(msg):
                tuling.do_reply(msg)
        else:
            @bot.register()
            def auto_reply(msg):
                for question in questions:
                    if isinstance(msg.chat, Friend) & question.content==msg.text:
                        return ' {} '.format(msg.text)
    return render_to_response('question.html',context)  