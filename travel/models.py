
# Create your models here.
from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Schedule(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    #the Title of Schedule
    author = models.CharField(max_length=20,blank=True)
    #the User
    content = models.CharField(max_length=1000,blank=True)
    #the content to the Schedule (by Author)
    style = models.CharField(max_length=100,blank=True)
    #Undifined
    image = models.FileField(blank=True)
    #Image to Schedule Maybe need default
    days = models.IntegerField(blank=True)
    #Total day of Schedule
    sequence = models.CharField(max_length=1000, blank = True)
    count = models.IntegerField(blank = True)
    def __str__(self):
        return self.title


class MapSite(models.Model):
    #For google map
    id = models.IntegerField(primary_key=True)
    site_name = models.CharField(max_length=100)
    #the site name
    location_Id = models.IntegerField(blank=True)
    #google map place Id
    image = models.FileField(blank=True)
    #Image from Google map api
    phone_number = models.CharField(max_length=100, blank=True)
    #Phone Number from Google map api
    address = models.CharField(max_length=100, blank=True)
    #address from Google map api
    site_type= models.CharField(max_length=200, blank = True)
    #undifined
    count = models.IntegerField(blank=True)
    #record to do some System

    def __str__(self):
        return self.site_name


class Site(models.Model):
    #one Mapsite in each schedule represent different Site

    id = models.IntegerField(primary_key=True)
    schedule_Id = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    #record which Schedule
    site_Id = models.ForeignKey(MapSite, on_delete=models.CASCADE)
    #record to MapSIte
    stay_time = models.IntegerField(blank=True)
    #undefined
    site_content = models.TextField(blank=True)
    #describe the Site
    def __str__(self):
        return str(self.day)

