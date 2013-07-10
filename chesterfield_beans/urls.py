from django.conf.urls import patterns, include, url
from site_management.views import base
from cms.views import show_content

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
    url(r'^', include('site_management.urls', namespace="manager")),
    #url(r'^content/', include('cms.urls', namespace = "content")),
    #(r'^comments/', include('django.contrib.comments.urls')),
)
