from django.shortcuts import render

def viewrooms(request):
    return render(request,'customermodule/viewrooms.html')

def bookrooms(request):
    return render(request,'customermodule/bookrooms.html')

from managermodule.models import roomdetails
def roomdetails_list(request):
    roomdetails_list=roomdetails.objects.all()
    return render(request,'customermodule/bookrooms.html',{'roomdetails_list':roomdetails_list})



