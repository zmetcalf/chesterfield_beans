from django.conf.urls import patterns, url

from cms import views

urlpatterns = patterns('',
    # url(r'^$', views.IndexView.as_view(), name = 'index'),   
    url(r'^(?P<poll_id>\d+)/content/$', views.content, name = 'content'),
)