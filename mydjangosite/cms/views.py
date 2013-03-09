from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q
from cms.models import Story, Category
from django.template import RequestContext
import mydjangosite.site_search as ss

def category(request, slug):
    """Given a category slug, display all items in a category."""
    category = get_object_or_404(Category, slug=slug)
    story_list = Story.objects.filter(category=category)
    heading = "Category: %s" % category.label
    return render_to_response("cms/story_list.html", locals())


def search(request):

    """
    Return a list of stories that match the provided search term
    in either the title or the main content.
    """
    # Old Code
    """
    if 'q' in request.GET:
        term = request.GET['q']
        story_list = Story.objects.filter(Q(title__icontains=term) | Q(markdown_content__icontains=term))
        #story_list = Story.objects.filter(title_iexact=term)
        heading = "Search Results FOR : %S" %term
    return render_to_response("cms/story_list.html", locals())
    """

    # New Code
    query_string = ''
    story_list = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = ss.get_query(query_string, ['title', 'markdown_content',])
        story_list = Story.objects.filter(entry_query)

    heading = "Search Results : %s" % query_string
    return render_to_response("cms/story_list.html", locals())

def add(request):

    """
    Return a list of stories that match the provided search term
    in either the title or the main content.
    """
    add1 = request.GET['add1']
    add2 = request.GET['add2']
    sum = float(add1) + float( add2)
    return render_to_response("cms/add_result.html", locals())
