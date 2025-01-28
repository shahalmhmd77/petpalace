from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

# Register the custom User model

from .models import Customer, Pet, Shop, Trainer,PetBoarding,GroomingService, trainingservice,AdoptionRequest

admin.site.register(Customer)
admin.site.register(Pet)
admin.site.register(Shop)
admin.site.register(Trainer)
admin.site.register(PetBoarding)
admin.site.register(GroomingService)
admin.site.register(trainingservice)
admin.site.register(AdoptionRequest)





