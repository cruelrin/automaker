# views.py

from django.shortcuts import render, redirect
from .forms import ClientForm, AppointmentForm

def register_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect('appointment')
    else:
        form = ClientForm()
    return render(request, 'register_client.html', {'form': form})

def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'make_appointment.html', {'form': form})
