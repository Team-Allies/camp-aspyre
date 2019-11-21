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


class Registration (models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    camper = models.ForeignKey(to='Camper', on_delete=models.CASCADE)
    camp = models.ForeignKey(to='Camp', on_delete=models.CASCADE)


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
    accomodations = models.CharField(max_length=255, blank=True)
    sponsor_org = models.CharField(max_length=255, blank=True)


class Camp (models.Model):
    campers = models.ManyToManyField(to='Camper', through='Registration')

    name_of_camp = models.CharField(max_length=255)
    # dates =
    street_address_location = models.CharField(max_length=255)
    city_location = models.CharField(max_length=255)
    # look this up later
    time_of_arrival = models.CharField(max_length=255)
    time_of_departure = models.CharField(max_length=255)
    meeting_place_for_carpool = models.CharField(max_length=255)










