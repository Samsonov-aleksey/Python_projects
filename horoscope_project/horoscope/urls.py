from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('horoscope/', views.ListHoroscope.as_view(), name='horoscope-list'),
    path('elems/', views.ListElems.as_view(), name='elems-list'),
    path('horoscope/<int:pk>/', views.DetailSign.as_view(), name='onesign'),
    path('elems/<int:pk>/', views.list_elem, name='oneelem'),
    path('', views.DoneView.as_view()),
    path('horoscope/dates',views.month_day_to_sign_zodiac , name = 'horoscope-dates'),
]