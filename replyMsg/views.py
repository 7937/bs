# coding:utf-8
from .models import Question,AutoReply,Timer
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from wxpy import *
import time,datetime
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

    questions = Question.objects.all()
    auto = AutoReply.objects.all()
    timers = Timer.objects.all()

    context = {}
    context['questions'] = questions
    context['auto'] = auto
    context['timer'] = timers

    timers(bot,timers)

    for a in auto:
        if a.auto == True:
            @bot.register()
            def reply_my_friend(msg):
                tuling.do_reply(msg)
        else:
            @bot.register()
            def auto_reply(msg):
                for question in questions:
                    if msg.type != TEXT:
                        return '打字给我看吧 (・ˍ・) '
                    elif int(isinstance(msg.chat, Friend)) & int(question.content==msg.text):
                        return question.answer
                    
    return render_to_response('question.html',context)  

def timer(bot,timers):
    for sched_time in timers:
        flag = 0
        while True:
            now = datetime.datetime.now()
            if now == sched_time.time:
                send_message(bot,sched_time.receiver,sched_time.content)
                flag = 1
            else:
                if flag == 1:
                    sched_time = sched_time + datetime.timedelta(days = recycle)
                    flag = 0
    

def send_message(bot,receiver,content):
    friend = bot.friends().search(receiver)[0]
    friend.send(content)
    