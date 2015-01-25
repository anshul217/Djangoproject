from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all/', 'twit.views.articles'),
    url(r'^get/(?P<twit_id>\d+)/$', 'twit.views.article'),
    url(r'^create/$', 'twit.views.create'),
)
