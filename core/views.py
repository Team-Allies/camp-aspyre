from django.shortcuts import render

def camper_registration(request):
    return render(request, 'core/camper_registration.html')