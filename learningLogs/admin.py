from django.contrib import admin

# Registering a model with the admin site
# Django includes some models in the admin site automatically, such as User and Group. But the models we create need to be added manually.

# The code below first imports the model we want to register, Topic
# The dot in front of models telss django to look for models.py in the same directory as admin.py
from .models import Topic, Entry

# The code below tells django to manage our model through the admin site.
admin.site.register(Topic)
admin.site.register(Entry)

# To user the superuser account go to:
# http://localhost:8000/admin/
# and login