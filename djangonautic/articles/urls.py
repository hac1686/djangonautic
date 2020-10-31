from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [

    url('^$', views.article_list), # the articles directory
    url('page2', views.article_page2),#page in that directory

]
