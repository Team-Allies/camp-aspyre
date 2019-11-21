from django.shortcuts import render, redirect, get_object_or_404
from core.forms import CamperRegistrationForm
from core.models import User, Camper

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

  