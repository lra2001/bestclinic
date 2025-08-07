from django.shortcuts import render

def home(request):
    return render(request, 'bestclinic_app/home.html')