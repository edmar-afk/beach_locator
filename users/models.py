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
    
    def __str__(self):
        return self.user.username
    
class Business(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=250)
    profile_pic = models.FileField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])],)
    location = models.CharField(max_length=250)
    contact = models.CharField(max_length=50)
    