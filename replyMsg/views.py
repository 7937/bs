# coding:utf-8
from .models import Question,AutoReply,Timer
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from wxpy import *
import time,datetime
import itchat
import logging
import threading

def login_c():
    print "login in"

def question(request):
    #bot = Bot(cache_path=True,qr_path="../static/img/qr.png",login_callback=login_c)
    global bot
    bot = Bot(cache_path=True,console_qr=True)
    tuling = Tuling(api_key='884ea5d4a41d48f583649eb8ea443669')
    
    logging.debug("A log message")	

    questions = Question.objects.all()
    auto = AutoReply.objects.all()
    timers = Timer.objects.all()

    context = {}
    context['questions'] = questions
    context['auto'] = auto
    context['timers'] = timers

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


def sendMsgOnTime(timers):
    for sched_time in timers:
        flag = 0
        while True:
            sched_time.receiver = u''.join(sched_time.receiver)
            now = timezone.now() + datetime.timedelta(hours = 8)
            if now.strftime('%Y-%m-%d %H:%M') == sched_time.time.strftime('%Y-%m-%d %H:%M'):
	        friend = bot.friends().search(sched_time.receiver)[0]
    	        friend.send(sched_time.content)
                flag = 1
		time.sleep(60)
            else:
                if flag == 1:
                    sched_time.time = sched_time.time + datetime.timedelta(days = sched_time.recycle)
                    flag = 0
    return    

if __name__ == "__main__":
    th = threading.Thread(sendMsgOnTime(timers))
    th.start()
