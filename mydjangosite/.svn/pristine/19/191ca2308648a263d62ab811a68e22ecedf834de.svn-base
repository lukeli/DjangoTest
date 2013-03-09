# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from blog.models import BlogPost
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.template import RequestContext

def index(request):
    #latest_blogpost_list = BlogPost.objects.all().order_by('-timestamp')[:5]
    # you also can set the default order in the model level:
    #    class Meta:
    #    ordering = ('-timestamp',)
    latest_blogpost_list = BlogPost.objects.all();
    return render_to_response('blog/index.html', {'latest_blogpost_list': latest_blogpost_list})

def archive(request):
    #latest_blogpost_list = BlogPost.objects.all().order_by('-timestamp')[:5]
    latest_blogpost_list = BlogPost.objects.all() [:5]
    return render_to_response('blog/archive.html', {'latest_blogpost_list': latest_blogpost_list})

def detail(request, post_id):
    p = get_object_or_404(BlogPost, pk=post_id)
    return render_to_response('blog/detail.html', {'post': p},
        context_instance=RequestContext(request))