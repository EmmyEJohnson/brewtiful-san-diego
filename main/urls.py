from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('route', views.RouteView.as_view(), name="route"),
    path('map', views.MapView.as_view(), name="map"),
]