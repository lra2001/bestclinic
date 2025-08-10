from django.contrib import admin
from .models import Appointment, Patient, Doctor

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'date_of_birth', 'phone_number', 'email')
    search_fields = ('firstname', 'lastname', 'email')
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'specialty', 'phone_number', 'email')
    search_fields = ('firstname', 'lastname', 'specialty', 'email')
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time')
    search_fields = ('patient__firstname', 'doctor__firstname', 'date')
    list_filter = ('date', 'doctor')

# Register your models here.
