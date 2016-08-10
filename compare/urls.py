# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import *

app_name = 'compare'
urlpatterns = [
    url(r'^$', ArticleList.as_view(), name='article_list'),
    url(r'^(?P<pk>\d+)/$', ArticleDetail.as_view(), name='article_detail'),
    url(r'^match/$', NotMatchList.as_view(), name='match_list'),
    url(r'^new/$', NewList.as_view(), name='new_list'),
    url(r'^add_match/(?P<stjornarskra_sentence_id>\d+)/(?P<frumvarp_sentence_id>\d+)/$', add_match, name='add_match'),
    url(r'^remove_match/(?P<stjornarskra_sentence_id>\d+)/(?P<frumvarp_sentence_id>\d+)/$', remove_match, name='remove_match'),
]