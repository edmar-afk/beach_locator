from django.urls import path
from . import views


urlpatterns = [
    path('<int:offer_id>/removeOffer/', views.removeOffer, name='removeOffer'),
    path('<int:concern_id>/removeConcern/', views.removeConcern, name='removeConcern'),
    path('<int:user_id>/removeUser/', views.removeUser, name='removeUser'),
    path('acceptUser/<int:user_id>/', views.acceptUser, name='acceptUser'),
    path('declineUser/<int:user_id>/', views.declineUser, name='declineUser'),
    
    path('mainConcerns', views.mainConcerns, name='mainConcerns'),
    path('customers', views.customers, name='customers'),
    path('mainDashboard', views.mainDashboard, name='mainDashboard'),
    path('mainLogin', views.mainLogin, name='mainLogin'),
    
    path('<int:profile_id>/updateContact/', views.updateContact, name='updateContact'),
    path('<int:profile_id>/updateLocation/', views.updateLocation, name='updateLocation'),
    path('locationContact', views.locationContact, name='locationContact'),
    path('services', views.services, name='services'),
    path('businessOwnerDashboard', views.businessOwnerDashboard, name='businessOwnerDashboard'),
    
    
    path('<int:resort_id>/resortDetails/', views.resortDetails, name='resortDetails'),
    path('customerDashboard', views.customerDashboard, name='customerDashboard'),
    path('customerConcerns', views.customerConcerns, name='customerConcerns'),
    
    path('homepage', views.homepage, name='homepage'),
    path('login', views.login, name='login'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('register', views.register, name='register'),
]