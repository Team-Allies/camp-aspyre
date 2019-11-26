from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from core.forms import CamperRegistrationForm, CamperScholarshipForm
from core.models import User, Camper, Camp, MedicalInformation, Registration

@login_required
def index(request):
  return render(request, 'core/index.html')

@login_required
def camper_registration(request):
  user = request.user
  camp=Camp.objects.get(pk=1)
  if request.method == 'POST':
    form = CamperRegistrationForm(request.POST)
    if form.is_valid():
      form_data = form.cleaned_data
      previously_attended = form_data.get("previously_attended")
      legal_full_name = form_data.get("legal_full_name")
      preferred_name = form_data.get("preferred_name")
      preferred_pronouns = form_data.get("preferred_pronouns")
      date_of_birth = form_data.get("date_of_birth")
      street_address = form_data.get("street_address")
      city = form_data.get("city")
      state = form_data.get("state")
      zip_code = form_data.get("zip_code")
      phone_number = form_data.get("phone_number")
      email = form_data.get("email")
      name_of_school = form_data.get("name_of_school")
      how_heard_about = form_data.get("how_heard_about")
      facebook = form_data.get("facebook")
      gain_from_camp = form_data.get("gain_from_camp")
      dietary_restrictions = form_data.get("dietary_restrictions")
      tshirt_size = form_data.get("tshirt_size")
      verify_sensitive_topics = form_data.get("verify_sensitive_topics")
      accommodations = form_data.get("accommodations")
      sponsor_org = form_data.get("sponsor_org")
      other_companies_paying = form_data.get("other_companies_paying")
      camper = Camper.objects.create(
        previously_attended = previously_attended,
        legal_full_name = legal_full_name,
        preferred_name = preferred_name,
        preferred_pronouns = preferred_pronouns,
        date_of_birth = date_of_birth,
        street_address =  street_address,
        city = city,
        state = state,
        zip_code = zip_code,
        phone_number = phone_number,
        email = email,
        name_of_school = name_of_school,
        how_heard_about = how_heard_about,
        facebook = facebook,
        gain_from_camp = gain_from_camp,
        dietary_restrictions = dietary_restrictions,
        tshirt_size = tshirt_size,
        verify_sensitive_topics = verify_sensitive_topics,
        accommodations = accommodations,
        sponsor_org = sponsor_org,
        other_companies_paying = other_companies_paying,
        user=user
      )
      registration = Registration.objects.create(
        user=user,
        camper=camper,
        camp=camp
      )
      return redirect(to='camper_registration_submitted')
  else:
    form = CamperRegistrationForm()
  return render(request, 'core/camper_registration.html', {'form': form, 'camp': camp})

@login_required
def camper_registration_submitted(request):
  return render(request, 'core/camper_registration_submitted.html')

@login_required
def camper_medical_form(request):
  return render(request, 'camper_medical_form', {'form': form})

@login_required
def camper_scholarship_form(request):
  user = request.user
  camp=Camp.objects.get(pk=1)
  if request.method == 'POST':
    form = CamperScholarshipForm(request.user, request.POST)
    if form.is_valid():
      form_data = form.cleaned_data
      camper = form_data.get("camper")
      camper.like_to_change = form_data.get("like_to_change")
      camper.currently_involved_activities = form_data.get("currently_involved_activities")
      camper.if_scholarship_not_granted = form_data.get("if_scholarship_not_granted")
      camper.definite_transportation = form_data.get("definite_transportation")
      camper.save()
      return redirect(to='camper_scholarship_submitted')
  else:
    form = CamperScholarshipForm(request.user)
  return render(request, 'core/camper_scholarship.html', {'form': form, 'camp': camp})

@login_required
def camper_scholarship_submitted(request):
  return render(request, 'core/scholarship_form_submitted.html')

# django-registration-redux:
