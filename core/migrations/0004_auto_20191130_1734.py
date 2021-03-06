# Generated by Django 2.2.7 on 2019-11-30 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191127_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='camper',
            old_name='accommodations',
            new_name='any_additional_accommodations_needed',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='definite_transportation',
            new_name='camper_has_definite_transportation_if_scholarship_is_granted',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='city',
            new_name='city_of_camper',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='date_of_birth',
            new_name='date_of_birth_of_camper',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='dietary_restrictions',
            new_name='does_camper_have_any_dietary_restrictions',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='other_companies_paying',
            new_name='does_the_camper_have_any_disabilities',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='sponsor_org',
            new_name='does_the_camper_have_any_sponsoring_organizations',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='email',
            new_name='email_of_camper',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='previously_attended',
            new_name='has_camper_previously_attended_ASPYRE',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='verify_sensitive_topics',
            new_name='has_the_camper_verified_that_sensitive_topics_will_be_covered',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='facebook',
            new_name='how_did_the_camper_hear_about_the_camp',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='if_scholarship_not_granted',
            new_name='if_scholarship_not_granted_can_they_pay_camp_cost',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='gain_from_camp',
            new_name='legal_full_name_of_camper',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='how_heard_about',
            new_name='phone_number_of_camper',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='legal_full_name',
            new_name='preferred_name_of_camper',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='like_to_change',
            new_name='preferred_pronouns_of_camper',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='phone_number',
            new_name='state_of_camper',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='preferred_name',
            new_name='street_address_of_camper',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='currently_involved_activities',
            new_name='what_activities_is_the_camper_involved_in',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='preferred_pronouns',
            new_name='what_does_the_camper_want_to_gain_from_the_camp',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='state',
            new_name='what_would_camper_change_in_school_or_community',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='street_address',
            new_name='would_the_camper_like_to_be_added_facebook',
        ),
        migrations.RenameField(
            model_name='camper',
            old_name='zip_code',
            new_name='zip_code_of_camper',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='authorizing_pick_up_name',
            new_name='any_other_unlisted_immunizations',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='authorizing_pick_up_name_second',
            new_name='any_physical_activities_to_be_limited_or_restricted',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='authorizing_pick_up_phone',
            new_name='any_unauthorized_persons_that_can_pick_up_camper',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='acetaminophen',
            new_name='camper_consent_for_community_values_agreement',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='add_adhd',
            new_name='camper_consent_for_waiver_to_participate',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='agreed',
            new_name='camper_signed_for_the_entire_form',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='authorizing_pick_up_phone_second',
            new_name='does_camper_have_any_drug_other_allergies',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='all_of_the_above',
            new_name='does_camper_have_any_food_allergies',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='camper_age',
            new_name='does_camper_have_any_triggers_to_be_aware_of',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='chicken_pox_when',
            new_name='does_camper_have_positive_coping_skills_to_use',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='coping_skills',
            new_name='explain_any_other_unlisted_medical_history',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='diphtheria_or_tetanus',
            new_name='family_physician_NP_PA_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='drug_other_allergies',
            new_name='family_physician_NP_PA_phone_number',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='haemophilus_influenza_b',
            new_name='fifth_medication_dose',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='hepatitis_a',
            new_name='fifth_medication_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='hepatitis_b',
            new_name='fifth_medication_prescriber_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='human_papillomavirus',
            new_name='fifth_medication_prescriber_phone_number',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='legal_full_name',
            new_name='fifth_medication_reason_for_taking',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_dose',
            new_name='fifth_medication_times',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_dose_2',
            new_name='first_authorized_persons_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_dose_3',
            new_name='first_authorized_persons_phone',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_dose_4',
            new_name='first_guardian_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_dose_5',
            new_name='first_guardian_phone_number',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_dose_6',
            new_name='first_medication_dose',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_name',
            new_name='first_medication_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_name_2',
            new_name='first_medication_prescriber_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_name_3',
            new_name='first_medication_prescriber_phone_number',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_name_4',
            new_name='first_medication_reason_for_taking',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_name_5',
            new_name='first_medication_times',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_name_6',
            new_name='fourth_medication_dose',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_prescriber_name',
            new_name='fourth_medication_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_prescriber_name_2',
            new_name='fourth_medication_prescriber_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_prescriber_name_4',
            new_name='fourth_medication_prescriber_phone_number',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_prescriber_name_3',
            new_name='fourth_medication_reason_for_taking',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_prescriber_name_5',
            new_name='fourth_medication_times',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='anxiety',
            new_name='guardian_consent_for_community_values_agreement',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='asthma',
            new_name='guardian_consent_for_waiver_to_participate',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='audio_visual_hallucinations',
            new_name='guardian_consent_to_freedom_of_expression_consent',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='bacitracin',
            new_name='guardian_consent_to_give_over_the_counter_medications',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='bismuth_subsalicylate',
            new_name='guardian_consent_to_health_information_and_treatment_at_ASPYRE',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='bleeding_clotting_disorder',
            new_name='guardian_signed_for_the_entire_form',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_prescriber_phone_number',
            new_name='mental_healthcare_provider_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_prescriber_name_6',
            new_name='mental_healthcare_provider_phone_number',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_prescriber_phone_number_2',
            new_name='month_and_year_of_diphtheria_or_tetanus_immunization',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_prescriber_phone_number_3',
            new_name='month_and_year_of_duration_of_chicken_pox',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_prescriber_phone_number_4',
            new_name='month_and_year_of_haemophilus_influenza_b_immunization',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_prescriber_phone_number_5',
            new_name='month_and_year_of_hepatitis_a_immunization',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_prescriber_phone_number_6',
            new_name='month_and_year_of_hepatitis_b_immunization',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_reason',
            new_name='month_and_year_of_human_papillomavirus_immunization',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_reason_3',
            new_name='month_and_year_of_meningococcal_meningitis_immunization',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_reason_2',
            new_name='month_and_year_of_mumps_measles_or_rubella_immunization',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_reason_4',
            new_name='month_and_year_of_pneumococcal_vaccine_immunization',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_reason_5',
            new_name='month_and_year_of_polio_immunization',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_reason_6',
            new_name='month_and_year_of_rotavirus_immunization',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_times',
            new_name='month_and_year_of_seasonal_flu_vaccine_immunization',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_times_3',
            new_name='month_and_year_of_tetanus_booster_immunization',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_times_2',
            new_name='month_and_year_of_tuberculin_test',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_times_4',
            new_name='month_and_year_of_varicella_immunization',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_times_5',
            new_name='provide_explanation_for_any_checked_mental_illness_items',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='medication_times_6',
            new_name='provide_explanation_of_any_checked_medical_history_items',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='meningococcal_miningitis',
            new_name='second_authorized_persons_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='mental_health_provider_phone_number',
            new_name='second_authorized_persons_phone',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='mental_health_provider_name',
            new_name='second_guardian_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='mumps_measles_rubella',
            new_name='second_guardian_phone_number',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='number_and_explanation',
            new_name='second_medication_dose',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='other',
            new_name='second_medication_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='other_explain',
            new_name='second_medication_prescriber_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='parent_guardian_name',
            new_name='second_medication_prescriber_phone_number',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='parent_guardian_name_second',
            new_name='second_medication_reason_for_taking',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='parent_guardian_name_third',
            new_name='second_medication_times',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='parent_guardian_phone_number',
            new_name='sixth_medication_dose',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='parent_guardian_phone_number_second',
            new_name='sixth_medication_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='parent_guardian_phone_number_third',
            new_name='sixth_medication_prescriber_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='physical_activities_restricted',
            new_name='sixth_medication_prescriber_phone_number',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='pneumococcal_vaccine',
            new_name='sixth_medication_reason_for_taking',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='polio',
            new_name='sixth_medication_times',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='preferred_name',
            new_name='third_guardian_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='rotavirus',
            new_name='third_guardian_phone_number',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='tetanus_booster',
            new_name='third_medication_dose',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='seasonal_flu_vaccine',
            new_name='third_medication_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='triggers',
            new_name='third_medication_prescriber_name',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='tuberculin_test',
            new_name='third_medication_prescriber_phone_number',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='unauthorized_to_pick_up',
            new_name='third_medication_reason_for_taking',
        ),
        migrations.RenameField(
            model_name='medicalinformation',
            old_name='varicella',
            new_name='third_medication_times',
        ),
        migrations.RemoveField(
            model_name='camper',
            name='have_disability',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='calcium_carbonate',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='chest_pain_during_exercise',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='chicken_pox',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='dairy_free',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='depression',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='diabetes',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='diarrhea_constipation',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='diphenhydramine',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='dizziness_during_exercise',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='dysmenorrhea',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='ear_infection',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='eating_disorder',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='eating_disorders',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='food_allergies',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='fractures',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='gender_dysphoria',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='german_measles',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='glasses_or_contacts',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='gluten_free',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='head_injury',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='headaches',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='heart_defect_disease',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='hospitalized_surgery',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='hypertension',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='ibuprofen',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='illness',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='joint_problems',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='measles',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='medic_alert_id',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='mental_verbal_abuse',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='mononucleosis',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='mumps',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='no_over_the_counter_meds',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='nut_free',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='obsessive_compulsive_disorder',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='panic_attacks',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='physical_abuse',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='polyethylene_glycol',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='ptsd',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='recent_injury_illness_disease',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='seizure_convulsions',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='sexual_assault_violence',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='significant_life_event',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='stomach_aches',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='trouble_sleeping',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='tuberculosis',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='vegan',
        ),
        migrations.RemoveField(
            model_name='medicalinformation',
            name='vegetarian',
        ),
        migrations.AddField(
            model_name='camper',
            name='does_the_camper_have_other_companies_paying',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='medicalinformation',
            name='date_of_camper_signed_for_the_entire_form',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='medicalinformation',
            name='date_of_guardian_signed_for_the_entire_form',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='medicalinformation',
            name='guardian_or_18yr_old_consent_to_photo_release',
            field=models.BooleanField(null=True),
        ),
    ]
