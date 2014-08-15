# -*- coding: utf-8 -*-
from django.forms import ModelForm,Form
from django import forms
from models import  *

class request_formForm(ModelForm):
    #date_from = forms.DateField(widget=forms.DateInput(attrs={'class':'timepicker'}))
    #test_bool = forms.BooleanField()
    class Meta:
        model = request_form


