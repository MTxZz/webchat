# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from django.urls import path

from . import views
app_name = 'chat'
urlpatterns = [
    url(
        regex=r'^dialogs/(?P<username>[\w.@+-]+)/$',
        view=views.DialogListView.as_view(),
        name='dialogs_detail'
    ),
    url(
        regex=r'^dialogs/$',
        view=views.DialogListView.as_view(),
        name='dialogs'
    ),

    path('chatList/', views.chatList, name = 'chatList'),
    path('rooms/', views.rooms, name='home'),
    path('room/<str:room_name>/', views.chatRoom, name='room'),
]


