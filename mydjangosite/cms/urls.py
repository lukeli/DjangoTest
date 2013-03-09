from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from cms.models import Story

#Using the Generic Views
urlpatterns = patterns('',
    url(r'^story/$',
        ListView.as_view(
            queryset= Story.objects.all(),
            context_object_name='story_list',
            template_name='cms/story_list.html'
        ),
        name = 'cms_home',
    ),

    url(r'^story/(?P<slug>[-\w]+)/$',
        DetailView.as_view(
            model=Story,
            template_name='cms/story_details.html'
        ),
        name = 'cms_story',
    ),
)

# Using the customized view
urlpatterns += patterns('cms.views',
    url(r'^search/$', 'search', name = 'cms_search'),
    url(r'^category/(?P<slug>[-\w]+)/$', 'category', name="cms_category"),
    url(r'^add/$', 'add', name = 'cms_add'),
)

