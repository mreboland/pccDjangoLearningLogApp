from django.db import models

# Defining models
# Each user will need to create a number of topics in their learning log. Each entry they make will be tied to a topic, and these entries will be displayed as text. We'll also need to store the timestamp of each entry, so we can show users when they made each entry.

# A module called models is being imported for us, and we're being invited to create models of our own. A model tells Django how to work with the data that will be stored in the app. Code-wise, a model is just a class; it has attributes and methods, just like every class we've discussed.

# Model for the topics users will store:

# We created a class called Topic which inherits from Model, a parent class included in django that defines a model's basic functionality.
# We added two attributes to the Topic class: text and dateAdded
class Topic(models.Model):
    """A topic the user is learning about."""
    
    # CharField, an attribute, is a piece of data that's made up of characters or text. We use CharField when we want to store a small amount of text, such as a name, title, or city.
    # Wehn we define a CharField attribute, we have to tell django how much space it should reserve in the database. We give it a length of 200 characters which should be enough to hold most topic names.
    text = models.CharField(max_length=200)
    # DateTimeField, and attribute, is a piece of data that will record a date and time.
    # auto_now_add=True tells django to automatically set this attribute to the current date and time whenever the user creates a new topic.
    dateAdded = models.DateTimeField(auto_now_add=True)
    
    # Django calls a __str__() method to display a simple representation of a model. We've written a __str__() method that returns the string stored in the 'text' attribute
    def __str__(self):
        """return a string representation of the model."""
        return self.text

# Note: To see the different kinds of fields you can use in a model, see the Django Model
# Field Reference at https: // docs.djangoproject.com/en/2.2/ref/models
# /fields/. You won’t need all the information right now, but it will be extremely
# useful when you’re developing your own apps.

# Activating models
# To use our models, we have to tell Django to include our app in the overall
# project. Open settings.py (in the learningLog/learningLog directory)
