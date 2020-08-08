#from django import forms
#from .models import enquiry
#from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

#class RegisterForm(forms.ModelForm):
#    class Meta:
#        model = enquiry
#        parent_name = forms.Charfield(label="name",max_length=200)
#        fields = ['parent_name', 'student_name', 'email', 'phone']
#        error_messages = {
#            NON_FIELD_ERRORS: {
#                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
#            }
#        }
