from django.urls import path
from . import views


urlpatterns = [
    
    path('<int:user_id>/removeUser/', views.removeUser, name='removeUser'),
    path('acceptUser/<int:user_id>/', views.acceptUser, name='acceptUser'),
    path('declineUser/<int:user_id>/', views.declineUser, name='declineUser'),
    
    path('customers', views.customers, name='customers'),
    path('mainDashboard', views.mainDashboard, name='mainDashboard'),
    path('mainLogin', views.mainLogin, name='mainLogin'),
    
    path('businessOwnerDashboard', views.businessOwnerDashboard, name='businessOwnerDashboard'),
    
    path('homepage', views.homepage, name='homepage'),
    path('login', views.login, name='login'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('register', views.register, name='register'),
]