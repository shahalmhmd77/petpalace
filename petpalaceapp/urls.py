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
    path('my-pets/', views.my_pets, name='my_pets'),
    path('shop/', views.shop, name='shop'),
    path('trainer_dashboard', views.trainer_dashboard, name='trainer_dashboard'),
    path('boarding', views.boarding, name='boarding'),
    path('training', views.training, name='training'),
    path('grooming', views.grooming, name='grooming'),
    path('manage_pets', views.manage_pets, name='manage_pets'),
    # path('success/', views.registration_success, name='pet_success'),


    path('add_training/', views.training_add, name='add_training'),
    path('edit_training/', views.training_edit, name='edit_training'),
    path('delete_training/<int:pk>/', views.training_delete, name='training_delete'),


]

