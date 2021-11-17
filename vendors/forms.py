from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import VendorProfile



class UserForm(UserCreationForm):

	first_name = forms.CharField(max_length=30, required=True,
		widget=forms.TextInput(attrs={'placeholder': 'Name of Company...'}))
	last_name = forms.CharField(max_length=30, required=True,
		widget=forms.TextInput(attrs={'placeholder': 'Additional information... (example: Slogan)'}))
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
	town = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	county = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	post_code = forms.CharField(max_length=8, required=True, widget = forms.HiddenInput())
	country = forms.CharField(max_length=40, required=True, widget = forms.HiddenInput())
	longitude = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())
	latitude = forms.CharField(max_length=50, required=True, widget = forms.HiddenInput())


	class Meta:
		model = VendorProfile
		fields = ('address', 'town', 'county', 'post_code',
		 'country', 'longitude', 'latitude')