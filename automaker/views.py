# views.py

from django.shortcuts import render, redirect
from .forms import ClientForm, AppointmentForm, PhotoReportForm

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


def make_appointment(request):
    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        photo_report_form = PhotoReportForm(request.POST, request.FILES)
        if appointment_form.is_valid() and photo_report_form.is_valid():
            appointment = appointment_form.save()
            photo_report = photo_report_form.save(commit=False)
            photo_report.appointment = appointment
            photo_report.save()
            return redirect('appointment_success')
    else:
        appointment_form = AppointmentForm()
        photo_report_form = PhotoReportForm()
    return render(request, 'make_appointment.html', {'appointment_form': appointment_form, 'photo_report_form': photo_report_form})
