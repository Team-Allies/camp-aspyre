import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse 

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
    date_of_birth = models.DateField(default=datetime.date.today)
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
    accommodations = models.CharField(max_length=255, blank=True)
    sponsor_org = models.CharField(max_length=255, blank=True)
    other_companies_paying = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.legal_full_name


class MedicalInformation(models.Model):
    registration = models.ForeignKey(to='Registration', on_delete=models.CASCADE)
    camper = models.ForeignKey(to='Camper', on_delete=models.CASCADE)

    height = models.CharField(max_length=255)
    weight = models.IntegerField()
    biological_sex = models.CharField(max_length=255)
    full_address = models.CharField(max_length=255)
    emergency_contact = models.CharField(max_length=255)
    relationship_to_student = models.CharField(max_length=255)
    best_phone_number_during_camp = models.CharField(max_length=255)
    best_phone_number_during_camp_secondary = models.CharField(max_length=255)
    alternate_contact = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255)
    doctor_phone = models.CharField(max_length=255)
    doctor_address = models.CharField(max_length=255)
    health_insurance_name = models.CharField(max_length=255)
    insurance_policy_number = models.CharField(max_length=255)
    other_pertinent_insurance_info = models.CharField(max_length=255)
    taking_meds = models.BooleanField()
    nervousness = models.BooleanField()
    mental_disorder = models.BooleanField()
    convulsions_epilepsy = models.BooleanField()
    fainting = models.BooleanField()
    heart_condition = models.BooleanField()
    rheumatic_fever = models.BooleanField()
    cancer_tumor = models.BooleanField()
    high_blood_pressure = models.BooleanField()
    headaches = models.BooleanField()
    asthma = models.BooleanField()
    ulcers = models.BooleanField()
    diabetes = models.BooleanField()
    medication_allergies = models.BooleanField()
    other_allergies_illnesses = models.BooleanField()
    physical_limitations = models.CharField(max_length=255)
    details_answers = models.CharField(max_length=255)
    
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










