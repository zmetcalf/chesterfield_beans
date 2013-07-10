from django.conf.urls import patterns, url

from site_management.views import show_cms

urlpatterns = patterns('',
        url(r'^cms/(?P<content_id>\d+)/$', show_cms, name='cms'),
)