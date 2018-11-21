import datetime
from .settings import FILES_PATH
import os
from django.shortcuts import render
from django.views.generic import TemplateView


class FileList(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, date=None):
        # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
        return {
            'files': [
                {'name': 'file_name_1.txt',
                 'ctime': datetime.datetime(2018, 1, 1),
                 'mtime': datetime.datetime(2018, 1, 2)}
            ],
            'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
        }



def file_content(request, name):
    files = os.listdir(FILES_PATH)
    file_content = 'такого файла нету'
    
    for file in files:
        if file == name:
            with open(os.path.join(FILES_PATH, file), encoding='utf8') as necessary_file:
                file_content = necessary_file.read()

    return render(
               request,
               'file_content.html',
               context={'file_name': name, 'file_content':file_content}
           )
