from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mydjangosite.views.home', name='home'),
    # url(r'^mydjangosite/', include('mydjangosite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   url(r'^admin/', include(admin.site.urls)),

    #Remove all the poll-specific URLs to polls/urls.py
    url(r'^polls/', include('polls.urls' )),
    url(r'^blog/', include('blog.urls' )),
    #url(r'^test/', include('test.urls' )),

    #url(r'^photo/$','photoGallery.views.index'  ),
    url(r'^photoGallery/', include('photoGallery.urls' )),
    url(r'^cms/', include('cms.urls' )),
    url(r'^liveblog/', include('liveblog.urls' )),
    url(r'^pastebin/', include('pastebin.urls' )),
)

# Have Django serve the MEDIA_ROOT
from mydjangosite.settings import MEDIA_ROOT,MEDIA_URL
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT,}),
    #url(r'^'+MEDIA_URL+'(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT,}),
)
