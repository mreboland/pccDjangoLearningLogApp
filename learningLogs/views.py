from django.shortcuts import render

# Writing a view
# A view function takes in information from a request, prepares the data needed to generate a page, and then sends the data back to the browers, often by using a template that defines what the page will look like.

# The import of render function at the top renders the response based on the data provided by views.

# When a URL request matches the pattern we just defined, django looks for a function called index() in the views.py file. Django then passes the request object to this view function. With no data needing to be processed we call the render() function.
# The render() function passes two arguments. The original request object and a template it can use to build the page. The template will be in index.html
def index(request):
    """The home page for Learning Log"""
    return render(request, "learningLogs/index.html")


