from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField("Post Time")

    def __str__(self):
        return self.title

    def was_posted_recently(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(days=1)

    was_posted_recently.admin_order_field = 'timestamp'
    was_posted_recently.boolean = True
    was_posted_recently.short_description = 'Posted recently?'

    class Meta:
        ordering = ('-timestamp',)