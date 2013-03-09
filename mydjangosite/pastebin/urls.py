from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from pastebin.models import Paste

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Paste.objects.all(),
            context_object_name='object_list', template_name='pastebin/paste_list.html'
        ),
        name = 'paste_list'
    ),

    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Paste,
            template_name='pastebin/paste_detail.html'
        ),
        name = 'paste_details'
    ),

    url(r'^add/$',
        CreateView.as_view(
            model= Paste,
            template_name='pastebin/paste_form.html'
        ),
        name='paste_add'),

    url(r'^edit/(?P<pk>\d+)/$',
        UpdateView.as_view(
            model= Paste,
            template_name='pastebin/paste_form.html'
        ),
        name='paste_edit'),

)
