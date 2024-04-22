from django import forms
from .models import Client, Appointment, PhotoReport, Master

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'address', 'phone', 'email']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['client', 'master', 'services', 'total_cost']

class MasterForm(forms.ModelForm):  
    class Meta:
        model = Master
        fields = ['name', 'experience', 'certification', 'specialization']

class PhotoReportForm(forms.ModelForm):
    class Meta:
        model = PhotoReport
        fields = ['before_photo', 'after_photo']
