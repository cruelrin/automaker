from django import forms
from .models import Client, Appointment

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'address', 'phone', 'email']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['client', 'master', 'services', 'total_cost']
