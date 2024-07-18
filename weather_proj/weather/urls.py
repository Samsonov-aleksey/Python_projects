from django.urls import path
from . import views
urlpatterns = [
    path('', views.weather_info, name='weather_info'),
]