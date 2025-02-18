from django.urls import path
from .views import *

urlpatterns=[
    path('bookTicket/',bookTicketView,name='bookTicket'),
    path('allTickets/',passengerView,name='allTickets'),
    path('update/<int:id>',updateTicketView,name='update'),
]