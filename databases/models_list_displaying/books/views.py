from django.views import generic
from .models import Book
from django.shortcuts import get_object_or_404



class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    queryset = Book.objects.all().order_by('pub_date')
    def get_queryset(self):
        category_url = self.kwargs['date']
        # print('111111111111111111111111 ', category_url)
    # queryset = Book.objects.filter(name='Война и мир')
    # def get_queryset(self):
    #
    #     pass
    # queryset = ['pub_date']
    # context_object_name = 'book_list'
    # paginate_by = 2
    # def get_context_data(self,request, date=None, **kwargs):
    #     template_name = 'book_date.html'
    #     context = super().get_context_data(**kwargs)
    #     print('222222222222 ', context)
    #     get_date_obj = date
    #     date = request.GET.get('books')
    #
    #     print('111111111111111111111 ',date)
    #     list_book = Book.objects.all()
    #     return {'list_book': list_book}
    # def get_queryset(self):
    #     # template_name = 'book_date.html'
    #     # queryset = Book.objects.filter(pub_date='2018-09-05')
    #     # print(self.request)
    #     self.Book = get_object_or_404(Book, pub_date=self.kwargs['pub_date'])
    #     return Book.objects.filter(pub_date=self.Book)
