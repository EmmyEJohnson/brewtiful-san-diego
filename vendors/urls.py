from django.urls import path
from django.conf.urls import url, include
from . import views


app_name = "vendors"

urlpatterns = [
	path('', views.AccountView.as_view(), name="account"),
	path('profile', views.profile_view, name="profile"),
  path('edit_profile', views.edit_profile, name="edit_profile"),
  path('profile_picture_update', views.profile_picture_update, name="profile_picture_update"),
  #Authentication routes
	path('sign_up', views.SignUpView.as_view(), name="sign_up"),
	path('sign_in', views.SignInView.as_view(), name="sign_in"),
	path('sign_out', views.sign_out, name="sign_out"),
  # Brew routes
  url(r'^brews/$', views.brew_list, name='brew_list'),
  url(r'^brews/create/$', views.brew_create, name='brew_create'),
  url(r'^brews/(?P<pk>\d+)/update/$', views.brew_update, name='brew_update'),
  url(r'^brews/(?P<pk>\d+)/delete/$', views.brew_delete, name='brew_delete'),
	]