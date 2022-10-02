from dataclasses import fields
from pyexpat import model
from django import forms
from website.models import *

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput(attrs ={
                'class':'formName, form-control',
                'placeholder': 'Your name',
                
            }),
            'phone' : forms.NumberInput(attrs={
                'class' : 'fornumber, form-control',
                'placeholder': 'Your Phone Number'
            }),
            'message' : forms.Textarea(attrs={
                'class' : 'formessage, form-control',
                'placeholder' : 'Your Message'
            }),
            'email' : forms.EmailInput(attrs={
                'class': 'formemail, form-control',
                'placeholder': 'Your E-mail address'
            }),
        }