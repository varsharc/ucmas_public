# Generated by Django 3.0.3 on 2020-06-09 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200609_0355'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='section_body',
            field=models.TextField(default='<text here>'),
        ),
    ]