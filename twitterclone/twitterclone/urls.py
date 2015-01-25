from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    url(r'^twitters/', include('twit.urls')),
    url(r'^accounts/login/$', 'twitterclone.views.login'),
    url(r'^accounts/auth/$', 'twitterclone.views.auth_view'),
    url(r'^accounts/logout/$', 'twitterclone.views.logout'),

    url(r'^accounts/loggedin/$', 'twitterclone.views.loggedin'),
    url(r'^accounts/invalid/$', 'twitterclone.views.invalid_login'),
    url(r'^accounts/register/$', 'twitterclone.views.register_user'),
    url(r'^accounts/register_success/$', 'twitterclone.views.register_success'),


)