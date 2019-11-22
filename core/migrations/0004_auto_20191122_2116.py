# Generated by Django 2.2.7 on 2019-11-22 21:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_camper_other_companies_paying'),
    ]

    operations = [
        migrations.RenameField(
            model_name='camper',
            old_name='accomodations',
            new_name='accommodations',
        ),
        migrations.AddField(
            model_name='camper',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
