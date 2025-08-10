from django.db import models

class Patient(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  date_of_birth = models.DateField()
  address = models.CharField(max_length=255)
  phone_number = models.CharField(max_length=15, blank=True, null=True)
  email = models.EmailField(blank=True, null=True)

class Doctor(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  specialty = models.CharField(max_length=255)
  phone_number = models.CharField(max_length=15, blank=True, null=True)
  email = models.EmailField(blank=True, null=True)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True, null=True)