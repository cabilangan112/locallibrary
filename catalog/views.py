# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic




def index(request):
	num_books=Book.objects.all().count()
	num_instances=BookInstance.objects.all().count()
	num_instances_available=BookInstance.objects.filter(status__exact='a').count()
	num_authors=Author.objects.count()
	
	return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )

class BookListView(generic.ListView):
	def get(self, request):
		queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
		books = Book.objects.all()
		context = {
			'books': books,
		}
		return render(request, "book_list.html", context)


def get_context_data(self, **kwargs):
	context = super(BookListView, self).get_context_data(**kwargs)
	context['some_data'] = 'This is just some data'
	return context

class BookDetailView(generic.DetailView):
	model = Book
	
def book_detail_view(request,pk):
    try:
        book_id=Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
	#book_id=get_object_or_404(Book, pk=pk)
    
    return render(
        request,
        'book_detail.html',
        context={'book':book_id,})
