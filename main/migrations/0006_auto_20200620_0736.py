# Generated by Django 3.0.3 on 2020-06-20 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200620_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recognition',
            name='rec_img',
            field=models.ImageField(default='', upload_to='main/img/'),
        ),
    ]