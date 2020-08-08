from django.db import models
from django import forms
from PIL import Image
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.core.validators import RegexValidator

#from django.forms import ModelForm

# Create your models here.
class recognition(models.Model):
    rec_title = models.CharField(max_length=140)
    rec_subtitle = models.CharField(max_length=255)
    rec_content = models.TextField(default="<text here>")
    rec_type = models.CharField(max_length=140)
    rec_img = models.ImageField(default="", upload_to='static/main/img/', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.rec_title

class enquiry(models.Model):
    parent_name = models.CharField(default="", max_length=100)
    student_name = models.CharField(default="", max_length=100)
    email = models.EmailField(default="", help_text='A valid email address, please.')
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Please share a valid 10 digit mobile number")
    phone = models.CharField(validators=[phone_regex], max_length=10,
    blank=True) # validators should be a list
    age=models.SmallIntegerField(default="0")
    reasons=models.TextField(default="Unknown")

    def __str__(self):
        return self.parent_name
