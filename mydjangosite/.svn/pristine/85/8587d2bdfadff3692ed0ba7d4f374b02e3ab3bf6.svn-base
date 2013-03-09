# Create your views here.

from django.http import HttpResponse
from django.core import serializers

from liveblog.models import BlogUpdate


def update_after(request, id):
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(serializers.serialize("json", BlogUpdate.objects.filter(pk__gt=id)))
    return response
