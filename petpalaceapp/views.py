from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .models import Pet, Shop, Trainer, Customer
from django.contrib.auth.models import User
from .models import Shop,PetTrainingData
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *


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

def shop(request):
    return render(request, 'petpalaceapp/shop.html') 


def trainer_dashboard(request):
    return render(request, 'petpalaceapp/trainer_dashboard.html') 

def grooming(request):
    return render(request, 'petpalaceapp/grooming.html') 

def boarding(request):
    return render(request, 'petpalaceapp/boarding.html') 

def training(request):
    training=PetTrainingData.objects.all()
    return render(request, 'petpalaceapp/training.html',{'training_data':training}) 

def manage_pets(request):
    return render(request, 'petpalaceapp/manage_pets.html') 




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

    return render(request, 'petpalaceapp/register_pet.html')


def shop_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'index.html')


from django.shortcuts import render, get_object_or_404, redirect
from .models import PetTrainingData
from .forms import PetTrainingDataForm

def training_list(request):
    """Displays a list of all pet training sessions."""
    trainings = PetTrainingData.objects.all().order_by('-session_date')
    return render(request, 'training_list.html', {'trainings': trainings})


def training_add(request):
    if request.method == 'POST':

        form = PetTrainingDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training')
    else:
        form = PetTrainingDataForm()
    return redirect('training')
    

def training_edit(request):
    training = get_object_or_404(PetTrainingData, pk=request.POST.get('training_id'))
    if request.method == 'POST':
        form = PetTrainingDataForm(request.POST, instance=training)
        if form.is_valid():
            form.save()
            return redirect('training')
    else:
        return redirect('training')

def training_delete(request, pk):
    """Handles deleting a training session."""
    training = get_object_or_404(PetTrainingData, pk=pk)
    training.delete()
    return redirect('training')


 
def update_shop_profile(request):
    shop = get_object_or_404(Shop, user=request.user)
    if request.method == 'POST':
        shop_name = request.POST.get('shopName')
        owner_name = request.POST.get('ownerName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        shop.full_name = shop_name
        shop.owner_name = owner_name
        shop.user.email = email
        shop.contact = phone
        shop.location = address
        shop.save()
        shop.user.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('shop_dashboard')  # Redirect to the shop dashboard or another appropriate page

    return render(request, 'shop_owner_profile.html',{'shop':shop})  


def shop_products(request):
    products = Product.objects.all()
    return render(request, 'shop_products.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        product = Product(
            name=name,
            category=category,
            quantity=quantity,
            description=description,
            price=price,
            image=image
        )
        product.save()
        messages.success(request, 'Product added successfully!')
    return redirect('shop_products') 


def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.category = request.POST.get('category')
        product.quantity = request.POST.get('quantity')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.image = request.FILES.get('image', product.image)  

        product.save()
        messages.success(request, 'Product updated successfully!')
    return redirect('shop_products')


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('shop_products')


def shop_order_history(request):
    orders = OrderHistory.objects.filter()
    return render(request, 'shop_order_history.html', {'orders': orders})