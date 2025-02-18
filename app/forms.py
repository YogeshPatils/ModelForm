from django import forms
from .models import *

class BookTicketForm(forms.ModelForm):
    class Meta:
        model=BookTicketModel
        fields='__all__'

