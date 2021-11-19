from django.contrib import admin
from .models import VendorProfile, Brew, Post

# Register your models here.
admin.site.register(VendorProfile)
admin.site.register(Brew)
admin.site.register(Post)
