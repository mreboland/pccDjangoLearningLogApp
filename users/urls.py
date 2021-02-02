"""Defines URL patterns for users"""

from django.urls import path, include

# Import the views module from 'users', which we need because we're writing our own view for the registration page.
from . import views

# Creating a new app name so django can differentiate it from learninglogs
app_name = "users"
urlpatterns = [
    # Include default auth urls
    
    # The login page’s pattern matches the URL http://localhost:8000/users
    # /login/. When Django reads this URL, the word users tells Django to look in
    # users/urls.py, and login tells it to send requests to Django’s default login view.
    path("", include("django.contrib.auth.urls")),
    
    # Registration page
    path("register/", views.register, name="register")
]
