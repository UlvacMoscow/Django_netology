from django.views import generic
from .models import Book
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator



class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    # paginate_by = 1

    def get_queryset(self):
        if self.kwargs:
            queryset = Book.objects.filter(pub_date=self.kwargs['date'])
            return queryset
        queryset = Book.objects.all().order_by('-pub_date')
        return queryset

    #
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs:
            books = Book.objects.order_by('pub_date')

            current_book = get_object_or_404(Book, pub_date=self.kwargs['date'])
            current_page = list(books).index(current_book)
            count_books = books.count()

            if 0 < current_page < count_books - 1:
                context['next_date'] = str(list(books)[current_page + 1].pub_date)
                context['prev_date'] = str(list(books)[current_page - 1].pub_date)

            elif 0 == current_page:
                context['next_date'] = str(list(books)[current_page + 1].pub_date)

            elif count_books - 1 == current_page:
                context['prev_date'] = str(list(books)[current_page - 1].pub_date)

                return context
