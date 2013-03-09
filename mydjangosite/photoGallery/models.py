from django.db import models
from django.db.models import permalink
from django.contrib import admin

from photoGallery.fields import ThumbnailImageField

class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        """
        This decorator takes the name of a URL pattern (either a view name or a URL pattern name)
        and a list of position or keyword arguments and uses the URLconf patterns to
        construct the correct, full URL. It returns a string for the correct URL, with all
        parameters substituted in the correct positions.

        For Example, if the URLConf contains:  -- URL of "item_details"
            url(r'^items/(?P<pk>\d+)/$',
                DetailView.as_view(
                    model=Item,
                    template_name='photoGallery/items_detail.html'
                ),
                name='item_detail',
            ),

        Then the item.get_absolute_url will return values -- .../items/1/, .../items/2/,
        -- using the item.id to replace the (?P<pk>\d+) in the URL of "item_details"

        We can define many  @permalink functions to return to different URLs
        @permalink
         def get_edit_url(self):
            return ('item_edit', [str(self.id)])
        """
        return ('item_detail', [str(self.id)])

class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField(max_length=100)
    #image = models.ImageField(upload_to='photos')
    image = ThumbnailImageField(upload_to='photos')

    caption = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('photo_detail', [str(self.id)] )

class PhotoInline(admin.StackedInline):
    model = Photo

class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)
