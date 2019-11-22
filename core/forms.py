from django import forms
from core.models import User, Camper, Camp, MedicalInformation
from django.forms import ModelForm


class CamperRegistrationForm(forms.Form):
  ATTENDED_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
  )
  previously_attended = forms.ChoiceField(choices=ATTENDED_CHOICES)
  legal_full_name = forms.CharField(max_length=100)
  preferred_name = forms.CharField(max_length=255)
  preferred_pronouns = forms.CharField(max_length=255)
  date_of_birth = forms.DateField(widget=forms.SelectDateWidget)
  street_address = forms.CharField(max_length=255) 
  city = forms.CharField(max_length=255)
  state = forms.CharField(max_length=255)
  zip_code = forms.CharField(max_length=255)
  phone_number = forms.CharField(max_length=255)
  email = forms.CharField(max_length=255)
  name_of_school = forms.CharField(max_length=255)
  how_heard_about = forms.CharField(max_length=255)
  facebook = forms.CharField(max_length=255)
  gain_from_camp = forms.CharField(max_length=255)
  dietary_restrictions = forms.CharField(max_length=255)
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
  accommodations = forms.CharField(max_length=255)
  sponsor_org = forms.CharField(max_length=255, required=False)
  other_companies_paying = forms.CharField(max_length=255, required=False)


# class CamperMedicalForm(forms.Form):
#     height = models.CharField(max_length=255)
#     weight = models.IntegerField()
#     biological_sex = models.CharField(max_length=255)
#     full_address = models.CharField(max_length=255)
#     emergency_contact = models.CharField(max_length=255)
#     relationship_to_student = models.CharField(max_length=255)
#     best_phone_number_during_camp = models.CharField(max_length=255)
#     best_phone_number_during_camp_secondary = models.CharField(max_length=255)
#     alternate_contact = models.CharField(max_length=255)
#     doctor_name = models.CharField(max_length=255)
#     doctor_phone = models.CharField(max_length=255)
#     doctor_address = models.CharField(max_length=255)
#     health_insurance_name = models.CharField(max_length=255)
#     insurance_policy_number = models.CharField(max_length=255)
#     other_pertinent_insurance_info = models.CharField(max_length=255)
#     taking_meds = models.BooleanField()
#     nervousness = models.BooleanField()
#     mental_disorder = models.BooleanField()
#     convulsions_epilepsy = models.BooleanField()
#     fainting = models.BooleanField()
#     heart_condition = models.BooleanField()
#     rheumatic_fever = models.BooleanField()
#     cancer_tumor = models.BooleanField()
#     high_blood_pressure = models.BooleanField()
#     headaches = models.BooleanField()
#     asthma = models.BooleanField()
#     ulcers = models.BooleanField()
#     diabetes = models.BooleanField()
#     medication_allergies = models.BooleanField()
#     other_allergies_illnesses = models.BooleanField()
#     physical_limitations = models.CharField(max_length=255)
#     details_answers = models.CharField(max_length=255)
