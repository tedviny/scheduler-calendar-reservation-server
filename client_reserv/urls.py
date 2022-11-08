from django.urls import path, include, re_path
from . import views

urlpatterns = [
  path('base', views.base, name='base'),
  path('home', views.home, name='home'),
  re_path(r'^reservation/$', views.reservationApi),
  re_path(r'^timeslot/$', views.timeslotApi),
]
