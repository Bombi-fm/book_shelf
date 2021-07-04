
from django.views import generic
from .models import Book, Genre


# Create your views here.


class BookListView(generic.ListView):
    model = Book
    template_name = 'bookshelf/book_list.html'
    context_object_name = 'book_list'
    queryset = Book.objects.all()


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'bookshelf/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.filter(bookgenre__book=context['object'])
        return context


class GenreListView(generic.ListView):
    model = Genre
    template_name = 'bookshelf/genre_list.html'
    context_object_name = 'genre_list'
    queryset = Genre.objects.all()


