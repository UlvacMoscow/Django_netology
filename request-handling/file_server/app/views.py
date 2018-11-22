import datetime
from .settings import FILES_PATH
import os
from django.shortcuts import render
from django.views.generic import TemplateView


class FileList(TemplateView):
    template_name = 'index.html'
    print('111111111111111111111')


    def get_context_data(self, date=None):
        file_list = []
        files = os.listdir(FILES_PATH)
        print(files)
        for file in files:
            file_way = os.path.join(FILES_PATH, file)
            file_info = {
                'name': file,
                'ctime': datetime.datetime.fromtimestamp(os.stat(file_way).st_ctime).strftime("%Y %m, %d"),
                'mtime': os.stat(file_way).st_mtime}
            file_list.append(file_info)
            print('--------------+++++++++++++++++++++')
        print(file_list)
        # datetime.datetime.fromtimestamp(os.stat(file_way).st_ctime).strftime("%Y %m, %d")
        # if not date:
        #     print(files)
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
        return {
            'files': file_list
            # 'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
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
