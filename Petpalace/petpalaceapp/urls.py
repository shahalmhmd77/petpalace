from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index, name='index'), 
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('about/', views.about, name='about'),
    path('price/', views.price, name='price'),
    path('product/', views.product, name='product'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('blog/', views.blog, name='blog'),
    path('shop_dashboard/', views.shop_dashboard, name='shop_dashboard'),
    path('pet_dashboard/', views.pet_dashboard, name='pet_dashboard'),
    path('register_pet/', views.register_pet, name='register_pet'),
    path('shop_logout/', views.shop_logout, name='shop_logout'),
    path('index/', views.index, name='index'),
    path('trainer_dashboard', views.trainer_dashboard, name='trainer_dashboard'),
    path('boarding', views.boarding, name='boarding'),
    path('training', views.training, name='training'),
    path('manage_pets', views.manage_pets, name='manage_pets'),
    path('edit/<int:pet_id>/', views.edit_pet, name='edit_pet'),
    path('delete/<int:pet_id>/', views.delete_pet, name='delete_pet'),
    path('trainer_grooming', views.trainer_grooming, name='trainer_grooming'),
    path('grooming', views.grooming, name='grooming'),
    # path('success/', views.registration_success, name='pet_success'),


    # path('add_training/', views.training_add, name='training_add'),
    # path('edit_training/', views.training_edit, name='edit_training'),
    # path('delete_training/<int:pk>/', views.training_delete, name='training_delete'),


    path('', views.home, name='home'),
    # path('add/', views.add_grooming, name='add_grooming'),
    # path('edit/<int:id>/', views.edit_grooming, name='edit_grooming'),
    # path('delete/<int:id>/', views.delete_grooming, name='delete_grooming'),



    path('pet_dashboard/', views.pet_list, name='my_pets'),                # List all pets
    path('register/', views.register_pet, name='register_pet'),  # Add a new pet
    path('edit/<int:pet_id>/', views.edit_pet, name='edit_pet'), # Edit a pet
    path('delete/<int:pet_id>/', views.delete_pet, name='delete_pet'), # Delete a pet

    path('logout/', views.logout_view, name='logout'),
    # path('shop_notifications/', views.shop_notifications, name='shop_notifications'),
    

    path('boarding_service/', views.boarding_service, name='boarding_service'),
    path('booking-confirmation/', views.booking_confirmation, name='booking_confirmation'),

    path('grooming_service/', views.grooming_service, name='grooming_service'),

    path('my_pets/', views.my_pets, name='my_pets'),


    path('view_boarding/', views.view_boarding, name='view_boarding'),
    path('view_grooming/', views.view_grooming, name='view_grooming'),
    path('view_training/', views.view_training, name='view_training'),

     path('training_service/', views.training_service, name='training_service'),


    # path('grooming_list', views.grooming_list, name='grooming_list'),       # List all sessions
    # path('add_grooming/', views.add_grooming, name='add_grooming'),     # Add a session
    # path('edit_grooming/<int:pk>/', views.edit_grooming, name='edit_grooming'),  # Edit a session
    # path('delete_grooming/<int:pk>/', views.delete_grooming, name='delete_grooming'),  # Delete a session

   

    path('register_trainer/', views.register_trainer, name='register_trainer'),

    
    path('shop_profile/', views.shop_profile, name='shop_profile'),
    
]





