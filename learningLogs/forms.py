from django import forms

from .models import Topic, Entry

# The topic ModelForm
# Any page that lets a user enter and submit information on a web page is a form, even if it doesn't look like one. When users enter info, we need to validate that the info provided is the right kind of data and is not malicious (code that breaks our server). We then need to process and save valid info to the appropriate place in the db.
# The simplest way to build a form in django is to use a 'ModelForm' which uses the info from the models we defined in models.py to automatically build a form.

# We import the forms modules and the model we'll work with, called Topic at the top
# Below we define a class which inherits from forms.ModelForm
class TopicForm(forms.ModelForm):
    # The simplest version of a ModelForm consists of a nested Meta class telling django which model to base the form on and which fields to include int he form
    class Meta:
        # Here we build a form from the Topic model and include only the text field below model =
        model = Topic
        fields = ["text"]
        # Here we tell django not to generate a label for the text field
        labels = {"text": ""}
        
# On to urls.py

# The entry ModelForm
# We need to create a form associated with the Entry model but this time wiht a bit more customization than TopicForm

# We first import the class Entry from models.py
class EntryForm(forms.ModelForm):
    
    class Meta:
        # Everything is the same below as TopicForm
        model = Entry
        fields = ["text"]
        labels = {"text": ""}
        # A widget attribute is an HTML form element, such as a single-line text box, multi-line text area, or drop-down list.
        # By including the widgets attribute, we can override django's default widget choices. By telling django to use a forms.Textarea element, we're customizing the input widget for the first 'text' so the text area will be 80 columns wide instead of the default 40.
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}

# Back to urls.py
