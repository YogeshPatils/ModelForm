from django.urls import path
from .views import *

urlpatterns=[
    path('bookTicket/',bookTicketView,name='bookTicket')
]