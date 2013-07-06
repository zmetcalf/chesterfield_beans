from django.conf.urls import patterns, url

from cms.views import show_content

urlpatterns = patterns('',
        url(r'^(?P<content_id>\d+)/$', show_content, name='content'),
)