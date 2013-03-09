__author__ = 'luke.li'
from blog.models import BlogPost
from django.contrib import admin

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

admin.site.register(BlogPost, BlogPostAdmin)