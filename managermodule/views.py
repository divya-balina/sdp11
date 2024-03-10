from django.shortcuts import render
from .models import roomdetails

def addrooms(request):
    return render(request, 'managermodule/addrooms.html')

def add_room_details(request):
    if request.method == 'POST':
        no_of_rooms = request.POST.get('no_of_rooms')
        type_of_room = request.POST.get('type_of_room')
        noofpeople = request.POST.get('noofpeople')

        roomdetails_obj = roomdetails(
            no_of_rooms=no_of_rooms,
            type_of_room=type_of_room,
            noofpeople=noofpeople
        )
        roomdetails_obj.save()

        return render(request, 'managermodule/datainserted.html')

    return render(request, 'managerhomepage.html')

def view_roomdetails(request):
    return render(request,'managermodule/view_roomdetails.html')


def viewrooms(request):
    return render(request,'managermodule/viewrooms.html')