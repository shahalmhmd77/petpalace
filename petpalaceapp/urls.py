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
    path('trainer_dashboard/', views.trainer_dashboard, name='trainer_dashboard'),
    path('boarding', views.boarding, name='boarding'),
    path('training', views.training, name='training'),
    path('grooming', views.grooming, name='grooming'),
    path('manage_pets', views.manage_pets, name='manage_pets'),
    # path('success/', views.registration_success, name='pet_success'),


    path('add_training/', views.training_add, name='add_training'),
    path('edit_training/', views.training_edit, name='edit_training'),
    path('delete_training/<int:pk>/', views.training_delete, name='training_delete'),

    path('update_shop_profile/', views.update_shop_profile, name='update_shop_profile'),
    path('shop_products/', views.shop_products, name='shop_products'),
    path('add_product/', views.add_product, name='add_product'),
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('shop_order_history/', views.shop_order_history, name='shop_order_history'),

    path('user_profile/', views.user_profile, name='user_profile'),
    path('trainer_profile/', views.trainer_profile, name='trainer_profile'),
    path('logout/', views.logout_view, name='logout'),
    path('trainer_management/', views.trainer_management, name='trainer_management'),
    path('add_trainer/', views.add_trainer, name='add_trainer'),
    path('delete_trainer/<int:trainer_id>/', views.delete_trainer, name='delete_trainer'),
    path('edit_trainer/<int:trainer_id>/', views.edit_trainer, name='edit_trainer'),
    path('adoption/', views.adoption, name='adoption'),

    path('add_adoption/', views.add_adoption, name='add_adoption'),
    path('service/', views.service, name='service'),
    path('add_service/', views.add_service, name='add_service'),

    path('service_management/', views.service_management, name='service_management'),

    path('change_trainer/', views.change_trainer, name='change_trainer'),
    path('trainer_history/', views.trainer_history, name='trainer_history'),
    path('grooming_completed/', views.grooming_completed, name='grooming_completed'),






]

