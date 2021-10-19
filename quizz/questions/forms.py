from django import forms
from django.forms import ModelForm
from .models import *


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['content']
