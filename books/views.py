# Create your views here.
from books.models import Publisher, Book
from django.shortcuts import render_to_response
from django.views.generic.simple import direct_to_template
from django.template.base import TemplateDoesNotExist
from django.http import Http404

def my_homepage_view(request):
    return Publisher.objects.update();

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', {'books': books, 'query': q})
    return render_to_response('search_form.html', {'errors': errors})

def about_pages(request, page):
    try:
        return direct_to_template(request, template='about/%s.html' % page)
    except TemplateDoesNotExist:
        raise Http404
