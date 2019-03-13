from __future__ import unicode_literals
# Create your views here.
import json
# import requests
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


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


def login(request):
    return render(request,'login.html')


def logout(request):
    return render(request,'logout.html')


def register(request):
    return render(request,'register.html')
