from django.views import generic
from .models import Book


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    def get_context_data(self, **kwargs):
        list_book = Book.objects.all()
        return {'list_book': list_book}
