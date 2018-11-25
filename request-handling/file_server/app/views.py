from datetime import datetime as dt
from .settings import FILES_PATH
import os
from django.shortcuts import render
from django.views.generic import TemplateView


class FileList(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, date=None):
        file_list = []
        files = os.listdir(FILES_PATH)
        for file in files:
            file_way = os.path.join(FILES_PATH, file)
            create_file_date = dt.fromtimestamp(os.stat(file_way).st_ctime).strftime("%Y-%m-%d")
            modified_file_date = dt.fromtimestamp(os.stat(file_way).st_mtime).strftime("%Y-%m-%d")
            print('create_file_date: ',create_file_date)
            if date == None:
                file_info = {
                    'name': file,
                    'ctime': dt.fromtimestamp(os.stat(file_way).st_ctime).strftime("%Y %B, %d  %H:%M"),
                    'mtime': dt.fromtimestamp(os.stat(file_way).st_mtime).strftime("%Y %B, %d  %H:%M"),}
                file_list.append(file_info)

            if date == create_file_date or date == modified_file_date:
                print('heeeeeeeeerrrrrrrrrrrrreeee')
                # print('2018-11-18', True, create_file_date)
                file_info = {
                    'name': file,
                    'ctime': {
                        'date' : dt.fromtimestamp(os.stat(file_way).st_ctime).strftime("%Y %B, %d  %H:%M").date(),
                        'time' : dt.fromtimestamp(os.stat(file_way).st_ctime).strftime("%H:%M")
                    },
                    'mtime':{
                        'date' : dt.fromtimestamp(os.stat(file_way).st_mtime).strftime("%Y %B, %d  %H:%M").date(),
                        'time' : dt.fromtimestamp(os.stat(file_way).st_ctime).strftime("%H:%M")
                    } }
                file_list.append(file_info)

                # print('date ', date)
                #
                # print('2 ', dt.fromtimestamp(os.stat(file_way).st_ctime).strftime("%Y %m, %d"))
                # if date == dt.fromtimestamp(os.stat(file_way).st_ctime).strftime("%Y %m, %d"):

        print(file_list)
        return {
            'files': file_list,
            'date': date #необязательно
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
