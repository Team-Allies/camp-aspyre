from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from core.forms import CamperRegistrationForm, CamperScholarshipForm, CamperMedicalForm
from core.models import User, Camper, Camp, MedicalInformation, Registration
from django.core.mail import send_mail

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
      has_camper_previously_attended_ASPYRE = form_data.get("has_camper_previously_attended_ASPYRE")
      legal_full_name_of_camper = form_data.get("legal_full_name_of_camper")
      preferred_name_of_camper = form_data.get("preferred_name_of_camper")
      preferred_pronouns_of_camper = form_data.get("preferred_pronouns_of_camper")
      date_of_birth_of_camper = form_data.get("date_of_birth_of_camper")
      street_address_of_camper = form_data.get("street_address_of_camper")
      city_of_camper = form_data.get("city_of_camper")
      state_of_camper = form_data.get("state_of_camper")
      zip_code_of_camper = form_data.get("zip_code_of_camper")
      phone_number_of_camper = form_data.get("phone_number_of_camper")
      email_of_camper = form_data.get("email_of_camper")
      name_of_school = form_data.get("name_of_school")
      how_did_the_camper_hear_about_the_camp = form_data.get("how_did_the_camper_hear_about_the_camp")
      would_the_camper_like_to_be_added_facebook = form_data.get("would_the_camper_like_to_be_added_facebook")
      what_does_the_camper_want_to_gain_from_the_camp = form_data.get("what_does_the_camper_want_to_gain_from_the_camp")
      does_camper_have_any_dietary_restrictions = form_data.get("does_camper_have_any_dietary_restrictions")
      does_the_camper_have_any_disabilities = form_data.get("does_the_camper_have_any_disabilities")
      any_additional_accommodations_needed = form_data.get("any_additional_accommodations_needed")
      does_the_camper_have_any_sponsoring_organizations = form_data.get("does_the_camper_have_any_sponsoring_organizations")
      tshirt_size = form_data.get("tshirt_size")
      has_the_camper_verified_that_sensitive_topics_will_be_covered = form_data.get("has_the_camper_verified_that_sensitive_topics_will_be_covered")
      does_the_camper_have_other_companies_paying = form_data.get("does_the_camper_have_other_companies_paying")
      camper = Camper.objects.create(
        has_camper_previously_attended_ASPYRE=has_camper_previously_attended_ASPYRE,
        legal_full_name_of_camper=legal_full_name_of_camper,
        preferred_name_of_camper=preferred_name_of_camper,
        preferred_pronouns_of_camper=preferred_pronouns_of_camper,
        date_of_birth_of_camper=date_of_birth_of_camper,
        street_address_of_camper= street_address_of_camper,
        city_of_camper=city_of_camper,
        state_of_camper=state_of_camper,
        zip_code_of_camper=zip_code_of_camper,
        phone_number_of_camper=phone_number_of_camper,
        email_of_camper=email_of_camper,
        name_of_school=name_of_school,
        how_did_the_camper_hear_about_the_camp=how_did_the_camper_hear_about_the_camp,
        would_the_camper_like_to_be_added_facebook=would_the_camper_like_to_be_added_facebook,
        what_does_the_camper_want_to_gain_from_the_camp=what_does_the_camper_want_to_gain_from_the_camp,
        does_camper_have_any_dietary_restrictions=does_camper_have_any_dietary_restrictions,
        does_the_camper_have_any_disabilities=does_the_camper_have_any_disabilities,
        any_additional_accommodations_needed=any_additional_accommodations_needed,
        does_the_camper_have_any_sponsoring_organizations=does_the_camper_have_any_sponsoring_organizations,
        tshirt_size=tshirt_size,
        has_the_camper_verified_that_sensitive_topics_will_be_covered=has_the_camper_verified_that_sensitive_topics_will_be_covered,
        does_the_camper_have_other_companies_paying=does_the_camper_have_other_companies_paying,        
        user=user,
      )
      registration = Registration.objects.create(
        user=user,
        camper=camper,
        camp=camp
      )
      send_mail('Test Email', f'This is an automated email saying that a new registration was submitted for {legal_full_name_of_camper}', 'jjporter921@gmail.com', [f'{email_of_camper}'])
      return redirect(to='camper_registration_form_submitted')
  else:
    form = CamperRegistrationForm()
  return render(request, 'core/camper_registration.html', {'form': form, 'camp': camp})

@login_required
def camper_registration_form_submitted(request):
  return render(request, 'core/camper_registration_submitted.html')

@login_required
def camper_medical_form(request):
  user = request.user
  camp=Camp.objects.get(pk=1)
  if request.method == 'POST':
    form = CamperMedicalForm(request.POST)
    breakpoint()
    if form.is_valid():
      form_data = form.cleaned_data
      first_guardian_name = form.data.get("first_guardian_name")
      first_guardian_phone_number = form.data.get("first_guardian_phone_number")
      first_guardian_home_work_or_cell = form.data.get("first_guardian_home_work_or_cell")
      second_guardian_name = form.data.get("second_guardian_name")
      second_guardian_phone_number = form.data.get("second_guardian_phone_number")
      second_guardian_home_work_or_cell = form.data.get("second_guardian_home_work_or_cell")
      third_guardian_name = form.data.get("third_guardian_name")
      third_guardian_phone_number = form.data.get("third_guardian_phone_number")
      third_guardian_home_work_or_cell = form.data.get("third_guardian_home_work_or_cell")
      emergency_contact_name = form.data.get("emergency_contact_name")
      emergency_contact_phone_number = form.data.get("emergency_contact_phone_number")
      emergency_home_work_cell = form.data.get("emergency_home_work_cell")
      can_camper_be_picked_up_by_guardian_or_emergency_contact = form.data.get("can_camper_be_picked_up_by_guardian_or_emergency_contact")
      any_unauthorized_persons_that_can_pick_up_camper = form.data.get("any_unauthorized_persons_that_can_pick_up_camper")
      first_authorized_persons_name = form.data.get("first_authorized_persons_name")
      first_authorized_persons_phone = form.data.get("first_authorized_persons_phone")
      second_authorized_persons_name = form.data.get("second_authorized_persons_name")
      second_authorized_persons_phone = form.data.get("second_authorized_persons_phone")
      family_physician_NP_PA_name = form.data.get("family_physician_NP_PA_name")
      family_physician_NP_PA_phone_number = form.data.get("family_physician_NP_PA_phone_number")
      mental_healthcare_provider_name = form.data.get("mental_healthcare_provider_name")
      mental_healthcare_provider_phone_number = form.data.get("mental_healthcare_provider_phone_number")
      will_camper_take_medication_while_at_camp = form.data.get("will_camper_take_medication_while_at_camp")
      first_medication_name = form.data.get("first_medication_name")
      first_medication_dose = form.data.get("first_medication_dose")
      first_medication_times = form.data.get("first_medication_times")
      first_medication_reason_for_taking = form.data.get("first_medication_reason_for_taking")
      first_medication_prescriber_name = form.data.get("first_medication_prescriber_name")
      first_medication_prescriber_phone_number = form.data.get("first_medication_prescriber_phone_number")
      second_medication_name = form.data.get("second_medication_name")
      second_medication_dose = form.data.get("second_medication_dose")
      second_medication_times = form.data.get("second_medication_times")
      second_medication_reason_for_taking = form.data.get("second_medication_reason_for_taking")
      second_medication_prescriber_name = form.data.get("second_medication_prescriber_name")
      second_medication_prescriber_phone_number = form.data.get("second_medication_prescriber_phone_number")
      third_medication_name = form.data.get("third_medication_name")
      third_medication_dose = form.data.get("third_medication_dose")
      third_medication_times = form.data.get("third_medication_times")
      third_medication_reason_for_taking = form.data.get("third_medication_reason_for_taking")
      third_medication_prescriber_name = form.data.get("third_medication_prescriber_name")
      third_medication_prescriber_phone_number = form.data.get("third_medication_prescriber_phone_number")
      fourth_medication_name = form.data.get("fourth_medication_name")
      fourth_medication_dose = form.data.get("fourth_medication_dose")
      fourth_medication_times = form.data.get("fourth_medication_times")
      fourth_medication_reason_for_taking = form.data.get("fourth_medication_reason_for_taking")
      fourth_medication_prescriber_name = form.data.get("fourth_medication_prescriber_name")
      fourth_medication_prescriber_phone_number = form.data.get("fourth_medication_prescriber_phone_number")
      fifth_medication_name = form.data.get("fifth_medication_name")
      fifth_medication_dose = form.data.get("fifth_medication_dose")
      fifth_medication_times = form.data.get("fifth_medication_times")
      fifth_medication_reason_for_taking = form.data.get("fifth_medication_reason_for_taking")
      fifth_medication_prescriber_name = form.data.get("fifth_medication_prescriber_name")
      fifth_medication_prescriber_phone_number = form.data.get("fifth_medication_prescriber_phone_number")
      sixth_medication_name = form.data.get("sixth_medication_name")
      sixth_medication_dose = form.data.get("sixth_medication_dose")
      sixth_medication_times = form.data.get("sixth_medication_times")
      sixth_medication_reason_for_taking = form.data.get("sixth_medication_reason_for_taking")
      sixth_medication_prescriber_name = form.data.get("sixth_medication_prescriber_name")
      sixth_medication_prescriber_phone_number = form.data.get("sixth_medication_prescriber_phone_number")
      camper_dietary_preference_choices = form.data.get("camper_dietary_preference_choices")
      does_camper_have_any_food_allergies = form.data.get("does_camper_have_any_food_allergies")
      does_camper_have_any_drug_other_allergies = form.data.get("does_camper_have_any_drug_other_allergies")
      camper_physical_health_history_choices = form.data.get("camper_physical_health_history_choices")
      explain_any_other_unlisted_medical_history = form.data.get("explain_any_other_unlisted_medical_history")
      provide_explanation_of_any_checked_medical_history_items = form.data.get("provide_explanation_of_any_checked_medical_history_items")
      does_camper_have_any_physical_activities_to_be_limited_or_restricted = form.data.get("does_camper_have_any_physical_activities_to_be_limited_or_restricted")
      month_and_year_of_diphtheria_or_tetanus_immunization = form.data.get("month_and_year_of_diphtheria_or_tetanus_immunization")
      month_and_year_of_tetanus_booster_immunization = form.data.get("month_and_year_of_tetanus_booster_immunization")
      month_and_year_of_polio_immunization = form.data.get("month_and_year_of_polio_immunization")
      month_and_year_of_rotavirus_immunization = form.data.get("month_and_year_of_rotavirus_immunization")
      month_and_year_of_mumps_measles_or_rubella_immunization = form.data.get("month_and_year_of_mumps_measles_or_rubella_immunization")
      month_and_year_of_hepatitis_a_immunization = form.data.get("month_and_year_of_hepatitis_a_immunization")
      month_and_year_of_hepatitis_b_immunization = form.data.get("month_and_year_of_hepatitis_b_immunization")
      month_and_year_of_varicella_immunization = form.data.get("month_and_year_of_varicella_immunization")
      month_and_year_of_duration_of_chicken_pox = form.data.get("month_and_year_of_duration_of_chicken_pox")
      month_and_year_of_haemophilus_influenza_b_immunization = form.data.get("month_and_year_of_haemophilus_influenza_b_immunization")
      month_and_year_of_seasonal_flu_vaccine_immunization = form.data.get("month_and_year_of_seasonal_flu_vaccine_immunization")
      month_and_year_of_pneumococcal_vaccine_immunization = form.data.get("month_and_year_of_pneumococcal_vaccine_immunization")
      month_and_year_of_human_papillomavirus_immunization = form.data.get("month_and_year_of_human_papillomavirus_immunization")
      month_and_year_of_meningococcal_meningitis_immunization = form.data.get("month_and_year_of_meningococcal_meningitis_immunization")
      month_and_year_of_tuberculin_test = form.data.get("month_and_year_of_tuberculin_test")
      was_tuberculin_test_positive_or_negative = form.data.get("was_tuberculin_test_positive_or_negative")
      any_other_unlisted_immunizations = form.data.get("any_other_unlisted_immunizations")
      camper_mental_health_history_choices = form.data.get("camper_mental_health_history_choices")
      any_other_unlisted_mental_illnesses = form.data.get("any_other_unlisted_mental_illnesses")
      provide_explanation_for_any_checked_mental_illness_items = form.data.get("provide_explanation_for_any_checked_mental_illness_items")
      does_camper_have_any_triggers_to_be_aware_of = form.data.get("does_camper_have_any_triggers_to_be_aware_of")
      does_camper_have_positive_coping_skills_to_use = form.data.get("does_camper_have_positive_coping_skills_to_use")
      guardian_authorized_over_counter_medications_choices = form.data.get("guardian_authorized_over_counter_medications_choices")
      guardian_consent_to_give_over_the_counter_medications = form.data.get("guardian_consent_to_give_over_the_counter_medications")
      guardian_consent_to_health_information_and_treatment_at_ASPYRE = form.data.get("guardian_consent_to_health_information_and_treatment_at_ASPYRE")
      guardian_consent_to_freedom_of_expression_consent = form.data.get("guardian_consent_to_freedom_of_expression_consent")
      guardian_or_18yr_old_consent_to_photo_release = form.data.get("guardian_or_18yr_old_consent_to_photo_release")
      guardian_consent_for_community_values_agreement = form.data.get("guardian_consent_for_community_values_agreement")
      camper_consent_for_community_values_agreement = form.data.get("camper_consent_for_community_values_agreement")
      guardian_consent_for_waiver_to_participate = form.data.get("guardian_consent_for_waiver_to_participate")
      camper_consent_for_waiver_to_participate = form.data.get("camper_consent_for_waiver_to_participate")
      guardian_signed_for_the_entire_form = form.data.get("guardian_signed_for_the_entire_form")
      date_of_guardian_signed_for_the_entire_form = form.data.get("date_of_guardian_signed_for_the_entire_form")
      camper_signed_for_the_entire_form = form.data.get("camper_signed_for_the_entire_form")
      date_of_camper_signed_for_the_entire_form = form.data.get("date_of_camper_signed_for_the_entire_form")
      medicalinformation = MedicalInformation.objects.create(
        user=user,
        age_of_camper=age_of_camper,
        first_guardian_name=first_guardian_name,
        first_guardian_phone_number=first_guardian_phone_number,
        first_guardian_home_work_or_cell=first_guardian_home_work_or_cell,
        second_guardian_name=second_guardian_name,
        second_guardian_phone_number=second_guardian_phone_number,
        second_guardian_home_work_or_cell=second_guardian_home_work_or_cell,
        third_guardian_name=third_guardian_name,
        third_guardian_phone_number=third_guardian_phone_number,
        third_guardian_home_work_or_cell=third_guardian_home_work_or_cell,
        emergency_contact_name=emergency_contact_name,
        emergency_contact_phone_number=emergency_contact_phone_number,
        emergency_home_work_cell=emergency_home_work_cell,
        can_camper_be_picked_up_by_guardian_or_emergency_contact=can_camper_be_picked_up_by_guardian_or_emergency_contact,
        any_unauthorized_persons_that_can_pick_up_camper=any_unauthorized_persons_that_can_pick_up_camper,
        first_authorized_persons_name=first_authorized_persons_name,
        first_authorized_persons_phone=first_authorized_persons_phone,
        second_authorized_persons_name=second_authorized_persons_name,
        second_authorized_persons_phone=second_authorized_persons_phone,
        family_physician_NP_PA_name=family_physician_NP_PA_name,
        family_physician_NP_PA_phone_number=family_physician_NP_PA_phone_number,
        mental_healthcare_provider_name=mental_healthcare_provider_name,
        mental_healthcare_provider_phone_number=mental_healthcare_provider_phone_number,
        will_camper_take_medication_while_at_camp=will_camper_take_medication_while_at_camp,
        first_medication_name=first_medication_name,
        first_medication_dose=first_medication_dose,
        first_medication_times=first_medication_times,
        first_medication_reason_for_taking=first_medication_reason_for_taking,
        first_medication_prescriber_name=first_medication_prescriber_name,
        first_medication_prescriber_phone_number=first_medication_prescriber_phone_number,
        second_medication_name=second_medication_name,
        second_medication_dose=second_medication_dose,
        second_medication_times=second_medication_times,
        second_medication_reason_for_taking=second_medication_reason_for_taking,
        second_medication_prescriber_name=second_medication_prescriber_name,
        second_medication_prescriber_phone_number=second_medication_prescriber_phone_number,
        third_medication_name=third_medication_name,
        third_medication_dose=third_medication_dose,
        third_medication_times=third_medication_times,
        third_medication_reason_for_taking=third_medication_reason_for_taking,
        third_medication_prescriber_name=third_medication_prescriber_name,
        third_medication_prescriber_phone_number=third_medication_prescriber_phone_number,
        fourth_medication_name=fourth_medication_name,
        fourth_medication_dose=fourth_medication_dose,
        fourth_medication_times=fourth_medication_times,
        fourth_medication_reason_for_taking=fourth_medication_reason_for_taking,
        fourth_medication_prescriber_name=fourth_medication_prescriber_name,
        fourth_medication_prescriber_phone_number=fourth_medication_prescriber_phone_number,
        fifth_medication_name=fifth_medication_name,
        fifth_medication_dose=fifth_medication_dose,
        fifth_medication_times=fifth_medication_times,
        fifth_medication_reason_for_taking=fifth_medication_reason_for_taking,
        fifth_medication_prescriber_name=fifth_medication_prescriber_name,
        fifth_medication_prescriber_phone_number=fifth_medication_prescriber_phone_number,
        sixth_medication_name=sixth_medication_name,
        sixth_medication_dose=sixth_medication_dose,
        sixth_medication_times=sixth_medication_times,
        sixth_medication_reason_for_taking=sixth_medication_reason_for_taking,
        sixth_medication_prescriber_name=sixth_medication_prescriber_name,
        sixth_medication_prescriber_phone_number=sixth_medication_prescriber_phone_number,
        camper_dietary_preference_choices=camper_dietary_preference_choices,
        does_camper_have_any_food_allergies=does_camper_have_any_food_allergies,
        does_camper_have_any_drug_other_allergies=does_camper_have_any_drug_other_allergies,
        camper_physical_health_history_choices=camper_physical_health_history_choices,
        explain_any_other_unlisted_medical_history=explain_any_other_unlisted_medical_history,
        provide_explanation_of_any_checked_medical_history_items=provide_explanation_of_any_checked_medical_history_items,
        does_camper_have_any_physical_activities_to_be_limited_or_restricted=does_camper_have_any_physical_activities_to_be_limited_or_restricted,
        month_and_year_of_diphtheria_or_tetanus_immunization=month_and_year_of_diphtheria_or_tetanus_immunization,
        month_and_year_of_tetanus_booster_immunization=month_and_year_of_tetanus_booster_immunization,
        month_and_year_of_polio_immunization=month_and_year_of_polio_immunization,
        month_and_year_of_rotavirus_immunization=month_and_year_of_rotavirus_immunization,
        month_and_year_of_mumps_measles_or_rubella_immunization=month_and_year_of_mumps_measles_or_rubella_immunization,
        month_and_year_of_hepatitis_a_immunization=month_and_year_of_hepatitis_a_immunization,
        month_and_year_of_hepatitis_b_immunization=month_and_year_of_hepatitis_b_immunization,
        month_and_year_of_varicella_immunization=month_and_year_of_varicella_immunization,
        month_and_year_of_duration_of_chicken_pox=month_and_year_of_duration_of_chicken_pox,
        month_and_year_of_haemophilus_influenza_b_immunization=month_and_year_of_haemophilus_influenza_b_immunization,
        month_and_year_of_seasonal_flu_vaccine_immunization=month_and_year_of_seasonal_flu_vaccine_immunization,
        month_and_year_of_pneumococcal_vaccine_immunization=month_and_year_of_pneumococcal_vaccine_immunization,
        month_and_year_of_human_papillomavirus_immunization=month_and_year_of_human_papillomavirus_immunization,
        month_and_year_of_meningococcal_meningitis_immunization=month_and_year_of_meningococcal_meningitis_immunization,
        month_and_year_of_tuberculin_test=month_and_year_of_tuberculin_test,
        was_tuberculin_test_positive_or_negative=was_tuberculin_test_positive_or_negative,
        any_other_unlisted_immunizations=any_other_unlisted_immunizations,
        camper_mental_health_history_choices=camper_mental_health_history_choices,
        any_other_unlisted_mental_illnesses=any_other_unlisted_mental_illnesses,
        provide_explanation_for_any_checked_mental_illness_items=provide_explanation_for_any_checked_mental_illness_items,
        does_camper_have_any_triggers_to_be_aware_of=does_camper_have_any_triggers_to_be_aware_of,
        does_camper_have_positive_coping_skills_to_use=does_camper_have_positive_coping_skills_to_use,
        guardian_authorized_over_counter_medications_choices=guardian_authorized_over_counter_medications_choices,
        guardian_consent_to_give_over_the_counter_medications=guardian_consent_to_give_over_the_counter_medications,
        guardian_consent_to_health_information_and_treatment_at_ASPYRE=guardian_consent_to_health_information_and_treatment_at_ASPYRE,
        guardian_consent_to_freedom_of_expression_consent=guardian_consent_to_freedom_of_expression_consent,
        guardian_or_18yr_old_consent_to_photo_release=guardian_or_18yr_old_consent_to_photo_release,
        guardian_consent_for_community_values_agreement=guardian_consent_for_community_values_agreement,
        camper_consent_for_community_values_agreement=camper_consent_for_community_values_agreement,
        guardian_consent_for_waiver_to_participate=guardian_consent_for_waiver_to_participate,
        camper_consent_for_waiver_to_participate=camper_consent_for_waiver_to_participate,
        guardian_signed_for_the_entire_form=guardian_signed_for_the_entire_form,
        date_of_guardian_signed_for_the_entire_form=date_of_guardian_signed_for_the_entire_form,
        camper_signed_for_the_entire_form=camper_signed_for_the_entire_form,
        date_of_camper_signed_for_the_entire_form=date_of_camper_signed_for_the_entire_form,
      )
      registration = Registration.objects.create(
        user=user,
        medicalinformation=medicalinformation,
        camp=camp,
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
      camper.what_would_camper_change_in_school_or_community = form_data.get("what_would_camper_change_in_school_or_community")
      camper.what_activities_is_the_camper_involved_in = form_data.get("what_activities_is_the_camper_involved_in")
      camper.if_scholarship_not_granted_can_they_pay_camp_cost = form_data.get("if_scholarship_not_granted_can_they_pay_camp_cost")
      camper.camper_has_definite_transportation_if_scholarship_is_granted = form_data.get("camper_has_definite_transportation_if_scholarship_is_granted")
      camper.save()
      return redirect(to='camper_scholarship_form_submitted')
  else:
    form = CamperScholarshipForm(request.user)
  return render(request, 'core/camper_scholarship.html', {'form': form, 'camp': camp})

@login_required
def camper_scholarship_submitted(request):
  return render(request, 'core/scholarship_form_submitted.html')


@login_required
def camper_medical_form_submitted(request):
  return render(request, 'core/camper_medical_form_submitted.html')

