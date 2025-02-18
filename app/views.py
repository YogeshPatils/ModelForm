from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *

# Create your views here.
def bookTicketView(request):
    fm=BookTicketForm()
    if request.method=='POST':
        fm=BookTicketForm(data=request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponse('''<h1 style="text-align:center;">Ticket Booked Sucessfully..!</h1> <a href={% url 'allTickets' %}>go to tickets table</a>''')
    return render(request, 'index.html',{'form':fm})

def passengerView(request):
    qs=BookTicketModel.objects.all()
    return render(request, 'passenger.html',{'ps':qs})

def updateTicketView(request, id):
    obj=BookTicketModel.objects.get(id=id)
    if request.method == 'POST':
        fm=BookTicketForm(data=request.POST,instance=obj)
        if fm.is_valid():
            fm.save()
        return redirect('allTickets')
    fm=BookTicketForm(instance=obj)
    return render(request, 'update.html',{'form':fm})
    