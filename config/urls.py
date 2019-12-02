"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', include("django.contrib.auth.urls")),
    path('ASPYRE-Registration/', views.camper_registration, name="camper_registration_form"),
    path('ASPYRE-Registration-submitted', views.camper_registration_form_submitted, name="camper_registration_form_submitted"),
    path('ASPYRE-Scholarship-form/', views.camper_scholarship_form, name="camper_scholarship_form"),
    path('ASPYRE-Scholarship-submitted/', views.camper_scholarship_submitted, name="camper_scholarship_form_submitted"),
    path('ASPYRE-Medical-Form/', views.camper_medical_form, name="camper_medical_form"),
    path('ASPYRE-MedicalForm-submitted', views.camper_medical_form_submitted, name="camper_medical_form_submitted"),
    path('medical_form_section_1', views.medical_form_section_1, name="medical_form_section_1"),
    path('medical_form_section_2', views.medical_form_section_2, name="medical_form_section_2"),
    path('medical_form_section_3', views.medical_form_section_3, name="medical_form_section_3"),
    path('medical_form_section_4', views.medical_form_section_4, name="medical_form_section_4"),
    path('medical_form_section_5', views.medical_form_section_5, name="medical_form_section_5"),
    path('medical_form_section_6', views.medical_form_section_6, name="medical_form_section_6"),
    path('medical_form_section_7', views.medical_form_section_7, name="medical_form_section_7"),
    path('medical_form_section_8', views.medical_form_section_8, name="medical_form_section_8"),
    path('medical_form_section_9', views.medical_form_section_9, name="medical_form_section_9"),
    path('medical_form_section_10', views.medical_form_section_10, name="medical_form_section_10"),
    path('medical_form_section_11', views.medical_form_section_11, name="medical_form_section_11"),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns