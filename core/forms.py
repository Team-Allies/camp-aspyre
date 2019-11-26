from django import forms
from core.models import User, Camper, Camp, MedicalInformation
from django.forms import ModelForm


class CamperRegistrationForm(forms.Form):
  ATTENDED_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
  )
  previously_attended = forms.ChoiceField(choices=ATTENDED_CHOICES)
  legal_full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  preferred_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  preferred_pronouns = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  date_of_birth = forms.DateField(widget=forms.SelectDateWidget)
  street_address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'})) 
  city = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  state = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  zip_code = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  phone_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  email = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  name_of_school = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  how_heard_about = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  facebook = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  gain_from_camp = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  dietary_restrictions = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  TSHIRT_SIZE_CHOICES = (
      ('XS', 'XS'),
      ('S', 'S'),
      ('M', 'M'),
      ('L', 'L'),
      ('XL', 'XL'),
      ('XXL', '2XL'),
      ('XXXL', '3XL'),
  )
  tshirt_size = forms.ChoiceField(choices=TSHIRT_SIZE_CHOICES)
  verify_sensitive_topics = forms.BooleanField()
  accommodations = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  sponsor_org = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  other_companies_paying = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class':'text_field_input'}))

class CamperScholarshipForm(forms.Form):
  legal_full_name = forms.CharField(max_length=100)
  preferred_name = forms.CharField(max_length=255)
  email = forms.CharField(max_length=255)
  like_to_change = forms.CharField(max_length=255)
  currently_involved_activities = forms.CharField(max_length=100)
  no_scholarship = forms.CharField(max_length=50)
  DEFINITE_TRANSPORTATION = (
  ('Yes', 'Yes'),
  ('No', 'No'),
  ('Carpool', 'Carpool would be necessary')
  )
  definite_transportation = forms.ChoiceField(choices=DEFINITE_TRANSPORTATION, widget=forms.RadioSelect())
  SCHOLARSHIP_GRANTED = (
  ('Same info as registration form', 'Same information as registration form'),
  ('Other', 'Other')
  )
  scholarship_granted = forms.ChoiceField(choices=SCHOLARSHIP_GRANTED, widget=forms.RadioSelect())


class CamperMedicalForm(forms.Form):
  date_of_birth = forms.DateField(widget=forms.SelectDateWidget)
  height = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  weight = forms.IntegerField()
  biological_sex = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  full_address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  emergency_contact = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  relationship_to_student = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  best_phone_number_during_camp = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  best_phone_number_during_camp_secondary = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  alternate_contact = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  doctor_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  doctor_phone = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  doctor_address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  health_insurance_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  insurance_policy_number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  other_pertinent_insurance_info = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  taking_meds = forms.BooleanField()
  nervousness = forms.BooleanField()
  mental_disorder = forms.BooleanField()
  convulsions_epilepsy = forms.BooleanField()
  fainting = forms.BooleanField()
  heart_condition = forms.BooleanField()
  rheumatic_fever = forms.BooleanField()
  cancer_tumor = forms.BooleanField()
  high_blood_pressure = forms.BooleanField()
  headaches = forms.BooleanField()
  asthma = forms.BooleanField()
  ulcers = forms.BooleanField()
  diabetes = forms.BooleanField()
  medication_allergies = forms.BooleanField()
  other_allergies_illnesses = forms.BooleanField()
  physical_limitations = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
  details_answers = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'text_field_input'}))
