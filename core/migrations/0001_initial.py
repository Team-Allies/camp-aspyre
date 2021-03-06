# Generated by Django 2.2.7 on 2019-11-26 15:58

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_camp', models.CharField(max_length=255)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('street_address_location', models.CharField(max_length=255)),
                ('city_location', models.CharField(max_length=255)),
                ('time_of_arrival', models.TimeField()),
                ('time_of_departure', models.TimeField()),
                ('meeting_place_for_carpool', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Camper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previously_attended', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('legal_full_name', models.CharField(max_length=255)),
                ('preferred_name', models.CharField(max_length=255)),
                ('preferred_pronouns', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField(default=datetime.date.today)),
                ('street_address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('name_of_school', models.CharField(max_length=255)),
                ('how_heard_about', models.CharField(max_length=255)),
                ('facebook', models.CharField(max_length=255)),
                ('gain_from_camp', models.CharField(max_length=255)),
                ('dietary_restrictions', models.CharField(max_length=255)),
                ('tshirt_size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', '2XL'), ('XXXL', '3XL')], max_length=5)),
                ('verify_sensitive_topics', models.BooleanField()),
                ('have_disability', models.BooleanField(default=None)),
                ('accommodations', models.CharField(blank=True, max_length=255)),
                ('sponsor_org', models.CharField(blank=True, max_length=255)),
                ('other_companies_paying', models.CharField(blank=True, max_length=255)),
                ('like_to_change', models.CharField(default=None, max_length=255)),
                ('currently_involved_activities', models.CharField(default='', max_length=100)),
                ('no_scholarship', models.CharField(default=None, max_length=50)),
                ('definite_transportation', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Carpool', 'Carpool would be necessary')], default='No', max_length=50)),
                ('scholarship_granted', models.CharField(choices=[('Same info as registration form', 'Same information as registration form'), ('Other', 'Other')], default=None, max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveIntegerField(choices=[(1, 'Parent'), (2, 'Nurse'), (3, 'General Staff'), (4, 'Admin Staff')], primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('camp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Camp')),
                ('camper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Camper')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_full_name', models.CharField(max_length=255)),
                ('preferred_name', models.CharField(max_length=255)),
                ('camper_age', models.CharField(max_length=255)),
                ('parent_guardian_name', models.CharField(max_length=255)),
                ('parent_guardian_phone_number', models.CharField(max_length=255)),
                ('parent_guardian_name_second', models.CharField(max_length=255)),
                ('parent_guardian_phone_number_second', models.CharField(max_length=255)),
                ('parent_guardian_name_third', models.CharField(max_length=255)),
                ('parent_guardian_phone_number_third', models.CharField(max_length=255)),
                ('emergency_contact_name', models.CharField(max_length=255)),
                ('emergency_contact_phone_number', models.CharField(max_length=255)),
                ('unauthorized_to_pick_up', models.CharField(max_length=255)),
                ('authorizing_pick_up_name', models.CharField(max_length=255)),
                ('authorizing_pick_up_phone', models.CharField(max_length=255)),
                ('authorizing_pick_up_name_second', models.CharField(max_length=255)),
                ('authorizing_pick_up_phone_second', models.CharField(max_length=255)),
                ('mental_health_provider_name', models.CharField(max_length=255)),
                ('mental_health_provider_phone_number', models.CharField(max_length=255)),
                ('medication_name', models.CharField(max_length=255)),
                ('medication_dose', models.CharField(max_length=255)),
                ('medication_times', models.CharField(max_length=255)),
                ('medication_reason', models.CharField(max_length=255)),
                ('medication_prescriber_name', models.CharField(max_length=255)),
                ('medication_prescriber_phone_number', models.CharField(max_length=255)),
                ('medication_name_2', models.CharField(max_length=255)),
                ('medication_dose_2', models.CharField(max_length=255)),
                ('medication_times_2', models.CharField(max_length=255)),
                ('medication_reason_2', models.CharField(max_length=255)),
                ('medication_prescriber_name_2', models.CharField(max_length=255)),
                ('medication_prescriber_phone_number_2', models.CharField(max_length=255)),
                ('medication_name_3', models.CharField(max_length=255)),
                ('medication_dose_3', models.CharField(max_length=255)),
                ('medication_times_3', models.CharField(max_length=255)),
                ('medication_reason_3', models.CharField(max_length=255)),
                ('medication_prescriber_name_3', models.CharField(max_length=255)),
                ('medication_prescriber_phone_number_3', models.CharField(max_length=255)),
                ('medication_name_4', models.CharField(max_length=255)),
                ('medication_dose_4', models.CharField(max_length=255)),
                ('medication_times_4', models.CharField(max_length=255)),
                ('medication_reason_4', models.CharField(max_length=255)),
                ('medication_prescriber_name_4', models.CharField(max_length=255)),
                ('medication_prescriber_phone_number_4', models.CharField(max_length=255)),
                ('medication_name_5', models.CharField(max_length=255)),
                ('medication_dose_5', models.CharField(max_length=255)),
                ('medication_times_5', models.CharField(max_length=255)),
                ('medication_reason_5', models.CharField(max_length=255)),
                ('medication_prescriber_name_5', models.CharField(max_length=255)),
                ('medication_prescriber_phone_number_5', models.CharField(max_length=255)),
                ('medication_name_6', models.CharField(max_length=255)),
                ('medication_dose_6', models.CharField(max_length=255)),
                ('medication_times_6', models.CharField(max_length=255)),
                ('medication_reason_6', models.CharField(max_length=255)),
                ('medication_prescriber_name_6', models.CharField(max_length=255)),
                ('medication_prescriber_phone_number_6', models.CharField(max_length=255)),
                ('vegetarian', models.BooleanField()),
                ('vegan', models.BooleanField()),
                ('dairy_free', models.BooleanField()),
                ('nut_free', models.BooleanField()),
                ('gluten_free', models.BooleanField()),
                ('food_allergies', models.BooleanField()),
                ('drug_other_allergies', models.CharField(max_length=255)),
                ('recent_injury_illness_disease', models.BooleanField()),
                ('illness', models.BooleanField()),
                ('asthma', models.BooleanField()),
                ('dysmenorrhea', models.BooleanField()),
                ('ear_infection', models.BooleanField()),
                ('seizure_convulsions', models.BooleanField()),
                ('dizziness_during_exercise', models.BooleanField()),
                ('chest_pain_during_exercise', models.BooleanField()),
                ('heart_defect_disease', models.BooleanField()),
                ('hypertension', models.BooleanField()),
                ('bleeding_clotting_disorder', models.BooleanField()),
                ('diabetes', models.BooleanField()),
                ('mononucleosis', models.BooleanField()),
                ('chicken_pox', models.BooleanField()),
                ('measles', models.BooleanField()),
                ('german_measles', models.BooleanField()),
                ('mumps', models.BooleanField()),
                ('tuberculosis', models.BooleanField()),
                ('joint_problems', models.BooleanField()),
                ('fractures', models.BooleanField()),
                ('headaches', models.BooleanField()),
                ('head_injury', models.BooleanField()),
                ('eating_disorder', models.BooleanField()),
                ('diarrhea_constipation', models.BooleanField()),
                ('stomach_aches', models.BooleanField()),
                ('glasses_or_contacts', models.BooleanField()),
                ('hospitalized_surgery', models.BooleanField()),
                ('medic_alert_id', models.BooleanField()),
                ('other_explain', models.CharField(max_length=255)),
                ('physical_activities_restricted', models.CharField(max_length=255)),
                ('diphtheria_or_tetanus', models.CharField(max_length=255)),
                ('tetanus_booster', models.CharField(max_length=255)),
                ('polio', models.CharField(max_length=255)),
                ('rotavirus', models.CharField(max_length=255)),
                ('mumps_measles_rubella', models.CharField(max_length=255)),
                ('hepatitis_a', models.CharField(max_length=255)),
                ('hepatitis_b', models.CharField(max_length=255)),
                ('varicella', models.CharField(max_length=255)),
                ('chicken_pox_when', models.CharField(max_length=255)),
                ('haemophilus_influenza_b', models.CharField(max_length=255)),
                ('seasonal_flu_vaccine', models.CharField(max_length=255)),
                ('pneumococcal_vaccine', models.CharField(max_length=255)),
                ('human_papillomavirus', models.CharField(max_length=255)),
                ('meningococcal_miningitis', models.CharField(max_length=255)),
                ('tuberculin_test', models.CharField(max_length=255)),
                ('eating_disorders', models.BooleanField()),
                ('add_adhd', models.BooleanField()),
                ('audio_visual_hallucinations', models.BooleanField()),
                ('ptsd', models.BooleanField()),
                ('gender_dysphoria', models.BooleanField()),
                ('significant_life_event', models.BooleanField()),
                ('sexual_assault_violence', models.BooleanField()),
                ('depression', models.BooleanField()),
                ('obsessive_compulsive_disorder', models.BooleanField()),
                ('panic_attacks', models.BooleanField()),
                ('anxiety', models.BooleanField()),
                ('mental_verbal_abuse', models.BooleanField()),
                ('physical_abuse', models.BooleanField()),
                ('trouble_sleeping', models.BooleanField()),
                ('other', models.CharField(max_length=255)),
                ('number_and_explanation', models.CharField(max_length=255)),
                ('triggers', models.CharField(max_length=255)),
                ('coping_skills', models.CharField(max_length=255)),
                ('acetaminophen', models.BooleanField()),
                ('ibuprofen', models.BooleanField()),
                ('diphenhydramine', models.BooleanField()),
                ('bismuth_subsalicylate', models.BooleanField()),
                ('calcium_carbonate', models.BooleanField()),
                ('polyethylene_glycol', models.BooleanField()),
                ('bacitracin', models.BooleanField()),
                ('all_of_the_above', models.BooleanField()),
                ('no_over_the_counter_meds', models.BooleanField()),
                ('agreed', models.BooleanField()),
                ('camper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Camper')),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Registration')),
            ],
        ),
        migrations.AddField(
            model_name='camp',
            name='campers',
            field=models.ManyToManyField(through='core.Registration', to='core.Camper'),
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(to='core.Role'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
