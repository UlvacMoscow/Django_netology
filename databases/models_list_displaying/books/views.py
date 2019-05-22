from django.views import generic
from .models import Book
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator



class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'

    def get_queryset(self):
        print('queryset calllll')
        queryset = Book.objects.all().order_by('-pub_date')
        return queryset


    def get_context_data(self, **kwargs):
        print('get_context_date calllll')
        context = super().get_context_data(**kwargs)
        if self.kwargs['date']:
            print('date url uuuuusssssssssseeeeeeeeee')
            queryset = Book.objects.filter(pub_date=self.kwargs['date'])
            context['object_list'] = queryset
            return context
        # queryset = Book.objects.filter(pub_date=category_url)
        query_for_paginate = Book.objects.all().order_by('-pub_date')
        paginator_class = Paginator(query_for_paginate, 1)
        # page = paginator_class.get_page(category_url)
        context = {'paginator' : paginator_class}
        context['object_list'] = self.get_queryset()
        # context['books'] = page
        return context
