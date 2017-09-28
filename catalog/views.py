# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.views.generic import DetailView




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
		queryset = Book.objects.filter(title__icontains='war')[:5] 
		books = Book.objects.all()
		paginate_by = 2
		context = {
			'books': books,
		}
		return render(request, "book_list.html", context)


def get_context_data(self, **kwargs):
	context = super(BookListView, self).get_context_data(**kwargs)
	context['some_data'] = 'This is just some data'
	return context
	
class BookDetailView(DetailView):
	model = Book
	template_name = "book_detail.html"
	
	def get_context_data(self, **kwargs):
		context = super(BookDetailView, self).get_context_data(**kwargs)
		return context
class AuthorListView(generic.ListView):

	def get(self, request):
		authors = Author.objects.all()
		paginate_by = 2
		context = {
			'authors': authors,
		}
		return render(request, "author_list.html", context)


		
class AuthorDetailView(DetailView):
	model = Book
	template_name = "author_detail.html"
	
	def get_context_data(self, **kwargs):
		context = super(AuthorDetailView, self).get_context_data(**kwargs)
		return context
