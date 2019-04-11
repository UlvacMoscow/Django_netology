from django.views import generic
from .models import Book
from django.shortcuts import get_object_or_404



class BookListView(generic.ListView):
    def __init__(self):
        super().__init__()
        self.model = Book
        self.template_name = 'book_list.html'

    def get_queryset(self):
        queryset = Book.objects.all().order_by('-pub_date')
        return queryset



class BookFilterDate(BookListView):
    def __init__(self):
        super().__init__()


    def get_context_data(self):
        category_url = self.kwargs['date']
        queryset = Book.objects.filter(pub_date=category_url)
        print('111111111111111 ', Paginator)
        context = {'object_list' : queryset}
        return context
