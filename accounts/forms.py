from django import forms
from django.db.models import fields
from django.forms import widgets

from .models import *

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'customer': forms.Select(attrs={
                'class': 'form-control',
            }),
            'product': forms.Select(attrs={
                'class': 'form-control',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
        }