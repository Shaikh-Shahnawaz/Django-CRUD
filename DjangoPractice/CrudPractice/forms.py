from django import forms
from .models import Student
from django.forms import ModelForm


class StudentForm(forms.ModelForm):
    class Meta:

        model = Student

        fields = ['name', 'email', 'phone', 'file']

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'file' : forms.FileInput(attrs={'class':'form-control-file'}),
        }