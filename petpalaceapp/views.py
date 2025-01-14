from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .models import Pet, Shop, Trainer, Customer
from django.contrib.auth.models import User
from .models import Shop
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product


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

def add_shop(request):
    products = Product.objects.all()
    return render(request, 'petpalaceapp/add_shop.html', {'products': products}) 



def add_product(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description')
            price = request.POST.get('price')
            image = request.FILES.get('image')
            category = request.POST.get('category')

            # Save the new product to the database
            try:
                product = Product.objects.create(
                    name=name,
                    description=description,
                    price=price,
                    image=image,
                    category=category
                )
            except Exception as e:  # Handle any errors
                messages.error(request, f'An error occurred: {e}')
                return render(request, 'petpalaceapp/add_product.html')


            # Redirect to a success page or the main list
            messages.success(request, 'Product added successfully!')
            return redirect('add_shop')  # Replace 'product_list' with your desired view name

        return render(request, 'petpalaceapp/add_product.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'petpalaceapp/product_list.html', {'products': products})

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


def delete_product(request,product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('add_shop') 
