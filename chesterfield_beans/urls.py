from django.conf.urls import patterns, include, url
from site_management.views import base

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
    url(r'^main/$', base),
    (r'^comments/', include('django.contrib.comments.urls')),
)
