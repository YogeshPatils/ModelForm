from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(BookTicketModel)
class BookTicketAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','From','To','dateOfJou','noOfTickets')