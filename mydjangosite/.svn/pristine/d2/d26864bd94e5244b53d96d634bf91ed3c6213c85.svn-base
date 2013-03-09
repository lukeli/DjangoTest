from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from blog.models import BlogPost
urlpatterns = patterns('blog.views',
    #All polls-specific URLS are here
    url(r'^$', 'index'),
    url(r'archive/$',  'archive'),
    url(r'^(?P<post_id>\d+)/$', 'detail'),

)