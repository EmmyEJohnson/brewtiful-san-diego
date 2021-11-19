from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import VendorProfile, Brew



class UserForm(UserCreationForm):

	first_name = forms.CharField(max_length=30, required=True,
		widget=forms.TextInput(attrs={'placeholder': 'Name of Company...'}))
	last_name = forms.CharField(max_length=30, required=False,
		widget=forms.TextInput(attrs={'placeholder': 'Additional information... (ex. "Slogan")'}))
	username = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': 'Email..'}))
	password1 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': 'Password..','class':'password'}))
	password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password..','class':'password'}))

	#reCAPTCHA token
	token = forms.CharField(
		widget=forms.HiddenInput())

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )


class AuthForm(AuthenticationForm):

	username = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': 'Email..'}))
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': 'Password..','class':'password'}))

	class Meta:
		model = User
		fields = ('username','password', )


class UserProfileForm(forms.ModelForm):

	address = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	locality = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	state = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	postal_code = forms.CharField(max_length=8, required=True, widget = forms.HiddenInput())
	country = forms.CharField(max_length=40, required=True, widget = forms.HiddenInput())
	longitude = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())
	latitude = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())


	class Meta:
		model = VendorProfile
		fields = ('address', 'locality', 'state', 'postal_code',
		 'country', 'longitude', 'latitude')

class EditProfileForm(ModelForm):
    
    class Meta:
        model = VendorProfile
        fields = ('company_name',)

class ProfileImageForm(ModelForm):

    class Meta:
        model = VendorProfile
        fields = ('image',)

class BrewForm(forms.ModelForm):
    class Meta:
        model = Brew
        fields = ('image', 'name', 'brew_type', 'brewery', 'description', 'price', )
      
        
# class CreatePostForm(ModelForm):
#     title = forms.CharField(max_length=100, required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Brew Name', 'class': 'modal-form-input',}))
#     description = forms.CharField(max_length=500, required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Description: Brew Type (ex. Ale, Lager, Lambic) from what Brewery', 'class': 'modal-form-input',}))
    
#     class Meta:
#         model: Post
#         fields = ('title', 'description', 'image')        