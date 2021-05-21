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
                'class': 'form-control w-25',
            }),
            'product': forms.Select(attrs={
                'class': 'form-control w-25',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control w-25',
            }),
        }