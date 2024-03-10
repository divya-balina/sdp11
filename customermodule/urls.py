from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('viewrooms/',views.viewrooms,name='viewrooms'),
    path('bookrooms/',views.bookrooms,name='bookrooms'),
    path('list/',views.roomdetails_list,name='roomdetails_list'),


]