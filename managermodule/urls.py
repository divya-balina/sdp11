from django.contrib import admin
from django.urls import path,include

from . import views
app_name = 'managermodule'

urlpatterns = [
    path('addrooms/',views.addrooms,name='addrooms'),
    path('add_room_details/',views.add_room_details,name='add_room_details'),
    path('view/',views.view_roomdetails,name='view_roomdetails'),




]