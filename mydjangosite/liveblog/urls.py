from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from liveblog.models import  BlogUpdate

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=BlogUpdate.objects.all(),
            context_object_name='object_list', template_name='liveblog/update_list.html'
           ),
        name = 'blog_list'
    ),
)


urlpatterns += patterns ('liveblog.views',
    url(r'^update_after/(?P<id>\d+)/$', 'update_after' ),
)

