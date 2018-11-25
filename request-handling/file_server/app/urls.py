from django.urls import path
from app.views import FileList, file_content
# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам


urlpatterns = [
    # # Определите схему урлов с привязкой к отображениям .views.FileList и .views.file_content
    path('', FileList.as_view(), name='file_list'),
    path('<str:date>/', FileList.as_view(), 'file_list'),
    path('file/<str:name>/', file_content, name='file_content' ),
]
