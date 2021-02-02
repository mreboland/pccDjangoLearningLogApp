from django.shortcuts import render, redirect
# We import the login() function to log the user in if their registration info is correct
from django.contrib.auth import login
# Importing the default UserCreationForm.
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# The register() view function needs to display a blank registration form when the registration page is first request and the process completed registration forms when they're submitted. When successful, the new user needs to be logged in.
def register(request):
    """Register a new user"""
    
    # Checking if we are responding to a POST request. If not, we make an instance of UserCreationForm with no initial data
    if request.method != 'POST':
        # Display blank registration form
        form = UserCreationForm()
    # If we're responding to a POST request, we make an instance of UserCreationForm based on the submitted data
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        
        # We check that the data is valid. Proper username, appropriate characters, pass matches, and nothing nefarious.
        if form.is_valid():
            # If valid, we save the username and the has of the pass to the db. The save() method returns the newly created user object which we assign to newUser.
            newUser = form.save()
            
            # Log the user in and then redirect to home page
            
            # When the user's info is saved, we log them in by calling the login() function with the request and newUser objects. This creates a valid session for the new user.
            login(request, newUser)
            # We then redirect the user to the home page where a personalized greeting in the hearder tells them their registration was successful.
            return redirect("learningLogs:index")
        
    # Display a blank or invalid form
    
    # Here we render the page, which will either be a blank form or a submitted form that is valid
    context = {"form": form}
    return render(request, "registration/register.html", context)
