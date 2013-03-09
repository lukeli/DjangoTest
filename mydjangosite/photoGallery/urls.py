from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from photoGallery.models import  Item, Photo

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Item.objects.all(),
            context_object_name='item_list', template_name='photoGallery/index.html'
           ),
        name = 'index'
    ),

    url(r'^items/$',
        ListView.as_view(
            queryset=Item.objects.all(),
            context_object_name='item_list', template_name='photoGallery/items_list.html'
        ),
        name='item_list',
    ),

    url(r'^items/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Item,
            template_name='photoGallery/items_detail.html'
        ),
        name='item_detail',
    ),

    url(r'^photos/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Photo,
            template_name='photoGallery/photos_detail.html'
        ),
        name='photo_detail',
    ),

)

