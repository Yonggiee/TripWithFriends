from django.conf import settings
from django.db import models

# Create your models here.
# - Users: ForeignKey
# - Location: Country django-location-field 2.1.0
# - Description: Text

class Trip(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField();
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, 
                                    related_name='trip')
