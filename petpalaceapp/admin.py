from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

# Register the custom User model

from .models import Customer, Pet, Shop, Trainer,Product, PetTrainingData,OrderHistory,ProductWithQuantity
from .models import *

admin.site.register(Customer)
admin.site.register(Pet)
admin.site.register(Shop)
admin.site.register(Trainer)
admin.site.register(Product)
admin.site.register(PetTrainingData)
admin.site.register(OrderHistory)
admin.site.register(ProductWithQuantity)
admin.site.register(PetAdoption)
admin.site.register(Service)


