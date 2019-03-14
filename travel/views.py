from __future__ import unicode_literals
# Create your views here.
import json
# import requests
from django.shortcuts import render
from .models import Site, Schedule, MapSite
from django.db.models import Count

def index(request):
    content={}
    recommend = []
    set = Schedule.objects.annotate(Count('count')).order_by('-count__count')[:10]
    for ele in set:
        recommend.append({
            'titel':ele.title,
            'author':ele.author,
            'content':ele.content,
            'image':ele.content,
            'days':ele.days,
            'count':ele.count,
        })
    content["recommend"] = recommend
    return render(request,'index.html',content)


def search_dis(request):
    return render(request,'search.html')


def sch(request, id_num):
    return render(request,'sch.html')


def show(request):
    return render(request,'show.html')


def show_result(request):
    return render(request,'show.html')


def display(request, input_day):
    return render(request,'display.html')


def profile(request,user_id):
    return render(request,'profile.html')


def login(request):
    return render(request,'login.html')


def logout(request):
    return render(request,'logout.html')


def register(request):
    return render(request,'register.html')
