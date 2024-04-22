from django.urls import path
from .views import create_appointment, detail_appointment, list_appointments, update_appointment, view_photo_report, manage_masters, services

urlpatterns = [
    path('create_appointment/', create_appointment, name='create_appointment'),
    path('detail_appointment/<int:appointment_id>/', detail_appointment, name='detail_appointment'),
    path('list_appointments/', list_appointments, name='list_appointments'),
    path('update_appointment/<int:appointment_id>/', update_appointment, name='update_appointment'),
    path('view_photo_report/<int:photo_id>/', view_photo_report, name='view_photo_report'),
    path('manage_masters/', manage_masters, name='manage_masters'),
    path('services/', services, name='services'),
    path('', create_appointment, name='home'),
]
