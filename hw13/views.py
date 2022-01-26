from django.shortcuts import render

# Create your views here.
from django.views import generic

from hw13.models import Quote, Author


class QuoteListView(generic.ListView):
    model = Quote
    paginate_by = 15


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 15


class AuthorDetailView(generic.DetailView):
    model = Quote
