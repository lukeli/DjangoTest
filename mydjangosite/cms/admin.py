__author__ = 'luke.li'
from cms.models import  Category, Story
from django.contrib import admin




class StoryAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "status", "created", "modified")
    search_fields = ("title", "content")
    list_filter = ("status", "owner", "created", "modified")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Story, StoryAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("label",)}

admin.site.register(Category, CategoryAdmin)