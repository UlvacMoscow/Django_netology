from datetime import datetime as dt
from .settings import FILES_PATH
import os
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView



class FileList(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, date=None, **kwargs):
        context = super().get_context_data(**kwargs)
        file_list = []
        for file in os.listdir(FILES_PATH):
            file_stats = os.stat(os.path.join(FILES_PATH, file))
            file_info = {
                'name': file,
                'ctime': dt.fromtimestamp(file_stats.st_ctime),
                'mtime': dt.fromtimestamp(file_stats.st_mtime),
            }


            if date == None or date[:10] == dt.fromtimestamp(file_stats.st_ctime).strftime("%Y-%m-%d") \
             or date[:10] == dt.fromtimestamp(file_stats.st_mtime).strftime("%Y-%m-%d"):
                file_list.append(file_info)

        context.update({
            'files': file_list,
            'date': date  # Этот параметр необязательный
        })
        return context


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
