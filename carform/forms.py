from django import forms
from .models import CarInformation

class CarInformationForm(forms.ModelForm):
    class Meta:
        model = CarInformation

