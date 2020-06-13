from django.conf import settings
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
# - Users: ForeignKey
# - Location: Country django-location-field 2.1.0
# - Description: Text

class Trip(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, 
                                    related_name='trip')
    trip_start = models.DateField(auto_now_add=False, blank=True)
    trip_end = models.DateField(auto_now_add=False, blank=True)
    tags = TaggableManager()

    def __str__(self):
        members = ','.join(str(member) for member in self.members.all())
        return "pk: {}, name: {}, members: {{{}}}".format(self.pk, self.name, members)
    
