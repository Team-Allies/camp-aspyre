from django import forms
from core.models import User, Camper, Camp, MedicalInformation
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CamperRegistrationForm(forms.Form):
  ATTENDED_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
  )
  has_camper_previously_attended_ASPYRE = forms.ChoiceField(choices=ATTENDED_CHOICES, widget=forms.RadioSelect(attrs={'class':'radio_field_input'}))
  legal_full_name_of_camper = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  preferred_name_of_camper = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  preferred_pronouns_of_camper = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  date_of_birth_of_camper = forms.DateField(widget = forms.DateInput(attrs={'type':'date', 'class':'date_field_input'}))
  street_address_of_camper = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'})) 
  city_of_camper = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  state_of_camper = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  zip_code_of_camper = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  phone_number_of_camper = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  email_of_camper = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  name_of_school = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  how_did_the_camper_hear_about_the_camp = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  would_the_camper_like_to_be_added_facebook = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  what_does_the_camper_want_to_gain_from_the_camp = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  does_camper_have_any_dietary_restrictions = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  does_the_camper_have_any_disabilities = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  any_additional_accommodations_needed = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  does_the_camper_have_any_sponsoring_organizations = forms.CharField(max_length=255, required=False, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  TSHIRT_SIZE_CHOICES = (
      ('XS', 'XS'),
      ('S', 'S'),
      ('M', 'M'),
      ('L', 'L'),
      ('XL', 'XL'),
      ('XXL', '2XL'),
      ('XXXL', '3XL'),
  )
  tshirt_size = forms.ChoiceField(choices=TSHIRT_SIZE_CHOICES, widget=forms.RadioSelect(attrs={'class':'radio_field_input'}))
  has_the_camper_verified_that_sensitive_topics_will_be_covered = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'boolean_field_input'}))
  does_the_camper_have_other_companies_paying = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))

class CamperScholarshipForm(forms.Form):
  camper = forms.ModelChoiceField(queryset=Camper.objects.all())
  what_would_camper_change_in_school_or_community = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  what_activities_is_the_camper_involved_in = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  if_scholarship_not_granted_can_they_pay_camp_cost = forms.CharField(max_length=50, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  DEFINITE_TRANSPORTATION = (
  ('Yes', 'Yes'),
  ('No', 'No'),
  ('Carpool', 'Carpool would be necessary')
  )
  camper_has_definite_transportation_if_scholarship_is_granted = forms.ChoiceField(choices=DEFINITE_TRANSPORTATION, widget=forms.RadioSelect(attrs={'class':'radio_field_input'}))

  def __init__(self, user, *args, **kwargs):
    super(CamperScholarshipForm, self).__init__(*args, **kwargs)
    self.fields['camper'].queryset=Camper.objects.filter(user=user)


class CamperMedicalForm(forms.Form):

#|=====| Section 1 - BASIC CONTACT INFO |=====|#

  first_guardian_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  first_guardian_phone_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  FIRST_GUARDIAN_HOME_WORK_CELL = (
      ('Home', 'Home'), 
      ('Work', 'Work'), 
      ('Cell', 'Cell'),
  )
  first_guardian_home_work_or_cell = forms.ChoiceField(choices=FIRST_GUARDIAN_HOME_WORK_CELL, widget=forms.RadioSelect(attrs={'class':'radio_field_input'}))
  second_guardian_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  second_guardian_phone_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  SECOND_GUARDIAN_HOME_WORK_CELL = (
      ('Home', 'Home'),
      ('Work', 'Work'),
      ('Cell', 'Cell'),
  )
  second_guardian_home_work_or_cell = forms.ChoiceField(choices=SECOND_GUARDIAN_HOME_WORK_CELL, widget=forms.RadioSelect(attrs={'class':'radio_field_input'}))
  third_guardian_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  third_guardian_phone_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  THIRD_GUARDIAN_HOME_WORK_CELL = (
      ('Home', 'Home'),
      ('Work', 'Work'),
      ('Cell', 'Cell'),
  )
  third_guardian_home_work_or_cell = forms.ChoiceField(choices=THIRD_GUARDIAN_HOME_WORK_CELL, widget=forms.RadioSelect(attrs={'class':'radio_field_input'}))
  emergency_contact_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  emergency_contact_phone_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  EMERGENCY_CONTACT_HOME_WORK_CELL = (
      ('Home', 'Home'),
      ('Work', 'Work'),
      ('Cell', 'Cell'),
  )
  emergency_home_work_cell = forms.ChoiceField(choices=EMERGENCY_CONTACT_HOME_WORK_CELL, widget=forms.RadioSelect(attrs={'class':'radio_field_input'}))
  CAN_BE_PICKED_UP_BY_GUARDIAN_OR_EMERGENCY_CONTACT = (
      ('Yes', 'Yes'),
      ('No', 'No'),
  )
  can_camper_be_picked_up_by_guardian_or_emergency_contact = forms.ChoiceField(choices=CAN_BE_PICKED_UP_BY_GUARDIAN_OR_EMERGENCY_CONTACT, widget=forms.RadioSelect(attrs={'class':'radio_field_input'}))
  any_unauthorized_persons_that_can_pick_up_camper = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  first_authorized_persons_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  first_authorized_persons_phone = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  second_authorized_persons_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  second_authorized_persons_phone = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  family_physician_NP_PA_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  family_physician_NP_PA_phone_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  mental_healthcare_provider_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  mental_healthcare_provider_phone_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  
#|=====| Section 2 - MEDICATIONS |=====|#

  TAKING_MEDICATION_WHILE_AT_CAMP_YES_OR_NO = (
      ('Yes', 'Yes'),
      ('No', 'No'),
  )
  will_camper_take_medication_while_at_camp = forms.ChoiceField(choices=TAKING_MEDICATION_WHILE_AT_CAMP_YES_OR_NO, widget=forms.RadioSelect(attrs={'class':'radio_field_input'}))
  
  first_medication_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  first_medication_dose = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  first_medication_times = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  first_medication_reason_for_taking = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  first_medication_prescriber_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  first_medication_prescriber_phone_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  
  second_medication_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  second_medication_dose = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  second_medication_times = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  second_medication_reason_for_taking = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  second_medication_prescriber_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  second_medication_prescriber_phone_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  
  third_medication_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  third_medication_dose = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  third_medication_times = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  third_medication_reason_for_taking = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  third_medication_prescriber_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  third_medication_prescriber_phone_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  
  fourth_medication_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  fourth_medication_dose = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  fourth_medication_times = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  fourth_medication_reason_for_taking = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  fourth_medication_prescriber_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  fourth_medication_prescriber_phone_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))

  fifth_medication_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  fifth_medication_dose = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  fifth_medication_times = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  fifth_medication_reason_for_taking = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  fifth_medication_prescriber_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  fifth_medication_prescriber_phone_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))

  sixth_medication_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  sixth_medication_dose = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  sixth_medication_times = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  sixth_medication_reason_for_taking = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  sixth_medication_prescriber_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  sixth_medication_prescriber_phone_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))

#|=====| Section 3 - DIETARY PREFERENCES/ALLERGIES |=====|#
  DIETARY_PREFERENCE_CHOICES = (
    ('Vegetarian','Vegetarian'),
    ('Vegan','Vegan'),
    ('Dairy-free','Dairy-free'),
    ('Nut-free','Nut-free'),
    ('Gluten-free','Gluten-free'),
  )
  camper_dietary_preference_choices = forms.ChoiceField(choices=DIETARY_PREFERENCE_CHOICES, widget=forms.RadioSelect(attrs={'class':'radio_field_input'}))
  does_camper_have_any_food_allergies = forms.CharField(widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  does_camper_have_any_drug_other_allergies = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))

#|=====| Section 4 - PHYSICAL HEALTH HISTORY/IMMUNIZATIONS |=====|#

  CAMPER_PHYSICAL_HEALTH_HISTORY_CHOICES = (
    ('recent injury , illness or infectious disease', 'recent injury , illness or infectious disease'),
    ('chronic or recurring illness', 'chronic or recurring illness'),
    ('asthma', 'asthma'),
    ('dysmenorrhea', 'dysmenorrhea'),
    ('frequent ear infections', 'frequent ear infections'),
    ('seizure disorders or convulsions', 'seizure disorders or convulsions'),
    ('dizziness during or after exercise', 'dizziness during or after exercise'),
    ('chest pain during or after exercise', 'chest pain during or after exercise'),
    ('heart defect / disease', 'heart defect / disease'),
    ('hypertension', 'hypertension'),
    ('bleeding / clotting disorder', 'bleeding / clotting disorder'),
    ('diabetes', 'diabetes'),
    ('mononucleosis ( in last 12 months )', 'mononucleosis ( in last 12 months )'),
    ('chicken pox', 'chicken pox'),
    ('measles', 'measles'),
    ('german measles', 'german measles'),
    ('mumps', 'mumps'),
    ('tuberculosis', 'tuberculosis'),
    ('hepatitis', 'hepatitis'),
    ('joint problems', 'joint problems'),
    ('fractures', 'fractures'),
    ('frequent headaches', 'frequent headaches'),
    ('head injury', 'head injury'),
    ('eating disorder', 'eating disorder'),
    ('diarrhea or constipation', 'diarrhea or constipation'),
    ('frequent stomach aches', 'frequent stomach aches'),
    ('wearing glasses or contacts', 'wearing glasses or contacts'),
    ('surgery or being hospitalized', 'surgery or being hospitalized'),
    ('wearing medic alert id', 'wearing medic alert id'),
    ('other unlisted medical history', 'other unlisted medical history'),
  )
  camper_physical_health_history_choices = forms.ChoiceField(choices=CAMPER_PHYSICAL_HEALTH_HISTORY_CHOICES, widget=forms.RadioSelect(attrs={'class':'radio_field_input'}))
  explain_any_other_unlisted_medical_history = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  provide_explanation_of_any_checked_medical_history_items = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  does_camper_have_any_physical_activities_to_be_limited_or_restricted = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  month_and_year_of_diphtheria_or_tetanus_immunization = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  month_and_year_of_tetanus_booster_immunization = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  month_and_year_of_polio_immunization = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  month_and_year_of_rotavirus_immunization = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  month_and_year_of_mumps_measles_or_rubella_immunization = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  month_and_year_of_hepatitis_a_immunization = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  month_and_year_of_hepatitis_b_immunization = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  month_and_year_of_varicella_immunization = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  month_and_year_of_duration_of_chicken_pox = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  month_and_year_of_haemophilus_influenza_b_immunization = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  month_and_year_of_seasonal_flu_vaccine_immunization = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  month_and_year_of_pneumococcal_vaccine_immunization = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  month_and_year_of_human_papillomavirus_immunization = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  month_and_year_of_meningococcal_meningitis_immunization = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  month_and_year_of_tuberculin_test = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  TUBERCULIN_TEST_POSITIVE_OR_NEGATIVE = (
    ('Yes, it was Positive', 'Yes, it was Positive'),
    ('No, it was Negative', 'No, it was Negative'),
  )
  was_tuberculin_test_positive_or_negative = forms.ChoiceField(choices=TUBERCULIN_TEST_POSITIVE_OR_NEGATIVE, widget=forms.RadioSelect(attrs={'class':'radio_field_input'}))
  any_other_unlisted_immunizations = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))

#|=====| Section 5 - MENTAL HEALTH HISTORY |=====|#

  MENTAL_HEALTH_HISTORY_CHOICES = ( 
    ('any eating disorders', 'any eating disorders'),
    ('add or adhd', 'add or adhd'),
    ('any audio visual hallucinations', 'any audio visual hallucinations'),
    ('ptsd', 'ptsd'),
    ('gender dysphoria', 'gender dysphoria'),
    ('any significant life event that continues to affect camper', 'any significant life event that continues to affect camper'),
    ('any sexual assault or sexual violence', 'any sexual assault or sexual violence'),
    ('depression', 'depression'),
    ('obsessive compulsive disorder', 'obsessive compulsive disorder'),
    ('any panic attacks', 'any panic attacks'),
    ('anxiety', 'anxiety'),
    ('any mental or verbal abuse', 'any mental or verbal abuse'),
    ('any physical abuse', 'any physical abuse'),
    ('any trouble sleeping or sleep disorders', 'any trouble sleeping or sleep disorders'),
  )
  camper_mental_health_history_choices = forms.ChoiceField(choices=MENTAL_HEALTH_HISTORY_CHOICES, widget=forms.RadioSelect(attrs={'class':'radio_field_input'}))
  any_other_unlisted_mental_illnesses = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  provide_explanation_for_any_checked_mental_illness_items = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))
  does_camper_have_any_triggers_to_be_aware_of = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'text_field_input'}))
  does_camper_have_positive_coping_skills_to_use = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class':'textarea_field_input'}))

#|=====| Section 6 - AUTHORIZATIONS |=====|#
  
  AUTHORIZED_OVER_COUNTER_MEDICATIONS_CHOICES = (
    ('Acetaminophen (Tylenol) - fever, pain', 'Acetaminophen (Tylenol) - fever, pain'),
    ('Ibuprofen (Advil) - fever, pain', 'Ibuprofen (Advil) - fever, pain'),
    ('Diphenhydramine (Benadryl) - antihistamine', 'Diphenhydramine (Benadryl) - antihistamine'),
    ('Bismuth Subsalicylate (Pepto Bismol) - heartburn, indigestion, nausea', 'Bismuth Subsalicylate (Pepto Bismol) - heartburn, indigestion, nausea'),
    ('Calcium Carbonate (Tums) - heartburn, indigestion', 'Calcium Carbonate (Tums) - heartburn, indigestion'),
    ('Polyethylene Glycol (Miralax) - laxative', 'Polyethylene Glycol (Miralax) - laxative'),
    ('Bacitracin (Neosporin) - antibiotic ointment', 'Bacitracin (Neosporin) - antibiotic ointment for cuts, scrapes, minor burns'),
    ('I consent for all of the above', 'I consent for all of the above'),
    ('I do not want any over the counter medications to be given', 'I do not want any over the counter medications to be given'),
  )
  guardian_authorized_over_counter_medications_choices = forms.ChoiceField(choices=AUTHORIZED_OVER_COUNTER_MEDICATIONS_CHOICES, widget=forms.RadioSelect(attrs={'class':'radio_field_input'}))

  guardian_consent_to_give_over_the_counter_medications = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'boolean_field_input'}))

  guardian_consent_to_health_information_and_treatment_at_ASPYRE = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'boolean_field_input'}))
  
  guardian_consent_to_freedom_of_expression_consent = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'boolean_field_input'}))

  guardian_or_18yr_old_consent_to_photo_release = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'boolean_field_input'}))

#|=====| Section 7 - COMMUNITY VALUES AGREEMENT |=====|#

  guardian_consent_for_community_values_agreement = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'boolean_field_input'}))
  camper_consent_for_community_values_agreement = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'boolean_field_input'}))

#|=====| Section 8 - PARENT/GUARDIAN AND PARTICIPANT RELEASE |=====|#

  guardian_consent_for_waiver_to_participate = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'boolean_field_input'}))
  camper_consent_for_waiver_to_participate = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'boolean_field_input'}))  

  guardian_signed_for_the_entire_form = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'boolean_field_input'}))
  date_of_guardian_signed_for_the_entire_form = forms.DateField(widget = forms.DateInput(attrs={'type':'date', 'class':'date_field_input'}))

  camper_signed_for_the_entire_form = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'boolean_field_input'}))
  date_of_camper_signed_for_the_entire_form = forms.DateField(widget = forms.DateInput(attrs={'type':'date', 'class':'date_field_input'}))
