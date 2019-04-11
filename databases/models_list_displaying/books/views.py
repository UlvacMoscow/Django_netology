from django.views import generic
from .models import Book
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator



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
        query_for_paginate = Book.objects.all().order_by('-pub_date')
        paginator_class = Paginator(query_for_paginate, 1)
        print('11111111111111 ', dir(paginator_class))
        page = paginator_class.get_page(category_url)
        context = {'paginator' : paginator_class}
        context['object_list'] = queryset
        context['books'] = page
        return context
