from django import forms
from django.db import models
from django.forms import fields
from .models import Person

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'email', 'password', 'profession')