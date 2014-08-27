# -*- coding: utf-8 -*-
from django.forms import ModelForm,Form
from django.forms.models import inlineformset_factory
from django import forms
from models import  *

class request_formForm(ModelForm):
    #date_from = forms.DateField(widget=forms.DateInput(attrs={'class':'timepicker'}))
    #test_bool = forms.BooleanField()
    class Meta:
        model = request_form

saturday_off_requestFormSet =inlineformset_factory(request_form,saturday_off_request,extra=1)

