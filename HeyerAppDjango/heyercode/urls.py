from django.urls import path, include
from rest_framework import routers
from . import views

app_name="heyercode"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    
]