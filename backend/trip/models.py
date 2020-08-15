from django.conf import settings
from django.db import models
from rest_framework.exceptions import APIException
from taggit.managers import TaggableManager

from profiles.models import Profile 

# Create your models here.
# - Users: ForeignKey
# - Location: Country django-location-field 2.1.0
# - Description: Text

country_list = ['Singapore', 'Malaysia', 'Thailand', 'South Korea', 
                'Japan', 'UK', 'USA', 'China', 'Vietnam', 'Indonesia',
                'Myammar', 'HongKong', 'Others']

class Trip(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    members = models.ManyToManyField(Profile, 
                                    related_name='trip')
    country = models.CharField(max_length=12, blank=False)
    trip_start = models.DateField(auto_now_add=False, blank=True, null=True)
    trip_end = models.DateField(auto_now_add=False, blank=True, null=True)
    tags = TaggableManager()

    def save(self, *args, **kwargs):
        if self.country and self.country not in country_list:
            raise APIException('Invalid country.')
        super().save(*args, **kwargs)

    def __str__(self):
        members = ','.join(str(member) for member in self.members.all())
        return "pk: {}, name: {}, members: {{{}}}".format(self.pk, self.name, members)
    
