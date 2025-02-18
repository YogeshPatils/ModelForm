from django.db import models

# Create your models here.
class BookTicketModel(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    From=models.CharField(max_length=100)
    To=models.CharField(max_length=100)
    dateOfJou=models.DateField()
    noOfTickets=models.IntegerField()
