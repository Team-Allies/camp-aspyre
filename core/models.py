from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse 

# Create your models here.

class User(AbstractUser):
    camp = models.ForeignKey(to='Camp', on_delete=models.CASCADE)

    is_admin_staff = models.BooleanField(default=False)

    is_parent = models.BooleanField(default=False)

    is_nurse = models.BooleanField(default=False)

    is_volunteer = models.BooleanField(default=False)

    is_general_staff = models.BooleanField(default=False)

class Camper(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    
    previously_attended = models.BooleanField()
    legal_full_name = models.CharField(max_length=255)
    preferred_name = models.CharField(max_length=255)
    preferred_pronouns = models.CharField(max_length=255)
    date_of_birth = models.IntegerField
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
    tshirt_size_choices = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', '2XL'),
        ('XXXL', '3XL'),
    ]
    tshirt_size = models.CharField(max_length=5, choices=tshirt_size_choices)
    verify_sensitive_topics = models.BooleanField()
    accomodations = models.CharField(max_length=255, blank=True)
    sponsor_org = models.CharField(max_length=255, blank=True)

class Camp (models.Model):
    camper = models.ManyToManyField(to='Camper')

    name_of_camp = models.CharField(max_length=255)
    # dates =
    street_address_location = models.CharField(max_length=255)
    city_location = models.CharField(max_length=255)
    # look this up later
    time_of_arrival = models.CharField(max_length=255)
    time_of_departure = models.CharField(max_length=255)
    meeting_place_for_carpool = models.CharField(max_length=255)





