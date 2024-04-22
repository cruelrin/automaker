from django.shortcuts import render, redirect
from .forms import ClientForm, AppointmentForm, MasterForm, PhotoReportForm
from .models import Client, Appointment, Master, Service, PhotoReport
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            return redirect('list_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'create_appointment.html', {'form': form})

def detail_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    return render(request, 'detail_appointment.html', {'appointment': appointment})

def list_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'list_appointments.html', {'appointments': appointments})

def update_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('list_appointments')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'update_appointment.html', {'form': form})

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

def manage_masters(request):
    masters = Master.objects.all()
    if request.method == 'POST':
        form = MasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_masters')
    else:
        form = MasterForm()
    return render(request, 'manage_masters.html', {'masters': masters, 'form': form})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def view_photo_report(request, photo_id):
    photo = PhotoReport.objects.get(id=photo_id)
    return render(request, 'view_photo_report.html', {'photo': photo})
