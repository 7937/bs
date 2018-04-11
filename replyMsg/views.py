# coding:utf-8
from .models import Question
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse

def question(request):
    questions = Question.objects.all()
    context = {}
    context['questions'] = questions
    return render_to_response('question.html',context)
