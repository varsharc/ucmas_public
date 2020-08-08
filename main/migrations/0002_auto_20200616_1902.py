# Generated by Django 3.0.3 on 2020-06-16 19:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='phone',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Please share a valid 10 digit mobile number', regex='^\\d{10}$')]),
        ),
    ]