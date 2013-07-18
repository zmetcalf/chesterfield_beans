from django.conf.urls import patterns, include, url

from blog.views import show_blogroll, show_blog_entry
from cms.views import show_cms
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chesterfield_beans.views.home', name='home'),
    # url(r'^chesterfield_beans/', include('chesterfield_beans.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cms/(?P<content_id>\d+)/$', show_cms, name='cms'),
    url(r'^blog/(?P<blog_id>\d+)/$', show_blogroll, name='blog'),
    url(r'^blog/entry/(?P<entry_id>\d+)/$', show_blog_entry,
        name='blog_entry'),
    # url(r'^', include('site_management.urls', namespace="manager")),
    # (r'^comments/', include('django.contrib.comments.urls')),
)
