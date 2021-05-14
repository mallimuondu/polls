from django import forms
from django.forms import ModelForm

from .models import *


class CreatePollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = (
            'question', 'choice_1', 'choice_2', 'choice_3'
        )
        widgets = {
            'question': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter your Poll Question'
            }),
            'choice_1': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Choice 1'
            }),
            'choice_2': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Choice 2'
            }),
            'choice_3': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Choice 3'
            }),
        }
