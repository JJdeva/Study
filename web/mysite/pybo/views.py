from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):
    """
    pybo 목록 출ㅕ
    """
    question_list = models.Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return HttpResponse('hello pybo')