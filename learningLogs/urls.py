"""Defines URL patterns for learningLogs"""
# Made after editing urls.py in learningLog

# We add a docstring at the start so we know which urls.py we are working in.

# We import the path function, which is needed when mapping URLs to views
from django.urls import path
# Importing the views module, the dot tells python to import the views.py module from the same directory as the current urls.py module.
from . import views

# The variable appName helps django distinguish this urls.py file from files of the same name in other apps within the project.
appName = "learningLogs"
# The variable urlpatterns in this module is a list of individual pages that can requested from the learningLogs app.
urlpatterns = [
    # Home page
    # The actual URL pattern is a call to the path() function, which takes
    # three arguments. The first argument is a string that helps Django route
    # the current request properly. Django receives the requested URL and tries
    # to route the request to a view. It does this by searching all the URL patterns
    # we’ve defined to find one that matches the current request. Django ignores
    # the base URL for the project (http://localhost:8000 /), so the empty string
    # ('') matches the base URL. Any other URL won’t match this pattern, and
    # Django will return an error page if the URL requested doesn’t match any
    # existing URL patterns.
    # The second argument in path() specifies which function to call
    # in views.py. When a requested URL matches the pattern we’re defining,
    # Django calls the index() function from views.py(we’ll write this view function
    # in the next section). The third argument provides the name index for
    # this URL pattern so we can refer to it in other code sections. Whenever we
    # want to provide a link to the home page, we’ll use this name instead of writing
    # out a URL.
    path("", views.index, name="index"),
]

# On to views.py