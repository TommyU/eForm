# -*- coding: utf-8 -*-
from django.forms import ModelForm
from models import  *

class request_formForm(ModelForm):
    class Meta:
        model = request_form
