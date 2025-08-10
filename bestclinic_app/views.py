from django.shortcuts import render
from .forms import AppointmentForm


def home(request):
    return render(request, 'home.html')