from __future__ import unicode_literals

from django.db import models
from  short.models import NewURL

class CountManager(models.Manager):
    def create_count(self,ins):
        if(isinstance(ins, NewURL)):
            obj, create = self.get_or_create(shortURL=ins)
            obj.count += 1
            obj.save()
            return obj.count
        return None

# Create your models here.
class Count(models.Model):
    shortURL = models.OneToOneField(NewURL)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)
    objects = CountManager()
    def __unicode__(self):
        return self.id