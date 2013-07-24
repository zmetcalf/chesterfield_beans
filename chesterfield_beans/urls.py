from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from blog.views import show_blogroll, show_blog_entry
from cms.views import get_page, get_home
from site_management.views import register

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chesterfield_beans.views.home', name='home'),
    # url(r'^chesterfield_beans/', include('chesterfield_beans.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^page/(?P<slug>[a-zA-Z0-9_.-]+)/$', get_page, name='page'),
    url(r'^blog/(?P<slug>[a-zA-Z0-9_.-]+)/$', show_blogroll, name='blog'),
    #url(r'^blog-entry/(?P<entry_id>\d+)/$', show_blog_entry,
    #    name='blog_entry'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[a-zA-Z0-9_.-]+)/$',
        show_blog_entry, name='blog_entry'),
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
    url(r'^register/$', register, name='registration'),
    url(r'^$', get_home, name='home'), # Add/remove $ after ^ if 404 instead of homepage
    (r'^comments/', include('django.contrib.comments.urls')),
)
