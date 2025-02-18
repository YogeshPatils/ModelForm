from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.
def bookTicketView(request):
    fm=BookTicketForm()
    if request.method=='POST':
        fm=BookTicketForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponse('<h1 style="text-align:center;">Ticket Booked Sucessfully..!</h1>')
    return render(request, 'index.html',{'form':fm})

def passengerView(request):
    qs=BookTicketModel.objects.all()
    return render(request, 'passenger.html',{'ps':qs})