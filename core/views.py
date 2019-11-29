from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from core.forms import CamperRegistrationForm, CamperScholarshipForm, CamperMedicalForm
from core.models import User, Camper, Camp, MedicalInformation, Registration

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
      have_disability = form_data.get("have_disability")
      accommodations = form_data.get("accommodations")
      sponsor_org = form_data.get("sponsor_org")
      other_companies_paying = form_data.get("other_companies_paying")
      camper = Camper.objects.create(
        previously_attended=previously_attended,
        legal_full_name=legal_full_name,
        preferred_name=preferred_name,
        preferred_pronouns=preferred_pronouns,
        date_of_birth=date_of_birth,
        street_address= street_address,
        city=city,
        state=state,
        zip_code=zip_code,
        phone_number=phone_number,
        email=email,
        name_of_school=name_of_school,
        how_heard_about=how_heard_about,
        facebook=facebook,
        gain_from_camp=gain_from_camp,
        dietary_restrictions=dietary_restrictions,
        tshirt_size=tshirt_size,
        verify_sensitive_topics=verify_sensitive_topics,
        have_disability=have_disability,
        accommodations=accommodations,
        sponsor_org=sponsor_org,
        other_companies_paying=other_companies_paying,
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
  user = request.user
  camp=Camp.objects.get(pk=1)
  if request.method == 'POST':
    form = CamperMedicalForm(request.POST)
    if form.is_valid():
      form_data = form.cleaned_data
      date_of_birth = form_data.get("date_of_birth")
      height = form_data.get("height")
      weight = form_data.get("weight")
      biological_sex = form_data.get("biological_sex")
      full_address = form_data.get("full_address")
      emergency_contact = form_data.get("emergency_contact")
      relationship_to_student = form_data.get("relationship_to_student")
      best_phone_number_during_camp = form_data.get("best_phone_number_during_camp")
      best_phone_number_during_camp_secondary = form_data.get("best_phone_number_during_camp_secondary")
      alternate_contact = form_data.get("alternate_contact")
      doctor_name = form_data.get("doctor_name")
      doctor_phone = form_data.get("doctor_phone")
      doctor_address = form_data.get("doctor_address")
      health_insurance_name = form_data.get("health_insurance_name")
      insurance_policy_number = form_data.get("insurance_policy_number")
      other_pertinent_insurance_info = form_data.get("other_pertinent_insurance_info")
      taking_meds = form_data.get("taking_meds")
      nervousness = form_data.get("nervousness")
      mental_disorder = form_data.get("mental_disorder")
      convulsions_epilepsy = form_data.get("convulsions_epilepsy")
      fainting = form_data.get("fainting")
      heart_condition = form_data.get("heart_condition")
      rheumatic_fever = form_data.get("rheumatic_fever")
      cancer_tumor = form_data.get("cancer_tumor")
      high_blood_pressure = form_data.get("high_blood_pressure")
      headaches = form_data.get("headaches")
      asthma = form_data.get("asthma")
      ulcers = form_data.get("ulcers")
      diabetes = form_data.get("diabetes")
      medication_allergies = form_data.get("medication_allergies")
      other_allergies_illnesses = form_data.get("other_allergies_illnesses")
      physical_limitations = form_data.get("physical_limitations")
      details_answers = form_data.get("details_answers")
      camper = MedicalInformation.objects.create(
        user=user,
        date_of_birth=date_of_birth,
        height=height,
        weight=weight,
        biological_sex=biological_sex,
        full_address=full_address,
        emergency_contact=emergency_contact,
        relationship_to_student=relationship_to_student,
        best_phone_number_during_camp=best_phone_number_during_camp,
        best_phone_number_during_camp_secondary=best_phone_number_during_camp_secondary,
        alternate_contact=alternate_contact,
        doctor_name=doctor_name,
        doctor_phone=doctor_phone,
        doctor_address=doctor_address,
        health_insurance_name=health_insurance_name,
        insurance_policy_number=insurance_policy_number,
        other_pertinent_insurance_info=other_pertinent_insurance_info,
        taking_meds=taking_meds,
        nervousness=nervousness,
        mental_disorder=mental_disorder,
        convulsions_epilepsy=convulsions_epilepsy,
        fainting=fainting,
        heart_condition=heart_condition,
        rheumatic_fever=rheumatic_fever,
        cancer_tumor=cancer_tumor,
        high_blood_pressure=high_blood_pressure,
        headaches=headaches,
        asthma=asthma,
        ulcers=ulcers,
        diabetes=diabetes,
        medication_allergies=medication_allergies,
        other_allergies_illnesses=other_allergies_illnesses,
        physical_limitations=physical_limitations,
        details_answers=details_answers,
      )
      registration = Registration.objects.get(
        user=user,
        camper=camper,
        camp=camp
      )
      return redirect(to='camper_medical_form_submitted')
  else:
    form = CamperMedicalForm()
  return render(request, 'core/camper_medical_form.html', {'form': form, 'camp': camp})

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


@login_required
def camper_medical_form_submitted(request):
  return render(request, 'core/camper_medical_form_submitted.html')

