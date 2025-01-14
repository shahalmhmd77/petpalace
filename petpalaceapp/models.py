from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=10)
    address = models.TextField()

    def __str__(self):
        return self.full_name
    

class Shop(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    location = models.TextField()

    def __str__(self):
        return self.name



class Trainer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    location = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Pet(models.Model):
    PET_TYPES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
    ]

    name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=10, choices=PET_TYPES)
    owner_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.pet_type})"
    

class Product(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    quantity= models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products', null=True, blank=True)

    def __str__(self):
        return 'products'