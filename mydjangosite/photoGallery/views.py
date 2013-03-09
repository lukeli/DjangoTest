# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from photoGallery.models import *
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.template import RequestContext

def index(request):
    #latest_blogpost_list = BlogPost.objects.all().order_by('-timestamp')[:5]
    # you also can set the default order in the model level:
    #    class Meta:
    #    ordering = ('-timestamp',)
    item_list = Item.objects.all();
    return render_to_response('photoGallery/index.html', {'item_list': item_list})

