from django.conf.urls import patterns, url

from site_management.views import show_cms, show_blogroll, show_blog_entry

urlpatterns = patterns('',
        url(r'^cms/(?P<content_id>\d+)/$', show_cms, name='cms'),
        url(r'^blog/(?P<blog_id>\d+)/$', show_blogroll, name='blog'),
        url(r'^blog/entry/(?P<entry_id>\d+)/$', show_blog_entry,
            name='blog_entry'),
)