from django import forms
from .models import car


class CarForm(forms.ModelForm):

    class Meta:
        model = car
        fields = ("name","type","avg_s")
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'avg_s': forms.NumberInput(attrs={'class': 'form-control'})
        }