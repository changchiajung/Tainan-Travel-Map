from __future__ import unicode_literals
# Create your views here.
import json
# import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import Site, Schedule, MapSite


def index(request):
    content = {}
    recommend = []
    recommend_set = Schedule.objects.order_by('-count')[:10]
    # sort the Schedule and get the top 10 ; the '-' means count backward
    for ele in recommend_set:
        recommend.append({
            'title': ele.title,
            'author': ele.author,
            'content': ele.content,
            'image': ele.content,
            'days': ele.days,
            'count': ele.count,
        })
    content["recommend"] = recommend
    return render(request, 'index.html', content)


def search_dis(request):
    return render(request, 'search.html')


def sch(request, id_num):
    if request.method == "GET":
        content = {}
        site_seq = []
        site_seq_detail = []
        show_schedule = Schedule.objects.get(id=id_num)
        # get the Schedule by id
        show_schedule.count += 1
        # update browse count
        show_schedule.save()
        # save model
        id_seq = [day.split(',') for day in show_schedule.sequence.split('&')]
        # split sequence to each day (type => string)
        for sequences in id_seq:
            site_seq.append([Site.objects.get(id=id) for id in sequences])
        # split each site in day (type => list [int])
        for each_day in site_seq:
            tem = []
            # renew list
            for each_site in each_day:
                site_detail = each_site.site_Id
                # get the corresponding object in mapsite
                tem.append({
                    'site_name': site_detail.site_name,
                    'location_Id': site_detail.location_Id,
                    'image': site_detail.image,
                    'phone_number': site_detail.phone_number,
                    'address': site_detail.address,
                    'count': site_detail.count,
                })
                # put data in the dict
            site_seq_detail.append(tem)
            # in this way the data structure will be [ [ {} .,. {} ],[ {} ... {} ]...[]]
        content['site_seq_detail'] = site_seq_detail
        content['schedule_detail'] = {
            'title': show_schedule.title,
            'author': show_schedule.author,
            'content': show_schedule.content,
            'image': show_schedule.image,
            'days': show_schedule.days,
            'sequence': show_schedule.sequence,
        }
        # put the detail of Schedule in the content
        return render(request, 'sch.html',content)
    else:
        message = request.POST.get('message', '')
        print(message)
        content={}
        content["sequence"] = message
        show_schedule = Schedule.objects.get(id=id_num)
        show_schedule.sequence=message
        show_schedule.save()
        return JsonResponse(content)



def show(request):
    content = {}
    return render(request, 'show.html', content)


def display(request, input_day):
    content ={}
    site_seq=[]
    site_seq_detail=[]
    show_schedule = Schedule.objects.get(id=input_day)
    # get the Schedule by id
    show_schedule.count += 1
    # update browse count
    show_schedule.save()
    # save model
    id_seq = [day.split(',') for day in show_schedule.sequence.split('&')]
    # split sequence to each day (type => string)
    for sequences in id_seq:
        site_seq.append([Site.objects.get(id=id) for id in sequences])
    # split each site in day (type => list [int])
    for each_day in site_seq:
        tem=[]
        # renew list
        for each_site in each_day:
            site_detail = each_site.site_Id
            # get the corresponding object in mapsite
            tem.append({
                'site_name': site_detail.site_name,
                'location_Id': site_detail.location_Id,
                'image': site_detail.image,
                'phone_number': site_detail.phone_number,
                'address': site_detail.address,
                'count': site_detail.count,
            })
            # put data in the dict
        site_seq_detail.append(tem)
        # in this way the data structure will be [ [ {} .,. {} ],[ {} ... {} ]...[]]
    content['site_seq_detail'] = site_seq_detail
    content['schedule_detail'] = {
        'title' : show_schedule.title,
        'author' : show_schedule.author,
        'content' : show_schedule.content,
        'image' : show_schedule.image,
        'days' : show_schedule.days,
    }
    # put the detail of Schedule in the content
    return render(request, 'display.html', content)


def profile(request,user_id):
    return render(request,'profile.html')


def login(request):
    return render(request,'login.html')


def logout(request):
    return render(request,'logout.html')


def register(request):
    return render(request,'register.html')
