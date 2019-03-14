"""travelMap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.urls import path
# from django.contrib import admin
# from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.conf import settings
from travel.views import index, search_dis, sch, show, show_result, display, login, logout, register, profile
urlpatterns = [
    url(r'^index', index),
    url(r'^search', search_dis),
    path('sch/<int:id_num>', sch),
    path('show/<slug:slug>',show),
    path('profile/<int:user_id>', profile),
    url(r'^result',show_result),
    url(r'^display/(?P<input_day>[-\w]+)/$', display, name="display"),
    url(r'^accounts/login/$', login),
	url(r'^accounts/logout/$', logout),
	url(r'^accounts/register/$', register),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL)

