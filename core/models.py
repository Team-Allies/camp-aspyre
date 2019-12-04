from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse 
from django import forms
import datetime

# Create your models here.


class User(AbstractUser):
    roles = models.ManyToManyField(to='Role')


class Role(models.Model):

    PARENT = 1
    NURSE = 2
    GENERAL_STAFF = 3
    ADMIN = 4
    ROLE_CHOICES = [
        (PARENT,  'Parent'),
        (NURSE, 'Nurse'),
        (GENERAL_STAFF, 'General Staff'),
        (ADMIN, 'Admin Staff'),
    ]

    id = models.PositiveIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class Registration(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    camper = models.ForeignKey(to='Camper', on_delete=models.CASCADE)
    camp = models.ForeignKey(to='Camp', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.camper.legal_full_name_of_camper

class Camper(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    ATTENDED_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    has_camper_previously_attended_ASPYRE = models.CharField(max_length=10, choices=ATTENDED_CHOICES)
    legal_full_name_of_camper = models.CharField(max_length=255)
    preferred_name_of_camper = models.CharField(max_length=255)
    preferred_pronouns_of_camper = models.CharField(max_length=255)
    date_of_birth_of_camper = models.DateField()
    street_address_of_camper = models.CharField(max_length=255) 
    city_of_camper = models.CharField(max_length=255)
    state_of_camper = models.CharField(max_length=255)
    zip_code_of_camper = models.CharField(max_length=255)
    phone_number_of_camper = models.CharField(max_length=255)
    email_of_camper = models.CharField(max_length=255)
    name_of_school = models.CharField(max_length=255)
    how_did_the_camper_hear_about_the_camp = models.CharField(max_length=255)
    would_the_camper_like_to_be_added_facebook = models.CharField(max_length=255)
    what_does_the_camper_want_to_gain_from_the_camp = models.CharField(max_length=255)
    does_camper_have_any_dietary_restrictions = models.CharField(max_length=255)
    does_the_camper_have_any_disabilities = models.CharField(max_length=255, blank=True)
    any_additional_accommodations_needed = models.CharField(max_length=255, blank=True)
    does_the_camper_have_any_sponsoring_organizations = models.CharField(max_length=255, blank=True)
    TSHIRT_SIZE_CHOICES = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', '2XL'),
        ('XXXL', '3XL'),
    ]
    tshirt_size = models.CharField(max_length=5, choices=TSHIRT_SIZE_CHOICES)
    has_the_camper_verified_that_sensitive_topics_will_be_covered = models.BooleanField()
    does_the_camper_have_other_companies_paying = models.CharField(max_length=255, blank=True)
    what_would_camper_change_in_school_or_community = models.CharField(max_length=255)
    what_activities_is_the_camper_involved_in = models.CharField(max_length=100, blank=True, null=True)
    if_scholarship_not_granted_can_they_pay_camp_cost = models.CharField(max_length=50, blank=True, null=True)
    DEFINITE_TRANSPORTATION = [
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Carpool', 'Carpool would be necessary'),
    ]
    camper_has_definite_transportation_if_scholarship_is_granted = models.CharField(choices=DEFINITE_TRANSPORTATION, max_length=50, blank=True, null=True)
                                           
    def __str__(self):
        return f"{self.legal_full_name_of_camper} ({self.preferred_name_of_camper})"


class Camp(models.Model):
    campers = models.ManyToManyField(to='Camper', through='Registration')
    name_of_camp = models.CharField(max_length=255)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    street_address_location = models.CharField(max_length=255)
    city_location = models.CharField(max_length=255)
    time_of_arrival = models.TimeField()
    time_of_departure = models.TimeField()
    meeting_place_for_carpool = models.CharField(max_length=255)

    def number_of_campers(self):
        return self.campers.count()
    def __str__(self):
        return self.name_of_camp 


class MedicalInformation(models.Model):
    registration = models.ForeignKey(to='Registration', on_delete=models.CASCADE)
    camper = models.ForeignKey(to='Camper', on_delete=models.CASCADE)

    #|=====| Section 1 - BASIC CONTACT INFO |=====|#

    first_guardian_name = models.CharField(max_length=255)
    first_guardian_phone_number = models.CharField(max_length=255)
    FIRST_GUARDIAN_HOME_WORK_CELL = [
        ('Home', 'Home'), 
        ('Work', 'Work'), 
        ('Cell', 'Cell'),
    ]
    first_guardian_home_work_or_cell = models.ChoiceField(choices=FIRST_GUARDIAN_HOME_WORK_CELL, widget=forms.RadioSelect())
    second_guardian_name = models.CharField(max_length=255)
    second_guardian_phone_number = models.CharField(max_length=255)
    SECOND_GUARDIAN_HOME_WORK_CELL = [
        ('Home', 'Home'),
        ('Work', 'Work'),
        ('Cell', 'Cell'),
    ]
    second_guardian_home_work_or_cell = models.ChoiceField(choices=SECOND_GUARDIAN_HOME_WORK_CELL, widget=forms.RadioSelect()) 
    third_guardian_name = models.CharField(max_length=255)
    third_guardian_phone_number = models.CharField(max_length=255)
    THIRD_GUARDIAN_HOME_WORK_CELL = [
        ('Home', 'Home'),
        ('Work', 'Work'),
        ('Cell', 'Cell'),
    ]
    third_guardian_home_work_or_cell = models.ChoiceField(choices=THIRD_GUARDIAN_HOME_WORK_CELL, widget=forms.RadioSelect())
    emergency_contact_name = models.CharField(max_length=255)
    emergency_contact_phone_number = models.CharField(max_length=255)
    EMERGENCY_CONTACT_HOME_WORK_CELL = (
        ('Home', 'Home'),
        ('Work', 'Work'),
        ('Cell', 'Cell'),
    )
    emergency_home_work_cell = models.ChoiceField(choices=EMERGENCY_CONTACT_HOME_WORK_CELL, widget=forms.RadioSelect())
    CAN_BE_PICKED_UP_BY_GUARDIAN_OR_EMERGENCY_CONTACT = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    can_camper_be_picked_up_by_guardian_or_emergency_contact = models.ChoiceField(choices=CAN_BE_PICKED_UP_BY_GUARDIAN_OR_EMERGENCY_CONTACT, widget=forms.RadioSelect())
    any_unauthorized_persons_that_can_pick_up_camper = models.CharField(max_length=255)
    first_authorized_persons_name = models.CharField(max_length=255)
    first_authorized_persons_phone = models.CharField(max_length=255)
    second_authorized_persons_name = models.CharField(max_length=255)
    second_authorized_persons_phone = models.CharField(max_length=255)
    family_physician_NP_PA_name = models.CharField(max_length=255)
    family_physician_NP_PA_phone_number = models.CharField(max_length=255)
    mental_healthcare_provider_name = models.CharField(max_length=255)
    mental_healthcare_provider_phone_number = models.CharField(max_length=255)
    
#|=====| Section 2 - MEDICATIONS |=====|#

    will_camper_take_medication_while_at_camp = models.BooleanField(widget=forms.RadioSelect())
    first_medication_name = models.CharField(max_length=255)
    first_medication_dose = models.CharField(max_length=255)
    first_medication_times = models.CharField(max_length=255)
    first_medication_reason_for_taking = models.CharField(max_length=255)
    first_medication_prescriber_name = models.CharField(max_length=255)
    first_medication_prescriber_phone_number = models.CharField(max_length=255)
    
    second_medication_name = models.CharField(max_length=255)
    second_medication_dose = models.CharField(max_length=255)
    second_medication_times = models.CharField(max_length=255)
    second_medication_reason_for_taking = models.CharField(max_length=255)
    second_medication_prescriber_name = models.CharField(max_length=255)
    second_medication_prescriber_phone_number = models.CharField(max_length=255)
    
    third_medication_name = models.CharField(max_length=255)
    third_medication_dose = models.CharField(max_length=255)
    third_medication_times = models.CharField(max_length=255)
    third_medication_reason_for_taking = models.CharField(max_length=255)
    third_medication_prescriber_name = models.CharField(max_length=255)
    third_medication_prescriber_phone_number = models.CharField(max_length=255)
    
    fourth_medication_name = models.CharField(max_length=255)
    fourth_medication_dose = models.CharField(max_length=255)
    fourth_medication_times = models.CharField(max_length=255)
    fourth_medication_reason_for_taking = models.CharField(max_length=255)
    fourth_medication_prescriber_name = models.CharField(max_length=255)
    fourth_medication_prescriber_phone_number = models.CharField(max_length=255)

    fifth_medication_name = models.CharField(max_length=255)
    fifth_medication_dose = models.CharField(max_length=255)
    fifth_medication_times = models.CharField(max_length=255)
    fifth_medication_reason_for_taking = models.CharField(max_length=255)
    fifth_medication_prescriber_name = models.CharField(max_length=255)
    fifth_medication_prescriber_phone_number = models.CharField(max_length=255)

    sixth_medication_name = models.CharField(max_length=255)
    sixth_medication_dose = models.CharField(max_length=255)
    sixth_medication_times = models.CharField(max_length=255)
    sixth_medication_reason_for_taking = models.CharField(max_length=255)
    sixth_medication_prescriber_name = models.CharField(max_length=255)
    sixth_medication_prescriber_phone_number = models.CharField(max_length=255)

#|=====| Section 3 - DIETARY PREFERENCES/ALLERGIES |=====|#

    DIETARY_PREFERENCE_CHOICES = [
        ('Vegetarian','Vegetarian'),
        ('Vegan','Vegan'),
        ('Dairy-free','Dairy-free'),
        ('Nut-free','Nut-free'),
        ('Gluten-free','Gluten-free'),
    ]
    camper_dietary_preference_choices = models.MultipleChoiceField(choices=DIETARY_PREFERENCE_CHOICES, widget=forms.RadioSelect())
    does_camper_have_any_food_allergies = models.BooleanField()
    does_camper_have_any_drug_other_allergies = models.CharField(max_length=255)

#|=====| Section 4 - PHYSICAL HEALTHY/IMMUNIZATIONS |=====|#

    CAMPER_PHYSICAL_HEALTH_HISTORY_CHOICES = [
        ('recent_injury_,_illness_or_infectious_disease', 'recent_injury_,_illness_or_infectious_disease'),
        ('chronic_or_recurring_illness', 'chronic_or_recurring_illness'),
        ('asthma', 'asthma'),
        ('dysmenorrhea', 'dysmenorrhea'),
        ('frequent_ear_infections', 'frequent_ear_infections'),
        ('seizure_disorders_or_convulsions', 'seizure_disorders_or_convulsions'),
        ('dizziness_during_or_after_exercise', 'dizziness_during_or_after_exercise'),
        ('chest_pain_during_or_after_exercise', 'chest_pain_during_or_after_exercise'),
        ('heart_defect_/_disease', 'heart_defect_/_disease'),
        ('hypertension', 'hypertension'),
        ('bleeding_/_clotting_disorder', 'bleeding_/_clotting_disorder'),
        ('diabetes', 'diabetes'),
        ('mononucleosis_(_in_last_12_months_)', 'mononucleosis_(_in_last_12_months_)'),
        ('chicken_pox', 'chicken_pox'),
        ('measles', 'measles'),
        ('german_measles', 'german_measles'),
        ('mumps', 'mumps'),
        ('tuberculosis', 'tuberculosis'),
        ('hepatitis', 'hepatitis'),
        ('joint_problems', 'joint_problems'),
        ('fractures', 'fractures'),
        ('frequent_headaches', 'frequent_headaches'),
        ('head_injury', 'head_injury'),
        ('eating_disorder', 'eating_disorder'),
        ('diarrhea_or_constipation', 'diarrhea_or_constipation'),
        ('frequent_stomach_aches', 'frequent_stomach_aches'),
        ('wearing_glasses_or_contacts', 'wearing_glasses_or_contacts'),
        ('surgery_or_being_hospitalized', 'surgery_or_being_hospitalized'),
        ('wearing_medic_alert_id', 'wearing_medic_alert_id'),
        ('other_unlisted_medical_history', 'other_unlisted_medical_history'),
    ]
    camper_physical_health_history_choices = models.MultipleChoiceField(choices=CAMPER_PHYSICAL_HEALTH_HISTORY_CHOICES, widget=forms.RadioSelect())
    explain_any_other_unlisted_medical_history = models.CharField(blank=True, null=True, max_length=255)
    provide_explanation_of_any_checked_medical_history_items = models.CharField(max_length=255)
    any_physical_activities_to_be_limited_or_restricted = models.CharField(max_length=255)
    month_and_year_of_diphtheria_or_tetanus_immunization = models.CharField(max_length=255)
    month_and_year_of_tetanus_booster_immunization = models.CharField(max_length=255)
    month_and_year_of_polio_immunization = models.CharField(max_length=255)
    month_and_year_of_rotavirus_immunization = models.CharField(max_length=255)
    month_and_year_of_mumps_measles_or_rubella_immunization = models.CharField(max_length=255)
    month_and_year_of_hepatitis_a_immunization = models.CharField(max_length=255)
    month_and_year_of_hepatitis_b_immunization = models.CharField(max_length=255)
    month_and_year_of_varicella_immunization = models.CharField(max_length=255)
    month_and_year_of_duration_of_chicken_pox = models.CharField(max_length=255)
    month_and_year_of_haemophilus_influenza_b_immunization = models.CharField(max_length=255)
    month_and_year_of_seasonal_flu_vaccine_immunization = models.CharField(max_length=255)
    month_and_year_of_pneumococcal_vaccine_immunization = models.CharField(max_length=255)
    month_and_year_of_human_papillomavirus_immunization = models.CharField(max_length=255)
    month_and_year_of_meningococcal_meningitis_immunization = models.CharField(max_length=255)
    month_and_year_of_tuberculin_test = models.CharField(max_length=255)
    TUBERCULIN_TEST_POSITIVE_OR_NEGATIVE = [
      ('Yes, it was Positive', 'Yes, it was Positive'),
      ('No, it was Negative', 'No, it was Negative'),
    ]
    was_tuberculin_test_positive_or_negative = models.ChoiceField(choices=TUBERCULIN_TEST_POSITIVE_OR_NEGATIVE, widget=forms.RadioSelect())
    any_other_unlisted_immunizations = models.CharField(max_length=255)

#|=====| Section 5 - MENTAL HEALTH HISTORY |=====|#
    MENTAL_HEALTH_HISTORY_CHOICES = [
        ('any_eating_disorders', 'any_eating_disorders'),
        ('add_or_adhd', 'add_or_adhd'),
        ('any_audio_visual_hallucinations', 'any_audio_visual_hallucinations'),
        ('ptsd', 'ptsd'),
        ('gender_dysphoria', 'gender_dysphoria'),
        ('any_significant_life_event_that_continues_to_affect_camper', 'any_significant_life_event_that_continues_to_affect_camper'),
        ('any_sexual_assault_or_sexual_violence', 'any_sexual_assault_or_sexual_violence'),
        ('depression', 'depression'),
        ('obsessive_compulsive_disorder', 'obsessive_compulsive_disorder'),
        ('any_panic_attacks', 'any_panic_attacks'),
        ('anxiety', 'anxiety'),
        ('any_mental_or_verbal_abuse', 'any_mental_or_verbal_abuse'),
        ('any_physical_abuse', 'any_physical_abuse'),
        ('any_trouble_sleeping_or_sleep_disorders', 'any_trouble_sleeping_or_sleep_disorders'),
    ]
    camper_mental_health_history_choices = models.MultipleChoiceField(choices=MENTAL_HEALTH_HISTORY_CHOICES, widget=forms.RadioSelect())
    provide_explanation_for_any_checked_mental_illness_items = models.CharField(blank=True, null=True, max_length=255)
    does_camper_have_any_triggers_to_be_aware_of = models.CharField(max_length=255)
    does_camper_have_positive_coping_skills_to_use = models.CharField(max_length=255)

#|=====| Section 6 - AUTHORIZATIONS |=====|#
    
    AUTHORIZED_OVER_COUNTER_MEDICATIONS_CHOICES = [
        ('acetaminophen', 'acetaminophen'),
        ('ibuprofen', 'ibuprofen'),
        ('diphenhydramine', 'diphenhydramine'),
        ('bismuth_subsalicylate', 'bismuth_subsalicylate'),
        ('calcium_carbonate', 'calcium_carbonate'),
        ('polyethylene_glycol', 'polyethylene_glycol'),
        ('bacitracin', 'bacitracin'),
        ('I_consent_for_all_of_the_above', 'I_consent_for_all_of_the_above'),
        ('I_do_not_want_any_over_the_counter_medications_to_be_given', 'I_do_not_want_any_over_the_counter_medications_to_be_given'),
    ]
    guardian_authorized_over_counter_medications_choices = models.MultipleChoiceField(choices=AUTHORIZED_OVER_COUNTER_MEDICATIONS_CHOICES, widget=forms.RadioSelect())
    guardian_consent_to_give_over_the_counter_medications = models.BooleanField()
    guardian_consent_to_health_information_and_treatment_at_ASPYRE = models.BooleanField()
    guardian_consent_to_freedom_of_expression_consent = models.BooleanField()
    guardian_or_18yr_old_consent_to_photo_release = models.BooleanField(null=True)

#|=====| Section 7 - COMMUNITY VALUES AGREEMENT |=====|#

    guardian_consent_for_community_values_agreement = models.BooleanField()

#|=====| Section 8 - PARENT/GUARDIAN AND PARTICIPANT RELEASE |=====|#

    guardian_consent_for_waiver_to_participate = models.BooleanField()

    # guardian_signed_for_the_entire_form = models.BooleanField()
    # date_of_guardian_signed_for_the_entire_form = models.DateField(null=True)
    
    # camper_signed_for_the_entire_form = models.BooleanField()
    # date_of_camper_signed_for_the_entire_form = models.DateField(null=True)

    def __str__(self):
        return self.legal_full_name_of_camper


