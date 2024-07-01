from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.

def customers(request):
    customers = User.objects.filter(last_name='Customer').order_by('-id')
    businessOwners = User.objects.filter(last_name='Business Owner').order_by('-id')
    
    context = {
        'customers':customers,
        'businessOwners':businessOwners,
    }
    return render(request, 'main/users.html', context)

def mainDashboard(request):
    return render(request, 'main/index.html')

def mainLogin(request):
    return render(request, 'main/mainLogin.html')

def homepage(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        info = authenticate(username=username, password=password)
        if info is not None:
            auth_login(request, info)
            if info.is_staff and info.last_name == 'Business Owner':
                return redirect('businessOwnerDashboard')
            elif info.is_staff and info.last_name == 'Customer':
                return redirect('businessOwnerDashboard')
            else:
                messages.error(request, "You are not approve to the admin. Please wait")
                return redirect('login')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fullname = request.POST['fullname']
        role = request.POST['role']
        location = request.POST['location']
        contact = request.POST['contact']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken.')
                return redirect('login')

            else:
                new_user = User.objects.create_user(
                    first_name=fullname, username=username, last_name=role, password=password1, is_staff=False, is_superuser=False )
                new_user.save()

                new_profile = Profile.objects.create(
                    user=new_user, location=location, contact=contact, email=email)
                new_profile.save()
                messages.success(request, 'Account created')
                return redirect('login')
        else:
            messages.error(request, 'Password does not match.')
            return redirect('register')
    return render(request, 'register.html')


def businessOwnerDashboard(request):
    return render(request, 'businessOwner/index.html')



def logoutUser(request):
    auth.logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('homepage')



def removeUser(request, user_id):
    User.objects.filter(id=user_id).delete()
    messages.success(request, 'User Removed')
    return redirect(request.META.get('HTTP_REFERER'))


def acceptUser(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_staff = True
    user.save()
    # You can redirect to a success page or to the same page
    messages.success(request, 'User Accepted')
    return redirect(request.META.get('HTTP_REFERER'))

def declineUser(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_staff = False
    user.save()
    # You can redirect to a success page or to the same page
    messages.success(request, 'User Declined')
    return redirect(request.META.get('HTTP_REFERER'))

