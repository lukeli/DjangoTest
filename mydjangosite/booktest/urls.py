from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from test.models import *
urlpatterns = patterns('',
    url(r'^v1$',
        ListView.as_view(
            queryset=Book.objects.order_by('title'),
            context_object_name='book_list', template_name='test/index.html')
        ),
    url(r'^v2$',
        ListView.as_view(
            queryset=Book2.objects.order_by('title'),
            context_object_name='book_list', template_name='test/index.html')
    ),
)