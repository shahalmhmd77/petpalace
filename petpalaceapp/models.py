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
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=10,null=True,blank=True)
    contact = models.CharField(max_length=10)
    image = models.ImageField(upload_to='pet_images/', null=True, blank=True)

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


class ProductWithQuantity(models.Model):
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


class PetAdoption(models.Model):
    pet=models.ForeignKey(Pet,on_delete=models.CASCADE,null=True,blank=True)
    adoption_date=models.DateField(null=True,blank=True)
    adopter=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    contact=models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        return f"Adoption of {self.pet.name} on {self.adoption_date}"
    


class Service(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True, blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, blank=True)
    pet_age = models.PositiveIntegerField(default=0)
    pet_breed = models.CharField(max_length=150, null=True, blank=True)
    adoption_date = models.DateField(null=True, blank=True)
    adopter = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=10, null=True, blank=True)
    service_type = models.CharField(max_length=10, null=True, blank=True)
    session_date = models.DateField(null=True, blank=True)
    session_duration = models.DurationField(null=True, blank=True, help_text="Duration of the session (hh:mm:ss)")
    training_type = models.CharField(max_length=100, null=True, blank=True, help_text="e.g., Obedience, Agility, Behavioral")
    grooming_type = models.CharField(max_length=100, null=True, blank=True)
    completed = models.BooleanField(null=True, blank=True)


    def __str__(self):
        return f"Service for {self.pet.name} on {self.adoption_date}"
    


class BuyHistory(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    supplements = models.ManyToManyField('ProductWithQuantity', blank=True)
    purchase_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_method = models.CharField(max_length=50, null=True, blank=True)  
    card_number = models.CharField(max_length=20, null=True, blank=True) 
    expiry_date = models.CharField(max_length=7, null=True, blank=True)  
    cvv = models.CharField(max_length=4, null=True, blank=True)  
    cardholder_name = models.CharField(max_length=100, null=True, blank=True)
    upi_id = models.CharField(max_length=100, null=True, blank=True)
    order_status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ] , null=True, blank=True)

    def __str__(self):
        return f"BuyHistory for {self.user} on {self.purchase_date}"


class Events(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    event_time = models.TimeField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='events', null=True, blank=True)

    def __str__(self):
        return self.event_name