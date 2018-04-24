# coding:utf-8
from .models import Question,AutoReply,Timer
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from wxpy import *
import time,datetime,os
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

    for sched_time in timers:
        t = sendMsgInTime(sched_time)
        t.start()

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
                        return u'打字给我看吧 (・ˍ・) '
                    elif int(isinstance(msg.chat, Friend)) & int(question.content==msg.text):
                        return question.answer
                    
    return render_to_response('question.html',context)  


class sendMsgInTime(threading.Thread):
    def __init__(self,sched_time):
        self.sched_time = sched_time
        threading.Thread.__init__(self)

    def run(self):
        flag = 0
        while True:
            self.sched_time.receiver = u''.join(self.sched_time.receiver)
            now = timezone.now() + datetime.timedelta(hours = 8)
            if now.strftime('%Y-%m-%d %H:%M') == self.sched_time.time.strftime('%Y-%m-%d %H:%M'):
                friend = bot.friends().search(self.sched_time.receiver)[0]
                friend.send(self.sched_time.content)
                flag = 1
                time.sleep(60)
            else:
                if flag == 1:
                    self.sched_time.time = self.sched_time.time + datetime.timedelta(days = self.sched_time.recycle)
                    flag = 0


def mutualFriends():
    bot1 = Bot()
    bot2 = Bot()
    for mf in mutual_friends(bot1, bot2):
        print(mf)

def upload_file(request):
    if request.method == "POST":
        myFile = request.FILES.get("myfile",None)
        if not myFile:
            return HttpResponse("no files for upload")
        destination = open(os.path.join("/data/robot/static/file",myFile.name),'wb+')
        for chunk in myFile.chunks():
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")