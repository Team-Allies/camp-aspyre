import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse 
from django import forms

# Create your models here.


class User(AbstractUser):
    roles = models.ManyToManyField(to='Role')


class Role(models.Model):

    PARENT = 1
    NURSE = 2
    GENERAL_STAFF = 3
    ADMIN = 4
    ROLE_CHOICES = (
        (PARENT,  'Parent'),
        (NURSE, 'Nurse'),
        (GENERAL_STAFF, 'General Staff'),
        (ADMIN, 'Admin Staff'),
    )

    id = models.PositiveIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class Registration(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    camper = models.ForeignKey(to='Camper', on_delete=models.CASCADE)
    camp = models.ForeignKey(to='Camp', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.camper.legal_full_name

class Camper(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    ATTENDED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    previously_attended = models.CharField(choices=ATTENDED_CHOICES, max_length=10)
    legal_full_name = models.CharField(max_length=255)
    preferred_name = models.CharField(max_length=255)
    preferred_pronouns = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    street_address = models.CharField(max_length=255) 
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    name_of_school = models.CharField(max_length=255)
    how_heard_about = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    gain_from_camp = models.CharField(max_length=255)
    dietary_restrictions = models.CharField(max_length=255)
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
    verify_sensitive_topics = models.BooleanField()
    have_disability = models.BooleanField(blank=True, null=True)
    accommodations = models.CharField(max_length=255, blank=True)
    sponsor_org = models.CharField(max_length=255, blank=True)
    other_companies_paying = models.CharField(max_length=255, blank=True)
    like_to_change = models.CharField(max_length=255)
    currently_involved_activities = models.CharField(max_length=100, blank=True, null=True)
    if_scholarship_not_granted = models.CharField(max_length=50, blank=True, null=True)
    DEFINITE_TRANSPORTATION = (
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Carpool', 'Carpool would be necessary'),
    )
    
    definite_transportation = models.CharField(choices=DEFINITE_TRANSPORTATION, max_length=50, blank=True, null=True)
                                           
    def __str__(self):
        return f"{self.legal_full_name} ({self.preferred_name})"


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
    # Section 1
    legal_full_name = models.CharField(max_length=255)
    preferred_name = models.CharField(max_length=255)
    camper_age = models.CharField(max_length=255)
    parent_guardian_name = models.CharField(max_length=255)
    parent_guardian_phone_number = models.CharField(max_length=255)
    HOME_WORK_CELL = (
        ('Home', 'Home'), 
        ('Work', 'Work'), 
        ('Cell', 'Cell'),
    )
    home_work_cell = forms.ChoiceField(choices=HOME_WORK_CELL, widget=forms.RadioSelect())
    parent_guardian_name_second = models.CharField(max_length=255)
    parent_guardian_phone_number_second = models.CharField(max_length=255)
    HOME_WORK_CELL_SECOND = (
        ('Home', 'Home'),
        ('Work', 'Work'),
        ('Cell', 'Cell'),
    )
    home_work_cell_second = forms.ChoiceField(choices=HOME_WORK_CELL_SECOND, widget=forms.RadioSelect())
    parent_guardian_name_third = models.CharField(max_length=255)
    parent_guardian_phone_number_third = models.CharField(max_length=255)
    HOME_WORK_CELL_THIRD = (
        ('Home', 'Home'),
        ('Work', 'Work'),
        ('Cell', 'Cell'),
    )
    home_work_cell_third = forms.ChoiceField(choices=HOME_WORK_CELL_THIRD, widget=forms.RadioSelect())
    emergency_contact_name = models.CharField(max_length=255)
    emergency_contact_phone_number = models.CharField(max_length=255)
    HOME_WORK_CELL_EMERGENCY = (
        ('Home', 'Home'),
        ('Work', 'Work'),
        ('Cell', 'Cell'),
    )
    home_work_cell_emergency = forms.ChoiceField(choices=HOME_WORK_CELL_EMERGENCY, widget=forms.RadioSelect())
    picked_up_by_guardian_or_emergency_contact = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    picked_up_by_guardian_or_emergency_contact = forms.ChoiceField(choices=picked_up_by_guardian_or_emergency_contact, widget=forms.RadioSelect())
    unauthorized_to_pick_up = models.CharField(max_length=255)
    authorizing_pick_up_name = models.CharField(max_length=255)
    authorizing_pick_up_phone = models.CharField(max_length=255)
    authorizing_pick_up_name_second = models.CharField(max_length=255)
    authorizing_pick_up_phone_second = models.CharField(max_length=255)
    mental_health_provider_name = models.CharField(max_length=255)
    mental_health_provider_phone_number = models.CharField(max_length=255)
    # Section 2
    MEDICATION_YES_OR_NO = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    medication_yes_or_no = forms.ChoiceField(choices=MEDICATION_YES_OR_NO, widget=forms.RadioSelect())
    medication_name = models.CharField(max_length=255)
    medication_dose = models.CharField(max_length=255)
    medication_times = models.CharField(max_length=255)
    medication_reason = models.CharField(max_length=255)
    medication_prescriber_name = models.CharField(max_length=255)
    medication_prescriber_phone_number = models.CharField(max_length=255)
    medication_name_2 = models.CharField(max_length=255)
    medication_dose_2 = models.CharField(max_length=255)
    medication_times_2 = models.CharField(max_length=255)
    medication_reason_2 = models.CharField(max_length=255)
    medication_prescriber_name_2 = models.CharField(max_length=255)
    medication_prescriber_phone_number_2 = models.CharField(max_length=255)
    medication_name_3 = models.CharField(max_length=255)
    medication_dose_3 = models.CharField(max_length=255)
    medication_times_3 = models.CharField(max_length=255)
    medication_reason_3 = models.CharField(max_length=255)
    medication_prescriber_name_3 = models.CharField(max_length=255)
    medication_prescriber_phone_number_3 = models.CharField(max_length=255)
    medication_name_4 = models.CharField(max_length=255)
    medication_dose_4 = models.CharField(max_length=255)
    medication_times_4 = models.CharField(max_length=255)
    medication_reason_4 = models.CharField(max_length=255)
    medication_prescriber_name_4 = models.CharField(max_length=255)
    medication_prescriber_phone_number_4 = models.CharField(max_length=255)
    medication_name_5 = models.CharField(max_length=255)
    medication_dose_5 = models.CharField(max_length=255)
    medication_times_5 = models.CharField(max_length=255)
    medication_reason_5 = models.CharField(max_length=255)
    medication_prescriber_name_5 = models.CharField(max_length=255)
    medication_prescriber_phone_number_5 = models.CharField(max_length=255)
    medication_name_6 = models.CharField(max_length=255)
    medication_dose_6 = models.CharField(max_length=255)
    medication_times_6 = models.CharField(max_length=255)
    medication_reason_6 = models.CharField(max_length=255)
    medication_prescriber_name_6 = models.CharField(max_length=255)
    medication_prescriber_phone_number_6 = models.CharField(max_length=255)
    # Section 3
    vegetarian = models.BooleanField()
    vegan = models.BooleanField()
    dairy_free = models.BooleanField()
    nut_free = models.BooleanField()
    gluten_free = models.BooleanField()
    food_allergies = models.BooleanField()
    drug_other_allergies = models.CharField(max_length=255)
    # Section 4
    recent_injury_illness_disease = models.BooleanField()
    illness = models.BooleanField()
    asthma = models.BooleanField()
    dysmenorrhea = models.BooleanField()
    ear_infection = models.BooleanField()
    seizure_convulsions = models.BooleanField()
    dizziness_during_exercise = models.BooleanField()
    chest_pain_during_exercise = models.BooleanField()
    heart_defect_disease = models.BooleanField()
    hypertension = models.BooleanField()
    bleeding_clotting_disorder = models.BooleanField()
    diabetes = models.BooleanField()
    mononucleosis = models.BooleanField()
    chicken_pox = models.BooleanField()
    measles = models.BooleanField()
    german_measles = models.BooleanField()
    mumps = models.BooleanField()
    tuberculosis = models.BooleanField()
    joint_problems = models.BooleanField()
    fractures = models.BooleanField()
    headaches = models.BooleanField()
    head_injury =models.BooleanField()
    eating_disorder = models.BooleanField()
    diarrhea_constipation = models.BooleanField()
    stomach_aches = models.BooleanField()
    glasses_or_contacts = models.BooleanField()
    hospitalized_surgery = models.BooleanField()
    medic_alert_id = models.BooleanField()
    other = models.BooleanField()
    other_explain = models.CharField(max_length=255)
    number_and_explanation = models.CharField(max_length=255)
    physical_activities_restricted = models.CharField(max_length=255)
    diphtheria_or_tetanus = models.CharField(max_length=255)
    tetanus_booster = models.CharField(max_length=255)
    polio = models.CharField(max_length=255)
    rotavirus = models.CharField(max_length=255)
    mumps_measles_rubella = models.CharField(max_length=255)
    hepatitis_a = models.CharField(max_length=255)
    hepatitis_b = models.CharField(max_length=255)
    varicella = models.CharField(max_length=255)
    chicken_pox_when = models.CharField(max_length=255)
    haemophilus_influenza_b = models.CharField(max_length=255)
    seasonal_flu_vaccine = models.CharField(max_length=255)
    pneumococcal_vaccine = models.CharField(max_length=255)
    human_papillomavirus = models.CharField(max_length=255)
    meningococcal_miningitis = models.CharField(max_length=255)
    tuberculin_test = models.CharField(max_length=255)
    other = models.CharField(max_length=255)
    # Section 5
    eating_disorders = models.BooleanField()
    add_adhd = models.BooleanField()
    audio_visual_hallucinations = models.BooleanField()
    ptsd = models.BooleanField()
    gender_dysphoria = models.BooleanField()
    significant_life_event = models.BooleanField()
    sexual_assault_violence = models.BooleanField()
    depression = models.BooleanField()
    obsessive_compulsive_disorder = models.BooleanField()
    panic_attacks = models.BooleanField()
    anxiety = models.BooleanField()
    mental_verbal_abuse = models.BooleanField()
    physical_abuse = models.BooleanField()
    trouble_sleeping = models.BooleanField()
    other = models.CharField(max_length=255)
    number_and_explanation = models.CharField(max_length=255)
    triggers = models.CharField(max_length=255)
    coping_skills = models.CharField(max_length=255)
    # Section 6
    acetaminophen = models.BooleanField()
    ibuprofen = models.BooleanField()
    diphenhydramine = models.BooleanField()
    bismuth_subsalicylate = models.BooleanField()
    calcium_carbonate = models.BooleanField()
    polyethylene_glycol = models.BooleanField()
    bacitracin = models.BooleanField()
    all_of_the_above = models.BooleanField()
    no_over_the_counter_meds = models.BooleanField()
    agreed = models.BooleanField()

    def __str__(self):
        return self.legal_full_name 


