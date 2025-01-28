

# from django import forms
# from .models import Pet

# class PetForm(forms.ModelForm):
#     class Meta:
#         model = Pet
#         fields = [ 'owner_name', 'contact', 'pet_type']
#         widgets = {
#             'owner_name': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter owner name',
#             }),
#             'contact': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter contact information',
#             }),
#             'pet_type': forms.Select(attrs={
#                 'class': 'form-control',
#             }),
#         }






from django import forms
from .models import PetBoarding

class PetBoardingForm(forms.ModelForm):
    class Meta:
        model = PetBoarding
        fields = ['service', 'start_date', 'end_date', 'drop_off_time', 'payment_method', 'feedback', 'customer_name']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'drop_off_time': forms.TimeInput(attrs={'type': 'time'}),
        }


from django import forms
from .models import GroomingService

class GroomingServiceForm(forms.ModelForm):
    class Meta:
        model = GroomingService
        fields = ['service_type', 'appointment_date', 'appointment_time', 'pet_name', 'owner_name', 'contact', 'special_requests']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time'}),
        }


from django import forms
from .models import GroomingSession

class Grooming(forms.ModelForm):
    class Meta:
        model = GroomingSession
        fields = ['pet_name', 'pet_age', 'pet_breed', 'groomer_name', 'session_date', 'services', 'cost']
        widgets = {
            'session_date': forms.DateInput(attrs={'type': 'date'}),
            'services': forms.Textarea(attrs={'placeholder': 'Enter services provided (e.g., Bathing, Nail Clipping)', 'rows': 4}),
            'cost': forms.NumberInput(attrs={'step': '0.01', 'placeholder': 'Enter cost (e.g., 50.00)'}),
        }

from django import forms
from .models import trainingservice

class PetOwnerTrainingForm(forms.ModelForm):
    class Meta:
        model = trainingservice
        fields = ['full_name', 'email', 'pet_name', 'pet_age', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'Any additional details?', 'rows': 4}),
        }


from django import forms
from .models import AdoptionRequest

class adopt_pet(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }


from django import forms
from .models import Trainer

class TrainerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'email', 'phone', 'expertise', 'bio']
