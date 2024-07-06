from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.utils import timezone
# Create your models here.

now = timezone.now()
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=250, blank=True, default="")
    contact = models.CharField(max_length=250,blank=True, default="")
    email = models.CharField(max_length=250,blank=True, default="")
    business_name = models.CharField(max_length=250)
    business_pic = models.FileField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])],)
    location = models.CharField(max_length=250)
    municipality = models.TextField(blank=True)
    province = models.TextField(blank=True)
    barangay = models.TextField(blank=True) 
    fb_account = models.TextField(blank=True)
   
   
    def __str__(self):
        return self.user.username

class Offer(models.Model):
    business = models.ForeignKey(Profile, on_delete=models.CASCADE)
    offer_name = models.TextField()
    price = models.TextField()


class Response(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    message = models.TextField()
    date_submitted = models.DateTimeField()
    