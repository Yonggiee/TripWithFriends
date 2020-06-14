from django.conf import settings
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    friends = models.ManyToManyField("Profile", blank=True)
    exposed_name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return str(self.exposed_name)

