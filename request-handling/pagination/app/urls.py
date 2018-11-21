from django.urls import path

from app.views import index, bus_stations


urlpatterns = [
    path('', index, name='index'),
    path('bus_stations/<int:count>/', bus_stations, name='bus_stations'),
]
