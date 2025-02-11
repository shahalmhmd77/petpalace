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
from .forms import *


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

from datetime import datetime
def index(request):

    banners = [
    {
        "title": "Happy Pets",
        "description": "Your pet deserves the best!",
        "image_url": "https://th.bing.com/th/id/OIP.GTpg1AGnrBKB2-9OyG0qVQHaEK?w=320&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7"
    },
    {
        "title": "New Adoption Center",
        "description": "Find your new best friend today!",
        "image_url": "https://images.pexels.com/photos/4587993/pexels-photo-4587993.jpeg"
    },
    {
        "title": "Special Grooming Services",
        "description": "Pamper your pet with luxury care!",
        "image_url": "https://images.pexels.com/photos/7210709/pexels-photo-721070"
    }
]
    
    events = Events.objects.filter(event_date__gte=datetime.now())
    products=Product.objects.all()
    return render(request, 'petpalaceapp/index.html', {'banners': events, 'products':products}) 

def shop(request):
    return render(request, 'petpalaceapp/shop.html') 


def trainer_dashboard(request):
    return render(request, 'petpalaceapp/trainer_dashboard.html') 


def grooming(request):
    # service_type='Grooming'
    services=Service.objects.filter(trainer__user=request.user,service_type='Grooming')
    return render(request, 'petpalaceapp/grooming.html',{'services':services}) 


def boarding(request):
    # service_type='Boarding'
    services=Service.objects.filter(trainer__user=request.user,service_type='Boarding')
    return render(request, 'petpalaceapp/boarding.html',{"services":services}) 

def training(request):
    # service_type='Training'
    services=Service.objects.filter(trainer__user=request.user,service_type='Training')
    return render(request, 'petpalaceapp/training.html',{'services':services})

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
    user = request.user
    pets=Pet.objects.filter(owner=user)
    return render(request, 'petpalaceapp/my_pets.html',{'pets':pets})



def register_pet(request):
    if request.method == 'POST':
        pet_name = request.POST.get('pet_name')
        pet_type = request.POST.get('pet_type')
        contact = request.POST.get('contact')
        image = request.FILES.get('image')

        # Save the new pet to the database
        Pet.objects.create(
            owner=request.user,
            name=pet_name,
            pet_type=pet_type,
            contact=contact,
            image=image

        )

        # Redirect to a success page or the main list
        messages.success(request, 'Pet registered successfully!')
        return redirect('my_pets')  # Replace 'home' with your desired view name

    return render(request, 'petpalaceapp/register_pet.html')

def delete_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    pet.delete()
    messages.success(request, 'Pet deleted successfully!')
    return redirect('my_pets')


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
    orders = BuyHistory.objects.filter()
    return render(request, 'shop_order_history.html', {'orders': orders})

def user_profile(request):
    user_data=get_object_or_404(Customer,user=request.user)
    if request.method == 'POST':
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('phone')
        location = request.POST.get('location')
        username = request.POST.get('username')
        user_data.user.username = username
        user_data.user.save()

        user_data.full_name = full_name
        user_data.name = username
        user_data.email = email
        user_data.contact = contact_number
        user_data.location = location
        user_data.expertise = request.POST.get('expertise')
        user_data.experience = request.POST.get('experience')
        user_data.bio = request.POST.get('bio')
        user_data.image = request.FILES.get('image', user_data.image)
        user_data.save()
        return redirect('trainer_profile')
    return render(request,'user_profile.html',{'user_data':user_data})


def trainer_profile(request):
    user_data=get_object_or_404(Trainer,user=request.user)
    return render(request,'trainer_profile.html',{'user_data':user_data})


from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('login')


def trainer_management(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainer_management.html', {'trainers': trainers})


def add_trainer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        expertise = request.POST.get('expertise')
        experience = request.POST.get('experience')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        image = request.FILES.get('image')
        if not username and not email and not password:
            messages.success(request, 'username ,email, password missing!')
            return redirect('trainer_management')

        new_trainer = Trainer(
            name=name,
            expertise=expertise,
            experience=experience,
            contact=contact,
            user=User.objects.create_user(username=username, email=email, password=password),
            bio=bio,
            image=image
        )
        new_trainer.save()
        messages.success(request, 'Trainer added successfully!')
        return redirect('trainer_management')

    return render(request, 'add_trainer.html') 


def delete_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    trainer.user.delete()
    trainer.delete()
    messages.success(request, 'Trainer deleted successfully!')
    return redirect('trainer_management')

def edit_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == 'POST':
        trainer.name = request.POST.get('name')
        password = request.POST.get('password')
        if password and not password == '':
            trainer.user.set_password(password)

        trainer.user.username = request.POST.get('username')
        trainer.expertise = request.POST.get('expertise')
        trainer.experience = request.POST.get('experience')
        trainer.contact = request.POST.get('contact')
        trainer.bio = request.POST.get('bio')
        trainer.image = request.FILES.get('image', trainer.image)
        trainer.save()
        messages.success(request, 'Trainer updated successfully!')
        return redirect('trainer_management')
    return render(request, 'edit_trainer.html', {'trainer': trainer})


def adoption(request):
    my_pets = Pet.objects.filter(owner=request.user)
    my_adoptions = PetAdoption.objects.filter(pet__owner=request.user)
    other_adoptions = PetAdoption.objects.exclude(pet__owner=request.user)
    print(other_adoptions)

    return render(request, 'adoption.html', {
        'pets': my_pets,
        'my_adoptions': my_adoptions,  
        'adoption_ads': other_adoptions  
    })

def add_adoption(request):
    if request.method == 'POST':
        pet_id = request.POST.get('pet_id')
        pet=get_object_or_404(Pet,id=pet_id)
        contact = request.POST.get('contact')
        location = request.POST.get('location')
        date=request.POST.get('date')

        PetAdoption.objects.create(
            pet=pet,
            contact=contact,
        )

        messages.success(request, 'Adoption request submitted successfully!')
        return redirect('adoption')

    return redirect('adoption')


def service(request):
    pets=Pet.objects.filter(owner=request.user)
    booking=Service.objects.filter(pet__owner=request.user)
    return render(request, 'service.html',{'pets':pets,'booking':booking})


def add_service(request):
    if request.method == 'POST':
        pet_id = request.POST.get('pet_name')
        pet=get_object_or_404(Pet,id=pet_id)

        form = PetServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.pet = pet
            service.save()
        else:
            print(form.errors)

        messages.success(request, 'Service request submitted successfully!')
        return redirect('service')

    return redirect('service')

def service_management(request):
    services = Service.objects.all()
    trainers=Trainer.objects.all()
    return render(request, 'service_management.html', {'services': services,'trainers':trainers})



def change_trainer(request):
    if request.method == 'POST':
        trainer_id = request.POST.get('trainer_id')
        service_id = request.POST.get('service_id')
        trainer = get_object_or_404(Trainer, id=trainer_id)
        service = get_object_or_404(Service, id=service_id)
        service.trainer = trainer
        service.save()
        messages.success(request, 'Trainer changed successfully!')
        return redirect('service_management')

    return redirect('service_management')


def trainer_history(request):
    history = Service.objects.filter(trainer__user=request.user)
    return render(request, 'trainer_history.html', {'history': history})


def grooming_completed(request):
    return render('grooming')


def list_products(request):
    products = Product.objects.all()
    return render(request, 'list_products.html', {'products': products})


def add_to_cart(request):
    item_id = request.GET.get('item_id', None)
    decrease = request.GET.get('decrease', False)
    remove = request.GET.get('remove', False)
    if item_id:
        product = get_object_or_404(Product, id=item_id)
        cart_items = request.session.get('cart_items', [])
        
        product_price = float(product.price)
        image = product.image.url if product.image else ''
        
        existing_item = next((item for item in cart_items if item['id'] == product.id), None)
        if remove: 
            if existing_item:
                cart_items.remove(existing_item)  
                messages.success(request, f'{product.name} has been removed from your cart.')
        elif existing_item:
            if decrease: 
                existing_item['quantity'] -= 1
                if existing_item['quantity'] <= 0:
                    cart_items.remove(existing_item)
            else:
                existing_item['quantity'] += 1
        else:
            cart_item = {
                'id': product.id,
                'name': product.name,
                'price': product_price, 
                'quantity': 1,
                'image':image
            }
            cart_items.append(cart_item)
        
        request.session['cart_items'] = cart_items
        if not decrease and not remove:
            messages.success(request, f'{product.name} has been added to your cart.')
    return redirect('cart_view')

@login_required(login_url='login')
def cart_view(request):
    cart_items = request.session.get('cart_items', [])
    total_price = sum(float(item['price']) * item['quantity'] for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


def product_payment(request):
    cart_items = request.session.get('cart_items', [])
    total_price = sum(float(item['price']) * item['quantity'] for item in cart_items)
    return render(request, 'product_payment.html', {'cart_items': cart_items, 'total_price': total_price})



def proceed_payment(request):
    if request.method == "POST":
        cart_items = request.session.get('cart_items', [])
        user = get_object_or_404(Customer, user=request.user)
        total_price = sum(float(item['price']) * item['quantity'] for item in cart_items)
        quantity_list = []

        for item in cart_items:
            product = get_object_or_404(Product, id=item['id'])
            obj = ProductWithQuantity.objects.create(product=product, quantity=item['quantity'])
            quantity_list.append(obj)

        payment_method = request.POST.get('payment_method')
        if payment_method == 'card':
            card_number = request.POST.get('card_number')
            expiry_date = request.POST.get('expiry_date')
            cvv = request.POST.get('cvv')
            cardholder_name = request.POST.get('cardholder_name')
            payment = BuyHistory.objects.create(user=user, total_amount=total_price,card_number=card_number,expiry_date=expiry_date,cardholder_name=cardholder_name,cvv=cvv,payment_method='card')
        
        elif payment_method == 'upi':
            upi_id = request.POST.get('upi_id')
            payment = BuyHistory.objects.create(user=user, total_amount=total_price,upi_id=upi_id,payment_method='upi')

        payment.supplements.add(*quantity_list)
        request.session['cart_items'] = [] 
        messages.success(request, "Your cart has been cleared.")
        return redirect('payment_success')
    
    return redirect('product_payment')

def payment_success(request):
    return render(request, 'payment_success.html')


def order_history_view(request):
    user = request.user
    buy_history = BuyHistory.objects.filter(user__user=user).order_by('-purchase_date')
    return render(request, 'user_order_history.html', {'buy_history': buy_history})

def events(request):
    if request.method == "POST":
        form = EventForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events') 
    else:
        form = EventForm()

    events_list = Events.objects.all()
    return render(request, 'add_events.html', {'form': form, 'events': events_list})


def delete_event(request, event_id):
    event = get_object_or_404(Events, id=event_id)
    event.delete()
    messages.success(request, 'Event deleted successfully!')
    return redirect('events')


def view_event(request, event_id):
    event = get_object_or_404(Events, id=event_id)
    return render(request, 'view_event.html', {'event': event})