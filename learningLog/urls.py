"""learningLog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Mapping a URL
# Users request pages by entering URLs into a browser and clicking links, so
# we’ll need to decide what URLs are needed. The home page URL is first:
# it’s the base URL people use to access the project. At the moment the base
# URL, http: // localhost: 8000 /, returns the default Django site that lets us know
# the project was set up correctly. We’ll change this by mapping the base URL
# to Learning Log’s home page.


# The first two imports, import a module and a function to manage URLs for the admin site.
from django.contrib import admin
from django.urls import path, include

# urlpatterns is a variable, which includes sets of URLs from the app in the project
urlpatterns = [
    # The below includes the module admin.site.urls, which defines all the URLs that can be requested from the admin site.
    path('admin/', admin.site.urls),
    # To include the URLs for learningLogs. Make sure to import 'include'.
    path("", include("learningLogs.urls"))
]

# We now need to make a second urls.py in the learningLogs folder.