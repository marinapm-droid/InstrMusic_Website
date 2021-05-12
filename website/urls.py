#  hello/urls.py
from django.conf.urls import url
from django.shortcuts import render
from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about', views.about_page_view, name='about'),
    path('contact_us', views.contact_us_page_view, name='contact_us'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
]
