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
    
# class Pet(models.Model):
#     PET_TYPE_CHOICES = [
#         ('dog', 'Dog'),
#         ('cat', 'Cat'),
#     ]
#     pet_type = models.CharField(max_length=10, choices=PET_TYPE_CHOICES)
#     owner_name = models.CharField(max_length=100, null=True, blank=True)
#     contact = models.CharField(max_length=10, null=True, blank=True)

#     def __str__(self):
#         return f"({self.pet_type})"


class Product(models.Model):
    name = models.CharField(max_length=255, default='Unnamed Product')  # Default name
    description = models.TextField(default='No description available')  # Default description
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Default price
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name





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
    



class GroomingSession(models.Model):
    pet_name = models.CharField(max_length=100)
    pet_age = models.PositiveIntegerField()
    pet_breed = models.CharField(max_length=100, blank=True, null=True)  # Optional
    groomer_name = models.CharField(max_length=100, blank=True, null=True)  # Optional
    session_date = models.DateField()
    services = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.pet_name} - {self.session_date}"









class Notification(models.Model):
    title=models.CharField(max_length=250)
    category=models.CharField(max_length=250)
    description=models.TextField(null=True,blank=True)


    def __str__(self):
        return self.title


class PetBoarding(models.Model):
    SERVICE_CHOICES = [
        ('standard', 'Standard Boarding'),
        ('luxury', 'Luxury Boarding'),
        ('premium', 'Premium Boarding'),
    ]

    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    drop_off_time = models.TimeField()
    payment_method = models.CharField(max_length=20)
    feedback = models.TextField(null=True, blank=True)
    customer_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.customer_name} for {self.service} service"
    

class GroomingService(models.Model):
    PACKAGE_CHOICES = [
        ('basic', 'Basic Grooming'),
        ('deluxe', 'Deluxe Grooming'),
        ('premium', 'Premium Grooming'),
    ]

    service_type = models.CharField(max_length=20, choices=PACKAGE_CHOICES)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    pet_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    special_requests = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pet_name} - {self.service_type} ({self.owner_name})"
    

class trainingservice(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    pet_name = models.CharField(max_length=255)
    pet_age = models.IntegerField()
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.pet_name}"
    

class Pet(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(null=True, blank=True)  # Allows null values
    available_for_adoption = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class AdoptionRequest(models.Model):
    pet = models.ForeignKey(Pet, related_name='adoption_requests', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Adoption Request for {self.pet.name} by {self.name}"
    




class Trainer(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    expertise = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        choices=[
            ('obedience', 'Obedience Training'),
            ('agility', 'Agility Training'),
            ('behavioral', 'Behavioral Training'),
            ('puppy', 'Puppy Training'),
        ]
    )
    bio = models.TextField(default='No bio provided')  # Default value for bio field

    def __str__(self):
        return self.name
