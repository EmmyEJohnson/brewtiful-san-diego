from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
from PIL import Image
from io import BytesIO
import time

# Create your models here.

class VendorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Company Name", max_length=100, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='static/images/profile/')
    created_at = models.DateTimeField(auto_now_add=True)
 
    address = models.CharField(verbose_name="Address",max_length=100, null=True, blank=True)
    locality = models.CharField(verbose_name="City",max_length=100, null=True, blank=True)
    state = models.CharField(verbose_name="State",max_length=100, null=True, blank=True)
    postal_code = models.CharField(verbose_name="Zip Code",max_length=8, null=True, blank=True)
    country = models.CharField(verbose_name="Country",max_length=100, null=True, blank=True)
    longitude = models.CharField(verbose_name="Longitude",max_length=50, null=True, blank=True)
    latitude = models.CharField(verbose_name="Latitude",max_length=50, null=True, blank=True)

    captcha_score = models.FloatField(default = 0.0)
    has_profile = models.BooleanField(default = False)
	
    is_active = models.BooleanField(default = True)

    def __str__(self):
	      return self.name
 
    class Meta:
        ordering = ['-created_at']
    
    
class Brew(models.Model):
    ALE = 1
    LAGER = 2
    LAMBIC = 3
    BREW_TYPES = (
        (ALE, 'Ale'),
        (LAGER, 'Lager'),
        (LAMBIC, 'Lambic'),
    )
    name = models.CharField(max_length=100, null=True)
    brew_type = models.PositiveSmallIntegerField(choices=BREW_TYPES, null=True)
    brewery = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=255, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='static/images/brew/')
    
    def __str__(self):
        return self.name
       
      
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    vendorprofile = models.ForeignKey(VendorProfile, related_name='post', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='post/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        