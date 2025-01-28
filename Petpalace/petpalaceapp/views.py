from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .models import Pet,Trainer, Customer
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

def about(request):
    return render(request, 'petpalaceapp/about.html')

def contact(request):
    return render(request, 'petpalaceapp/contact.html')

def price(request):
    return render(request, 'petpalaceapp/price.html')

def product(request):
     return render(request, 'petpalaceapp/product.html')

def footer(request):
    return render(request, '/petpalaceapp/footer.html')


def service(request):
    return render(request, 'petpalaceapp/service.html')

def team(request):
     return render(request, 'petpalaceap/team.html')


def testimonial(request):
    return render(request, 'petpalaceapp/testimonial.html')

def blog(request):
    return render(request, 'petpalaceapp/blog.html')


def shop_dashboard(request):
    return render(request, 'petpalaceapp/shop_dashboard.html')


def pet_dashboard(request):
    return render(request, 'petpalaceapp/pet_dashboard.html')

def index(request):
    return render(request, 'petpalaceapp/index.html') 

def grooming(request):
    return render(request, 'petpalaceapp/grooming.html')




def trainer_dashboard(request):
    return render(request, 'petpalaceapp/trainer_dashboard.html') 


def boarding(request):
    return render(request, 'petpalaceapp/boarding.html') 

def training(request):
    training=PetTrainingData.objects.all()
    return render(request, 'petpalaceapp/training.html',{'training_data':training}) 

def manage_pets(request):
    return render(request, 'petpalaceapp/manage_pets.html') 

def trainer_grooming(request):
    return render(request, 'petpalaceapp/trainer_grooming.html') 





def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        address = request.POST.get('address')
        password = request.POST.get('password')
        username = request.POST.get('username')

        # Save the new user to the database
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        Customer.objects.create(
            user=user,
            full_name=full_name,
            email=email,
            contact_number=contact_number,
            address=address
        )

        # Redirect to a success page or the main list
        messages.success(request, 'Account created successfully!')
        return redirect('login')  # Replace 'home' with your desired view name

    return render(request, 'petpalaceapp/registration.html')



def login_view(request):
    if request.method == 'POST':
            # Authenticate the user
            username = request.POST.get('username')
            password = request.POST.get('password')                                                                                                                                
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You're now logged in!")

                if user.is_staff:
                    return redirect('shop_dashboard')
                elif Customer.objects.filter(user=user).exists():
                    return redirect('pet_dashboard')
                elif Trainer.objects.filter(user=user).exists():
                    return redirect('trainer_dashboard')
                return redirect('index')  # Or wherever you want to redirect after login
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'petpalaceapp/login.html')




def my_pets(request):
    pets=Pet.objects.all()
    return render(request, 'petpalaceapp/my_pets.html',{'pets':pets})



def register_pet(request):
    if request.method == 'POST':
        pet_name = request.POST.get('pet_name')
        pet_type = request.POST.get('pet_type')
        owner_name = request.POST.get('owner_name')
        contact = request.POST.get('contact')

        # Save the new pet to the database
        Pet.objects.create(
            name=pet_name,
            pet_type=pet_type,
            owner_name=owner_name,
            contact=contact
        )

        # Redirect to a success page or the main list
        messages.success(request, 'Pet registered successfully!')
        return redirect('my_pets')  # Replace 'home' with your desired view name

    return render(request, 'petpalaceapp/regiter_pet.html')

def edit_pet(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    if request.method == 'POST':
        pet.name = request.POST['name']
        pet.owner_name = request.POST['owner_name']
        pet.contact = request.POST['contact']
        pet.pet_type = request.POST['pet_type']
        pet.save()
        return redirect('my_pets')
    return render(request, 'edit_pet.html', {'pet': pet})



def shop_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'index.html')






# from django.shortcuts import render, redirect, get_object_or_404
# from .models import GroomingSession
# from .forms import GroomingServiceForm

# # List all grooming sessions
# def grooming_list(request):
#     grooming_data = GroomingSession.objects.all()
#     return render(request, 'grooming.html', {'grooming_data': grooming_data})

# # Add a new grooming session
# def add_grooming(request):
#     if request.method == 'POST':
#         form = GroomingServiceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('shop_dashboard')
#     else:
#         form = GroomingServiceForm()
#     return render(request, 'petpalaceapp/grooming.html', {'form': form})

# # Edit an existing grooming session
# def edit_grooming(request, pk):
#     grooming_session = get_object_or_404(GroomingSession, pk=pk)
#     if request.method == 'POST':
#         form = GroomingServiceForm(request.POST, instance=grooming_session)
#         if form.is_valid():
#             form.save()
#             return redirect('shop_dashboard')
#     else:
#         form = GroomingServiceForm(instance=grooming_session)
#     return render(request, 'grooming.html', {'form': form})

# # Delete a grooming session
# def delete_grooming(request, pk):
#     grooming_session = get_object_or_404(GroomingSession, pk=pk)
#     grooming_session.delete()
#     return redirect('grooming_list')


# # Render Home Page
# def home(request):
#     grooming_data = GroomingSession.objects.all()
#     return render(request, 'grooming.html', {'grooming_data': grooming_data})



 

# from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
# from .models import Pet
# from .forms import PetForm

# # List of Pets
# def pet_list(request):
#     pets = Pet.objects.all()
#     return render(request, 'pet_list.html', {'pets': pets})

# # Add a Pet
# def register_pet(request):
#     if request.method == 'POST':
#         form = PetForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('pet_list')  # Redirect to the pet list page
#     else:
#         form = PetForm()
#     return render(request, 'register_pet.html', {'form': form})

# # Edit a Pet
# def edit_pet(request, pet_id):
#     pet = get_object_or_404(Pet, id=pet_id)
#     if request.method == 'POST':
#         form = PetForm(request.POST, instance=pet)
#         if form.is_valid():
#             form.save()
#             return redirect('pet_list')  # Redirect to the pet list page
#     else:
#         form = PetForm(instance=pet)
#     return render(request, 'edit_pet.html', {'form': form})

# # Delete a Pet
# def delete_pet(request, pet_id):
#     pet = get_object_or_404(Pet, id=pet_id)
#     if request.method == 'POST':
#         pet.delete()
#         return redirect('pet_list')  # Redirect to the pet list page
#     return render(request, 'delete_pet.html', {'pet': pet})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Pet
# from .forms import PetForm

# List Pets for Adoption
def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pets/adopt_pet.html', {'pets': pets})

# Add Pet
def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm()
    return render(request, 'pets/add_pet.html', {'form': form})

# Edit Pet
def edit_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm(instance=pet)
    return render(request, 'pets/edit_pet.html', {'form': form})

# Delete Pet
def delete_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == 'POST':
        pet.delete()
        return redirect('pet_list')
    return render(request, 'pets/delete_pet.html', {'pet': pet})


def logout_view(request):
    logout(request)
    return redirect('login')







from django.shortcuts import render, redirect
from .forms import PetBoardingForm
from .models import PetBoarding

def boarding_service(request):
    if request.method == 'POST':
        form = PetBoardingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet_dashboard')  # Redirect to a success page
    else:
        form = PetBoardingForm()
    return render(request, 'petpalaceapp/boarding_service.html', {'form': form})


def booking_confirmation(request):
    bookings = PetBoarding.objects.all()  # Fetch all bookings for display
    return render(request, 'booking_confirmation.html', {'bookings': bookings})


from django.shortcuts import render, redirect
from .forms import GroomingServiceForm

def grooming_service(request):
    if request.method == 'POST':
        form = GroomingServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet_dashboard')  # Redirect to a success page after submission
    else:
        form = GroomingServiceForm()
    return render(request, 'petpalaceapp/grooming_service.html', {'form': form})


def view_boarding(request):
    bookings = PetBoarding.objects.all()  # Fetch all entries
    return render(request, 'petpalaceapp/view_boarding.html', {'bookings': bookings})


from .models import GroomingService

def view_grooming(request):
    services = GroomingService.objects.all()  # Fetch all grooming services
    return render(request, 'petpalaceapp/view_grooming.html', {'services': services})

from django.shortcuts import render
from .models import trainingservice

def view_training(request):
    services = trainingservice.objects.all()  # Fetch all training services
    return render(request, 'petpalaceapp/view_training.html', {'services': services})




def shop_profile(request):
    # Dummy data to populate the profile page
    shop_data = {
        'shop_name': 'Shop Name',
        'owner': 'John Doe',
        'location': '123 Pet Street, Petville',
        'contact': '+123 456 7890',
        'total_pets': 20,
        'pending_requests': 5,
        'total_orders': 15,
        'pending_orders': 3,
    }
    
    return render(request, 'shop_profile.html', shop_data)



from django.shortcuts import render, redirect
from .forms import PetOwnerTrainingForm
from django.contrib import messages

def training_service(request):
    if request.method == 'POST':
        form = PetOwnerTrainingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered for the training program!')
            return redirect('pet_dashboard')
    else:
        form = PetOwnerTrainingForm()

    return render(request, 'petpalaceapp/view_grooming.html', {'form': form})



from django.shortcuts import render, redirect
from .models import Pet, AdoptionRequest
from .forms import adopt_pet

def home(request):
    # Fetch all pets that are available for adoption
    pets = Pet.objects.filter(available_for_adoption=True)
    
    return render(request, 'petpalaceapp/adopt_pet.html', {'pets': pets})

def adopt_pet(request, pet_id):
    # Get the pet being adopted by the user
    pet = Pet.objects.get(id=pet_id)
    
    if request.method == 'POST':
        # Process the adoption form
        form = adopt_pet(request.POST)
        if form.is_valid():
            adoption_request = form.save(commit=False)
            adoption_request.pet = pet
            adoption_request.save()
            return redirect('adopt_pet')
    else:
        form = adopt_pet()

    return render(request, 'petpalaceapp/adopt_pet.html', {'pet': pet, 'form': form})

def thank_you(request):
    return render(request, 'adopt_pet.html')


from django.shortcuts import render, redirect
from .forms import TrainerRegistrationForm

def register_trainer(request):
    if request.method == 'POST':
        form = TrainerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to a success page after registration
    else:
        form = TrainerRegistrationForm()
    return render(request, 'petpalaceapp/register_trainer.html', {'form': form})
