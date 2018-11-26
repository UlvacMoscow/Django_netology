from datetime import datetime as dt
import os
from .settings import FILES_PATH
from django.shortcuts import render_to_response
from django.views.generic import TemplateView



class FileList(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, date=None, **kwargs):
        context = super().get_context_data(**kwargs)
        server_files = []
        for file in os.listdir(FILES_PATH):
            file_stats = os.stat(os.path.join(FILES_PATH, file))
            file_info = {
                'name': file,
                'ctime': dt.fromtimestamp(file_stats.st_ctime),
                'mtime': dt.fromtimestamp(file_stats.st_mtime),
            }

            if date == None or date[:10] == dt.fromtimestamp(file_stats.st_ctime).strftime("%Y-%m-%d") \
             or date[:10] == dt.fromtimestamp(file_stats.st_mtime).strftime("%Y-%m-%d"):
                server_files.append(file_info)

        context.update({
            'files': server_files,
            'date': date  # Этот параметр необязательный
        })
        return context


def file_content(request, name):
    files = os.listdir(FILES_PATH)
    if name in files:
        with open(os.path.join(FILES_PATH, name), encoding='utf8') as f:
            f_content = f.read()
    else:
        f_content = 'File not found'

    return render_to_response(
        'file_content.html',
        context={'file_name': name, 'file_content': f_content}
)



# from datetime import datetime as dt
# from .settings import FILES_PATH
# import os
# from django.shortcuts import render, render_to_response
# from django.views.generic import TemplateView
#
#
# class FileList(TemplateView):
#     template_name = 'index.html'
#     def get_context_data(self, date=None, **kwargs):
#         # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
#         context = super().get_context_data(**kwargs)
#         date = date
#         # date = date if date is not None else ""
#         server_files = []
#         for file in os.listdir(FILES_PATH):
#             file_stats = os.stat(os.path.join(FILES_PATH, file))
#             file_info = {
#                 'name': file,
#                 'ctime': dt.fromtimestamp(file_stats.st_ctime),
#                 'mtime': dt.fromtimestamp(file_stats.st_mtime),
#             }
#
#             print(date)
#             print(dt.fromtimestamp(file_stats.st_mtime).strftime("%Y-%m-%d"))
#
#             if date == dt.fromtimestamp(file_stats.st_ctime).strftime("%Y-%m-%d") \
#              or date == dt.fromtimestamp(file_stats.st_mtime).strftime("%Y-%m-%d"):
#                 server_files.append(file_info)
                # print("+++++++++IF TRUE________")
                # print(date)
                # print(dt.fromtimestamp(file_stats.st_mtime).strftime("%Y-%m-%d"))
            # elif date:
            #     server_files.append(file_info)
                # print("++++ELIF++++")
                # print(date)
            # else:
            #     server_files.append(file_info)
            #     print("++++ELSE++++")
        # context.update({
        #     'files': server_files,
        #     'date': date  # Этот параметр необязательный
        # })
        # return context

    # def get_context_data(self, date=None):
    #     file_list = []
    #     files = os.listdir(FILES_PATH)
    #     for file in files:
    #         file_way = os.path.join(FILES_PATH, file)
    #         create_file_date = dt.fromtimestamp(os.stat(file_way).st_ctime).strftime("%Y-%m-%d")
    #         modified_file_date = dt.fromtimestamp(os.stat(file_way).st_mtime).strftime("%Y-%m-%d")
    #         print('create_file_date: ',create_file_date)
    #         if date == None:
    #             file_info = {
    #                 'name': file,
    #                 'ctime': dt.fromtimestamp(os.stat(file_way).st_ctime).strftime("%Y %B, %d  %H:%M"),
    #                 'mtime': dt.fromtimestamp(os.stat(file_way).st_mtime).strftime("%Y %B, %d  %H:%M"),}
    #             file_list.append(file_info)
    #
    #         if date == create_file_date or date == modified_file_date:
    #             print('heeeeeeeeerrrrrrrrrrrrreeee')
                # print('2018-11-18', True, create_file_date)
                # file_info = {
                #     'name': file,
                #     'ctime': {
                #         'date' : dt.fromtimestamp(os.stat(file_way).st_ctime).strftime("%Y %B, %d  %H:%M").date(),
                #         'time' : dt.fromtimestamp(os.stat(file_way).st_ctime).strftime("%H:%M")
                #     },
                #     'mtime':{
                #         'date' : dt.fromtimestamp(os.stat(file_way).st_mtime).strftime("%Y %B, %d  %H:%M").date(),
                #         'time' : dt.fromtimestamp(os.stat(file_way).st_ctime).strftime("%H:%M")
                #     } }
                # file_list.append(file_info)

                # print('date ', date)
                #
                # print('2 ', dt.fromtimestamp(os.stat(file_way).st_ctime).strftime("%Y %m, %d"))
                # if date == dt.fromtimestamp(os.stat(file_way).st_ctime).strftime("%Y %m, %d"):

        # print(file_list)
        # return {
        #     'files': file_list,
        #     'date': date #необязательно
        # }




# def file_content(request, name):
#     files = os.listdir(FILES_PATH)
#     file_content = 'такого файла нету'
#
#     for file in files:
#         if file == name:
#             with open(os.path.join(FILES_PATH, file), encoding='utf8') as necessary_file:
#                 file_content = necessary_file.read()
#
#     return render_to_response(
#                request,
#                'file_content.html',
#                context={'file_name': name, 'file_content':file_content}
#            )
