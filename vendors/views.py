from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import View
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string
from .models import VendorProfile, Brew

from config.mixins import(
	AjaxFormMixin, 
	reCAPTCHAValidation,
	FormErrors,
	RedirectParams,
	)

from .forms import (
	UserForm,
	UserProfileForm,
	AuthForm,
  EditProfileForm,
  ProfileImageForm,
  BrewForm,
	)

result = "Error"
message = "There was an error, please try again"


class AccountView(TemplateView):

	template_name = "vendors/account.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)


def profile_view(request):

	user = request.user
	up = user.vendorprofile

	form = UserProfileForm(instance = up) 

	if request.is_ajax():
		form = UserProfileForm(data = request.POST, instance = up)
		if form.is_valid():
			obj = form.save()
			obj.has_profile = True
			obj.save()
			result = "Success"
			message = "Your profile has been updated"
		else:
			message = FormErrors(form)
		data = {'result': result, 'message': message}
		return JsonResponse(data)

	else:

		context = {'form': form}
		context['google_api_key'] = settings.GOOGLE_API_KEY
		context['base_country'] = settings.BASE_COUNTRY

		return render(request, 'vendors/profile.html', context)

# def edit_profile(request):
#     args = {}

#     if request.method == 'POST':
#         form = EditProfileForm(request.POST)
#         form.actual_user = request.user
#         if form.is_valid():
#             obj=form.save()
#             return reverse('edit_profile')
#     else:
#         form = EditProfileForm()

#     args['form'] = form
#     return render(request, 'vendors/edit_profile.html', args)
  
# # #Save
def save_vendorprofile_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            form = VendorProfile.objects.all()
            data['html_profile'] = render_to_string('vendors/profile.html', {
                'form': form
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data) 
  
def edit_profile(request, pk):
    vendorprofile = get_object_or_404(VendorProfile, pk=pk)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=vendorprofile)
    else:
        form = EditProfileForm(instance=vendorprofile)
    return save_vendorprofile_form(request, form, 'vendors/edit_profile.html')
    
      
def profile_picture_update(request):
    if request.method == 'POST':
       form = ProfileImageForm(request.POST, request.FILES)
       if form.is_valid():
           obj=form.save()
           return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
       else:
           return JsonResponse({'error': True, 'errors': form.errors})
    else:
        form = ProfileImageForm()
        return render(request, 'vendors/profile_picture_update.html', {'form': form})

class SignUpView(AjaxFormMixin, FormView):

	template_name = "vendors/sign_up.html"
	form_class = UserForm
	success_url = "/"

	#reCAPTURE key required in context
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["recaptcha_site_key"] = settings.RECAPTCHA_SITE_KEY
		return context

	#over write the mixin logic to get, check and save reCAPTURE score
	def form_valid(self, form):
		response = super(AjaxFormMixin, self).form_valid(form)	
		if self.request.is_ajax():
			token = form.cleaned_data.get('token')
			captcha = reCAPTCHAValidation(token)
			if captcha["success"]:
				obj = form.save()
				obj.email = obj.username
				obj.save()
				up = obj.vendorprofile
				up.captcha_score = float(captcha["score"])
				up.save()
				
				login(self.request, obj, backend='django.contrib.auth.backends.ModelBackend')

				#change result & message on success
				result = "Success"
				message = "Thank you for signing up"

				
			data = {'result': result, 'message': message}
			return JsonResponse(data)

		return response




class SignInView(AjaxFormMixin, FormView):

	template_name = "vendors/sign_in.html"
	form_class = AuthForm
	success_url = "/"

	def form_valid(self, form):
		response = super(AjaxFormMixin, self).form_valid(form)	
		if self.request.is_ajax():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			#attempt to authenticate user
			user = authenticate(self.request, username=username, password=password)
			if user is not None:
				login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
				result = "Success"
				message = 'You are now logged in'
			else:
				message = FormErrors(form)
			data = {'result': result, 'message': message}
			return JsonResponse(data)
		return response

# Sign Out View
def sign_out(request):

	logout(request)
	return redirect(reverse('vendors:sign-in'))



# Brew views
def brew_list(request):
    brews = Brew.objects.all()
    return render(request, 'brew_list.html', {'brews': brews})

def save_brew_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            brews = Brew.objects.all()
            data['html_brew_list'] = render_to_string('includes/partial_brew_list.html', {
                'brews': brews
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data) 
  
def brew_create(request):
    data = dict()

    if request.method == 'POST':
        form = BrewForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            brews = Brew.objects.all()
            data['html_brew_list'] = render_to_string('includes/partial_brew_list.html', {
                'brews': brews
            })
        else:
            data['form_is_valid'] = False
    else:
        form = BrewForm()

    context = {'form': form}
    data['html_form'] = render_to_string('includes/partial_brew_create.html',
        context,
        request=request
    )
    return JsonResponse(data)
  
  
def brew_update(request, pk):
    brew = get_object_or_404(Brew, pk=pk)
    if request.method == 'POST':
        form = BrewForm(request.POST, instance=brew)
    else:
        form = BrewForm(instance=brew)
    return save_brew_form(request, form, 'includes/partial_brew_update.html')
  
  
def brew_delete(request, pk):
    brew = get_object_or_404(Brew, pk=pk)
    data = dict()
    if request.method == 'POST':
        brew.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        brews = Brew.objects.all()
        data['html_brew_list'] = render_to_string('includes/partial_brew_list.html', {
            'brews': brews
        })
    else:
        context = {'brew': brew}
        data['html_form'] = render_to_string('includes/partial_brew_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)  