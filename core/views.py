from django.shortcuts import render, redirect, get_object_or_404
from core.forms import CamperRegistrationForm
from core.models import User, Camper, Camp, MedicalInformation

def index(request):
  return render(request, 'core/index.html')

def camper_registration(request):
  form = CamperRegistrationForm(request.POST)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      pass
      #redirect to new URL...probably payment page or scholarship form
    else:
      form = CamperRegistrationForm()
  return render(request, 'core/camper_registration.html', {'form': form})

def camper_registration_submitted(request):
  return render(request, 'core/camper_registration_submitted.html')

def camper_medical_form(request):
#   form = CamperMedicalForm(request.POST)
#   if request.method == 'POST':
#     if form.is_valid():
#       form.save()
#       pass
#     else:
#       form = CamperMedicalForm()
  return render(request, 'core/camper_medical_form.html', {'form': form})
  