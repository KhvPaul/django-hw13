from django.views import generic

from hw13.models import Author, Quote


class QuoteListView(generic.ListView):
    model = Quote
    paginate_by = 10


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 15


class AuthorDetailView(generic.DetailView):
    model = Author
