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
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    location = models.TextField(null=True, blank=True)
    expertise = models.CharField(max_length=100, null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='trainers', null=True, blank=True)

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


class OrderHistory(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    products=models.ForeignKey('productWithQuantity',on_delete=models.CASCADE,null=True,blank=True)
    quantity=models.IntegerField(default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ])

    def __str__(self):
        return f"Order on {self.order_date.strftime('%Y-%m-%d')} - Status: {self.status}"


class productWithQuantity(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    quantity=models.IntegerField(default=0)

    def __str__(self):
        return self.product.name



class PetTrainingData(models.Model):
    # Pet Information
    pet_name = models.CharField(max_length=50)
    pet_age = models.PositiveIntegerField(default=0)
    pet_breed = models.CharField(max_length=150,null=True,blank=True)

    # Trainer Information
    trainer_name = models.CharField(max_length=100,null=True,blank=True)

    session_date = models.DateField()
    session_duration = models.DurationField(help_text="Duration of the session (hh:mm:ss)")
    training_type = models.CharField(max_length=100, help_text="e.g., Obedience, Agility, Behavioral")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Pet Training Data"
        verbose_name_plural = "Pet Training Data"
        ordering = ['-session_date']

    def __str__(self):
        return f"Training Data for {self.pet_name} by {self.trainer_name} on {self.session_date}"




