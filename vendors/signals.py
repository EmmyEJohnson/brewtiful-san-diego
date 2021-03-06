from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import VendorProfile



@receiver(post_save, sender=User)
def create_or_update_vendor_profile(sender, instance, created, **kwargs):
    if created:
        VendorProfile.objects.create(user=instance)
    instance.vendorprofile.save()
    
    
    
    
    
    
# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
# 	if created:
# 		vendorprofile = VendorProfile.objects.create(user=instance)