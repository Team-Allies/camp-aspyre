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
    have_disability = models.BooleanField(default=None)
    accommodations = models.CharField(max_length=255, blank=True)
    sponsor_org = models.CharField(max_length=255, blank=True)
    other_companies_paying = models.CharField(max_length=255, blank=True)
    like_to_change = models.CharField(max_length=255, default=None)
    currently_involved_activities = models.CharField(max_length=100, default="")
    no_scholarship = models.CharField(max_length=50, default=None)
    DEFINITE_TRANSPORTATION = (
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Carpool', 'Carpool would be necessary'),
    )
    definite_transportation = models.CharField(choices=DEFINITE_TRANSPORTATION, max_length=50, default=None)
    SCHOLARSHIP_GRANTED = (
    ('Same info as registration form', 'Same information as registration form'),
    ('Other', 'Other'),
    )
    scholarship_granted = models.CharField(choices=SCHOLARSHIP_GRANTED, max_length=50, default=None)

    def __str__(self):
        return self.legal_full_name


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
    
    








