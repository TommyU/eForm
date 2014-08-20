from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns('',
    url(r'^$',requestList.as_view()),
    url(r'^(?P<pk>[\d]+)/$',requestDetail.as_view()),
    url(r'^create/$',requestCreate.as_view()),
    url(r'^delete/(?P<pk>[\d]+)$',requestDelete.as_view()),
    url(r'^update/(?P<pk>[\d]+)$',requestUpdate.as_view()),
    url(r'^(?P<val>[\w]+)/$',requestList.as_view()),

)
