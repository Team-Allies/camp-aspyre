from django import forms
from core.models import User, Camper, Camp
from django.forms import ModelForm

class CamperRegistrationForm(forms.Form):
  ATTENDED_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
  )
  previously_attended = forms.ChoiceField(choices=ATTENDED_CHOICES, widget=forms.RadioSelect())
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
  accomodations = forms.CharField(max_length=255)
  sponsor_org = forms.CharField(max_length=255)


