from django.shortcuts import render

from .models import Topic

# Writing a view
# A view function takes in information from a request, prepares the data needed to generate a page, and then sends the data back to the browers, often by using a template that defines what the page will look like.

# The import of render function at the top renders the response based on the data provided by views.

# When a URL request matches the pattern we just defined, django looks for a function called index() in the views.py file. Django then passes the request object to this view function. With no data needing to be processed we call the render() function.
# The render() function passes two arguments. The original request object and a template it can use to build the page. The template will be in index.html
def index(request):
    """The home page for Learning Log"""
    return render(request, "learningLogs/index.html")

# Topics page
# We added topics to our urls.py so we can access by going to /topics in the url.
# We now need to write the topics function to retrieve data from the database and send it to the template.

# We first need to import the model associated with the data we need at the top.
# The topics() function needs one parameter, the request object django received from the server
def topics(request):
    """Show all topics"""
    
    # We query the database by asking for the Topic objects, sorted by the dateAdded attribute. We store the resulting queryset in topics var.
    topics = Topic.objects.order_by("dateAdded")
    # We define a context that we'll send to the template. A context is a dictionary in qhich the keys are names we'll use in the template to access the data, and the values are the data we need to send to the template.
    context = {"topics": topics}
    # When building a page that uses data, we pass the context variable to render() as well as the request object and the path to the template
    return render(request, "learningLogs/topics.html", context)

# The topic view
# The topic() function needs to get the topic and all associated entries from the database

# This is the first view function that requires a param other than the request object. The function accepts the value captured by the expression /<int:topic_id>/ and stores it in topicId
def topic(request, topic_id):
    """Show a single topic and all its entries"""
    # We use get() to retrieve the topic, just as we did in the django shell.
    topic = Topic.objects.get(id=topic_id)
    # We get the entries associated with this topic, and we order them according to dateAdded. The minus sign sorts the results in reverse order, the most recent entries first.
    entries = topic.entry_set.order_by("-dateAdded")
    # We store the topic and entries in the context dictionary and send context to the template topic.html
    context = {
        "topic": topic, 
        "entries": entries
        }
    return render(request, "learningLogs/topic.html", context)

