from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *



class PetRegistrationForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'pet_type', 'contact']
        widgets = {
            'pet_type': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
        }


from .models import PetTrainingData
class PetTrainingDataForm(forms.ModelForm):
    class Meta:
        model = PetTrainingData
        fields = ['pet_name', 'pet_age', 'pet_breed', 'trainer_name', 'session_date', 'session_duration', 'training_type']
        widgets = {
            'session_date': forms.DateInput(attrs={'type': 'date'}),
            'session_duration': forms.TimeInput(attrs={'type': 'time'}),
        }


class PetServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
     

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['event_name', 'event_date', 'event_time', 'location', 'description','image']
