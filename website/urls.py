from django.conf.urls import url
from django.shortcuts import render
from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('home', views.home_page_view, name='home'),
    path('faq', views.faq_page_view, name='faq'),
    path('about_website', views.about_website_page_view, name='about_website'),
    path('about', views.about_page_view, name='about'),
    path('instructions', views.instructions_page_view, name='instructions'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('download', views.download_page_view, name='download'),
    path('comments', views.comments_page_view, name='comments'),
    path('contact_us', views.contact_us_page_view, name='contact_us'),
    path('list_contact', views.list_contact_page_view, name='list_contact'),
    path('edit_contact/<int:contact_id>', views.edit_contact_page_view, name='edit_contact'),
    path('remove_contact/<int:contact_id>', views.remove_contact_page_view, name='remove_contact'),
    path('events_details/<int:events_id>', views.events_detail_page_view, name='events_details'),
    path('events', views.events_page_view, name='events'),
    path('events_details/<int:events_id>/participate', views.participate_page_view, name='participate'),
    path('login', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),
    path('quizz_results', views.quizz_results_page_view, name='quizz_results'),
    path('result_comment', views.comment_results_page_view, name='result_comment'),
    path('new_event', views.new_event_page_view, name='new_event'),
    path('spa', views.spa_page_view, name='spa'),
    path("sections/<int:num>", views.section, name="section"),
    path("article_1", views.article_1, name="article_1"),
    path("article_2", views.article_2, name="article_2"),
    path("article_3", views.article_3, name="article_3"),
    path("article_4", views.article_4, name="article_4"),

]
