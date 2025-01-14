from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Pet, Shop, Trainer, Customer



class PetRegistrationForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'pet_type', 'owner_name', 'contact']
        widgets = {
            'pet_type': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
        }

