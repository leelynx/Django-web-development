from django.shortcuts import render_to_response
from booksapp.models import Book


def search(req):
    error = False
    if 'q' in req.GET:
        q = req.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', {'books': books, 'query': q})
    return render_to_response('search_form.html', {'error': error})
