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


# Defining the entry model
# For a user to record what they've been learning about, we need to define a model for the kinds of entries users can make in their learning logs. Each entry needs to be associated with a particular topic. This relationship is called a many-to-one relationship, meaning many entries can be associated with one topic.

# The Entry class inherits from django's base Model just like Topic did.
class Entry(models.Model):
    """Something specific learned about a topic"""
    
    # Topic, a ForeignKey instance, is a database term. It's a reference to another record in the database. This is the code that connects each entry to a specific topic. Each topic is assigned a key, or ID, when it's created. When django needs to establish a connection between two pieces of data, it uses the key associated with each piece of info.
    # The on_delete... argument tells django that when a topic is deleted, all the entries associated with thta topic should be deleted as well. This is known as a cascading delete.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # test, an instance of TextField, doesn't need a size limit because we don't want to limit the size of individual entries.
    text = models.TextField()
    # The dateAdded attribute allows us to present entries in the order they were created and to place a timestamp next to each entry
    dateAdded = models.DateTimeField(auto_now_add=True)
    
    # The Meta class holds extra info for managing a model. It allows us to set a special attribute telling django to use Entries when it needs to refer to more than one entry. Without this, django would refer to multiple entries as Entrys.
    # verbose_name... has to be typed that way, it's a meta option
    class Meta:
        verbose_name_plural = "entries"
    
    # The method below tells django which info to show when it refers to individual entries. Because an entry can be a long body of text, we tell django to show just the first 50 characters of text. We also add an ellipsis to clarify that we're not always displaying the entire entry.
    def __str__(self):
        """Return a string representation of the model"""

        # 18-2. Short Entries: The __str__() method in the Entry model currently appends
        # an ellipsis to every instance of Entry when Django shows it in the admin site
        # or the shell. Add an if statement to the __str__() method that adds an ellipsis
        # only if the entry is longer than 50 characters. Use the admin site to add an
        # entry that’s fewer than 50 characters in length, and check that it doesn’t have
        # an ellipsis when viewed.
        if len(self.text) < 50:
            return f"{self.text}"
        else:
            return f"{self.text[:50]}..."
    
# Migrating the entry model
# Because we added a new model we need to migrate the database again.
# python manage.py makemigrations learningLogs

# and then:
# python manage.py migrate
