from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
 
 
class Provider(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)

class ProviderUpdate(models.Model):
    provider = models.ForeignKey(Provider, related_name='updates')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    created_by = models.ForeignKey(User)