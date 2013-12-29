__author__ = 'AlbertoRinconBorreguero'
from django.forms import ModelForm
from django import forms
from ApuntUS.models import *


class ApunteForm(ModelForm):
    class Meta:
        model = Apunte
        fields = '__all__'