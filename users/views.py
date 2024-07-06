from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, Offer, Response
from django.contrib.auth import authenticate, login as auth_login
from django.utils import timezone
# Create your views here.

def mainConcerns(request):
    concerns = Response.objects.all().order_by('-id')
    
    context = {
        'concerns': concerns
    }
    
    return render(request, 'main/concerns.html', context)

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
                return redirect('customerDashboard')
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
        location = request.POST['business_location']
        business_pic = request.FILES.get('business_pic')
        name = request.POST['business_name']
        contact = request.POST['contact']
        email = request.POST['business_email']
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
                    user=new_user, location=location, contact=contact, email=email, business_pic=business_pic, business_name=name)
                new_profile.save()
               
                messages.success(request, 'Account created')
                return redirect('login')
        else:
            messages.error(request, 'Password does not match.')
            return redirect('register')
    return render(request, 'register.html')




def updateContact(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        fb = request.POST['fb']
        email = request.POST['email']
        
        profile.contact = phone_number
        profile.fb_account = fb
        profile.email = email
        profile.save()
        
        messages.success(request, 'Contact info Updated')
        return redirect(request.META.get('HTTP_REFERER'))



def updateLocation(request, profile_id):
    profile = Profile.objects.get(pk=profile_id)
    
    if request.method == 'POST':
        barangay = request.POST['barangay']
        municipality = request.POST['municipality']
        province = request.POST['province']
        
        profile.barangay = barangay
        profile.municipality = municipality
        profile.province = province
        profile.save()
        
        messages.success(request, 'Location info Updated')
        return redirect(request.META.get('HTTP_REFERER'))


def businessOwnerDashboard(request):
    return render(request, 'businessOwner/index.html')


def locationContact(request):
    return render(request, 'businessOwner/location.html')



def services(request):

    try:
        business = Profile.objects.get(user=request.user.id)
        offers = Offer.objects.filter(business=business.id)
    except Profile.DoesNotExist:
        # Handle the case where the Profile does not exist for the user
        messages.error(request, 'Profile does not exist.')
        return render(request, 'businessOwner/services.html')
    
    if request.method == 'POST':
        service_name = request.POST['service_name']
        offer = request.POST['offer']
        
        new_offer = Offer.objects.create(business=business, offer_name=service_name, price=offer)
        new_offer.save()
        messages.success(request, 'Services added Successfully!')
    
    context = {
        'offers': offers
    }
    return render(request, 'businessOwner/services.html', context)




def resortDetails(request, resort_id):
    user = User.objects.get(id=resort_id)
    offers = Offer.objects.filter(business=user.profile)
    
    context = {
        'user': user,
        'offers': offers,
    }
    return render(request, 'customer/resortDetails.html', context)



def customerDashboard(request):
    resorts = User.objects.filter(last_name='Business Owner').order_by('-id')
     
    context = {
        'resorts': resorts
    }
    
    return render(request, 'customer/index.html', context)


def customerConcerns(request):
    
    if request.method == 'POST':
        reason = request.POST['reason']
        message = request.POST['message']
        
        new_response = Response.objects.create(sender=request.user, reason=reason, message=message, date_submitted=timezone.now())
        new_response.save()
        messages.success(request, 'Concerns submitted')
    
    return render(request, 'customer/concerns.html')




def logoutUser(request):
    auth.logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('homepage')

def removeOffer(request, offer_id):
    Offer.objects.filter(id=offer_id).delete()
    messages.success(request, 'Service/Offer Removed')
    return redirect(request.META.get('HTTP_REFERER'))

def removeConcern(request, concern_id):
    Response.objects.filter(id=concern_id).delete()
    messages.success(request, 'Concern Removed')
    return redirect(request.META.get('HTTP_REFERER'))


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

